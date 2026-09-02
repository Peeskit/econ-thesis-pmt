"""
ETL pipeline: reads SES 2564 CSV files → thematic PostgreSQL tables + pmt_dataset view.

Usage:
    python -m src.data_loader
    python -m src.data_loader --pg-url postgresql://localhost/ses2564
    python -m src.data_loader --csv-dir /path/to/csvs
"""

import argparse
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from tqdm import tqdm

from src.column_map import COLUMN_MAP
from src.config import PG_URL, SES_CSV_DIR

# ── Column sets for thematic splitting of REC01 ──────────────────────────────

_TARGET_READABLE = {
    "household_id",
    "region",
    "province",
    "area_type",
    "sampling_weight",
    "monthly_income_household",
    "monthly_current_income_household",
    "monthly_income_percapita",
    "monthly_current_income_percapita",
}

_INCOME_RECS = {"REC13", "REC14", "REC15", "REC16"}

_EXPENDITURE_RECS = {"REC04", "REC05", "REC06", "REC07", "REC08", "REC09",
                     "REC10", "REC11", "REC12"}


# ── CSV reading ───────────────────────────────────────────────────────────────

def _read_csv(path: Path) -> pd.DataFrame:
    for enc in ("utf-8-sig", "cp874", "latin-1"):
        try:
            return pd.read_csv(path, encoding=enc, low_memory=False)
        except (UnicodeDecodeError, pd.errors.ParserError):
            continue
    raise ValueError(f"Could not decode {path}")


def read_csv_records(csv_dir: Path) -> dict[str, pd.DataFrame]:
    csv_dir = Path(csv_dir)
    csv_files = sorted(csv_dir.glob("*.csv"))

    recs: dict[str, list[pd.DataFrame]] = {}
    rec18_parts: list[pd.DataFrame] = []

    for path in tqdm(csv_files, desc="Reading CSVs", unit="file"):
        name = path.stem
        upper = name.upper()
        idx = upper.rfind("REC")
        if idx == -1:
            continue
        rec_key = "REC" + upper[idx + 3:].lstrip()

        df = _read_csv(path)
        df.rename(columns=COLUMN_MAP, inplace=True)

        if "18PART" in rec_key or "18 PART" in rec_key:
            rec18_parts.append(df)
        else:
            key = rec_key[:5]
            recs.setdefault(key, []).append(df)

    if rec18_parts:
        recs["REC18"] = [pd.concat(rec18_parts, ignore_index=True, join="outer")]

    result = {k: pd.concat(v, ignore_index=True) for k, v in recs.items()}
    print(f"Loaded {len(result)} record types: {sorted(result)}")
    return result


# ── Thematic table builders ───────────────────────────────────────────────────

def build_target(rec01: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in _TARGET_READABLE if c in rec01.columns]
    return rec01[cols].copy()


def build_household(rec01: pd.DataFrame) -> pd.DataFrame:
    cols = [c for c in rec01.columns if c not in _TARGET_READABLE or c == "household_id"]
    return rec01[cols].copy()


def build_housing_assets(rec03: pd.DataFrame) -> pd.DataFrame:
    return rec03.copy()


def build_members(rec02: pd.DataFrame) -> pd.DataFrame:
    return rec02.copy()


def build_income_sources(recs: dict[str, pd.DataFrame]) -> pd.DataFrame:
    parts = []
    for key in sorted(_INCOME_RECS):
        if key in recs:
            df = recs[key].copy()
            df["_source_record"] = key
            parts.append(df)
    if not parts:
        raise ValueError("No income source records (REC13–16) found")
    return pd.concat(parts, ignore_index=True)


def build_expenditure(recs: dict[str, pd.DataFrame]) -> pd.DataFrame:
    parts = []
    for key in sorted(_EXPENDITURE_RECS):
        if key in recs:
            df = recs[key].copy()
            df["_source_record"] = key
            parts.append(df)
    if not parts:
        raise ValueError("No expenditure records (REC04–12) found")
    return pd.concat(parts, ignore_index=True)


def build_debt(rec25: pd.DataFrame) -> pd.DataFrame:
    return rec25.copy()


# ── Database writing ──────────────────────────────────────────────────────────

def _pmt_view_sql(engine) -> str:
    """Build explicit-column SELECT for pmt_dataset view to avoid duplicates."""
    with engine.connect() as con:
        def cols(table: str) -> list[str]:
            result = con.execute(text(
                "SELECT column_name FROM information_schema.columns "
                "WHERE table_name = :t ORDER BY ordinal_position"
            ), {"t": table})
            return [row[0] for row in result]

        shared = {"household_id", "region", "province", "area_type", "sampling_weight"}
        target_cols = cols("target")
        household_cols = [c for c in cols("household") if c not in shared]
        housing_cols = [c for c in cols("housing_assets") if c not in shared]

    t_sel = ", ".join(f't."{c}"' for c in target_cols)
    h_sel = ", ".join(f'h."{c}"' for c in household_cols)
    ha_sel = ", ".join(f'ha."{c}"' for c in housing_cols)

    return f"""
CREATE OR REPLACE VIEW pmt_dataset AS
SELECT {t_sel}, {h_sel}, {ha_sel}
FROM target t
JOIN household h USING (household_id)
JOIN housing_assets ha USING (household_id)
"""


def write_to_db(tables: dict[str, pd.DataFrame], pg_url: str) -> None:
    engine = create_engine(pg_url)

    for name, df in tqdm(tables.items(), desc="Writing tables", unit="table"):
        # Sanitise column names: strip leading/trailing whitespace
        df.columns = [c.strip() for c in df.columns]
        df.to_sql(name, engine, if_exists="replace", index=False, method="multi", chunksize=5000)
        print(f"  {name}: {len(df):,} rows, {len(df.columns)} cols")

    view_sql = _pmt_view_sql(engine)
    with engine.connect() as con:
        con.execute(text(view_sql))
        con.commit()
    print("  pmt_dataset view created")
    engine.dispose()


# ── Entry point ───────────────────────────────────────────────────────────────

def main(csv_dir: Path = SES_CSV_DIR, pg_url: str = PG_URL) -> None:
    print(f"CSV dir : {csv_dir}")
    print(f"PG URL  : {pg_url}")

    recs = read_csv_records(csv_dir)

    tables = {
        "target":         build_target(recs["REC01"]),
        "household":      build_household(recs["REC01"]),
        "housing_assets": build_housing_assets(recs["REC03"]),
        "members":        build_members(recs["REC02"]),
        "income_sources": build_income_sources(recs),
        "expenditure":    build_expenditure(recs),
        "debt":           build_debt(recs["REC25"]),
    }

    write_to_db(tables, pg_url)
    print(f"\nDone. Database loaded into {pg_url}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load SES 2564 CSVs into PostgreSQL")
    parser.add_argument("--csv-dir", type=Path, default=SES_CSV_DIR)
    parser.add_argument("--pg-url", default=PG_URL)
    args = parser.parse_args()
    main(args.csv_dir, args.pg_url)
