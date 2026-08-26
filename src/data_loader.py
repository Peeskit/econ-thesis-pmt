"""
ETL pipeline: reads SES 2564 CSV files → thematic SQLite tables + pmt_dataset view.

Usage:
    python src/data_loader.py
    python src/data_loader.py --csv-dir /path/to/csvs --db-path /path/to/out.db
"""

import argparse
import sqlite3
from pathlib import Path

import pandas as pd
from tqdm import tqdm

from src.column_map import COLUMN_MAP
from src.config import DB_PATH, SES_CSV_DIR

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

# REC types that feed income_sources
_INCOME_RECS = {"REC13", "REC14", "REC15", "REC16"}

# REC types that feed expenditure
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
    """
    Read all SES CSV files from csv_dir, rename columns via COLUMN_MAP,
    and return a dict keyed by record type (e.g. 'REC01', 'REC18').
    REC18 part files are concatenated into a single 'REC18' entry.
    """
    csv_dir = Path(csv_dir)
    csv_files = sorted(csv_dir.glob("*.csv"))

    recs: dict[str, list[pd.DataFrame]] = {}
    rec18_parts: list[pd.DataFrame] = []

    for path in tqdm(csv_files, desc="Reading CSVs", unit="file"):
        name = path.stem  # e.g. "Microdata SES 2564 REC01"
        # Extract record key: last token(s) after "REC"
        upper = name.upper()
        idx = upper.rfind("REC")
        if idx == -1:
            continue
        rec_key = "REC" + upper[idx + 3:].lstrip()  # e.g. "REC01", "REC18PART1"

        df = _read_csv(path)
        df.rename(columns=COLUMN_MAP, inplace=True)
        # Normalise household_id column name (handles mixed-case source header)
        for alias in ("New_hh_no", "NEW_HH_NO"):
            if alias in df.columns:
                df.rename(columns={alias: "household_id"}, inplace=True)

        if "18PART" in rec_key or "18 PART" in rec_key:
            rec18_parts.append(df)
        else:
            key = rec_key[:5]  # trim to "REC01" etc.
            recs.setdefault(key, []).append(df)

    # Concatenate REC18 parts (parts cover different sub-sections so columns differ — outer join)
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

_HOUSEHOLD_TABLES = {"target", "household", "housing_assets", "debt"}

_PMT_VIEW_SQL = """
CREATE VIEW pmt_dataset AS
SELECT
    t.household_id,
    t.region,
    t.province,
    t.area_type,
    t.sampling_weight,
    t.monthly_income_household,
    t.monthly_current_income_household,
    t.monthly_income_percapita,
    t.monthly_current_income_percapita,
    h.*,
    ha.*
FROM target t
JOIN household h  USING (household_id)
JOIN housing_assets ha USING (household_id)
"""

# Columns duplicated by JOIN that we strip from h.* and ha.*
# SQLite doesn't support EXCEPT/EXCLUDE in SELECT, so we build explicit lists.

def _pmt_view_sql(con: sqlite3.Connection) -> str:
    """Build explicit-column SELECT for pmt_dataset view to avoid duplicates."""
    def cols(table: str) -> list[str]:
        cur = con.execute(f"PRAGMA table_info({table})")
        return [row[1] for row in cur.fetchall()]

    shared = {"household_id", "region", "province", "area_type", "sampling_weight"}
    target_cols = cols("target")
    household_cols = [c for c in cols("household") if c not in shared]
    housing_cols = [c for c in cols("housing_assets") if c not in shared]

    t_sel = ", ".join(f"t.{c}" for c in target_cols)
    h_sel = ", ".join(f"h.{c}" for c in household_cols)
    ha_sel = ", ".join(f"ha.{c}" for c in housing_cols)

    return f"""
CREATE VIEW pmt_dataset AS
SELECT {t_sel}, {h_sel}, {ha_sel}
FROM target t
JOIN household h USING (household_id)
JOIN housing_assets ha USING (household_id)
"""


def write_to_db(tables: dict[str, pd.DataFrame], db_path: Path) -> None:
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)

    con = sqlite3.connect(db_path)
    try:
        for name, df in tqdm(tables.items(), desc="Writing tables", unit="table"):
            df.to_sql(name, con, if_exists="replace", index=False)
            print(f"  {name}: {len(df):,} rows, {len(df.columns)} cols")

        # Drop and recreate the view
        con.execute("DROP VIEW IF EXISTS pmt_dataset")
        con.execute(_pmt_view_sql(con))
        con.commit()
        print("  pmt_dataset view created")
    finally:
        con.close()


# ── Entry point ───────────────────────────────────────────────────────────────

def main(csv_dir: Path = SES_CSV_DIR, db_path: Path = DB_PATH) -> None:
    print(f"CSV dir : {csv_dir}")
    print(f"DB path : {db_path}")

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

    write_to_db(tables, db_path)
    print(f"\nDone. Database written to {db_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load SES 2564 CSVs into SQLite")
    parser.add_argument("--csv-dir", type=Path, default=SES_CSV_DIR)
    parser.add_argument("--db-path", type=Path, default=DB_PATH)
    args = parser.parse_args()
    main(args.csv_dir, args.db_path)
