## Context

SES 2564 microdata exists as 21 CSV files (plus `.sav` Stata variants) totalling ~200MB. The CSV variants are already present under `Microdata SES 2564 CSV/`, so no format conversion is needed. See proposal.md for motivation.

The data is structured as record types (REC01–REC25), where most files are household-level (46,840 rows) and REC02 is individual-level (130,670 rows). The join key across all files is `NEW_HH_NO`.

## Goals / Non-Goals

**Goals:**
- Single `src/data_loader.py` script that reads all CSVs and writes `data/ses2564.db`
- Idempotent: re-running drops and recreates tables
- Fast enough to run in < 2 minutes on a laptop
- Works as both a standalone script and an importable module (for notebooks)

**Non-Goals:**
- Type inference beyond pandas defaults — column types are kept as-is
- Data validation or cleaning — that belongs in the feature engineering step
- Remote database (PostgreSQL, etc.) — SQLite is sufficient for single-user thesis work
- Ingesting the `.sav` files — CSVs already exist and are equivalent

## Decisions

### SQLite over other options

**Chose**: SQLite via Python's built-in `sqlite3` (through `pandas.to_sql`)

**Alternatives considered**:
- *Raw CSV reads each time*: No persistent schema, slow for repeated notebook runs
- *DuckDB*: Excellent for analytical queries, but adds a non-stdlib dependency; SQLite is universally available and sufficient for 46k-row data
- *Parquet files*: Good for columnar access but requires `pyarrow`, doesn't support SQL joins across files easily in notebooks

**Rationale**: SQLite requires zero infrastructure, is queryable with standard SQL in any notebook, and the file can be recreated from CSVs at any time.

### Thematic tables + `pmt_dataset` view

**Chose**: Group the raw CSV records into 7 thematic tables, then expose a `pmt_dataset` SQLite VIEW that pre-joins the tables needed for ML modeling.

```
CSV source records  →  Thematic SQLite tables
─────────────────────────────────────────────
REC01 (A/C-series income aggregates)  →  target
REC01 (A/C-series member/demog.)      →  household
REC03 (HH-series)                     →  housing_assets
REC02 (HM-series, individual-level)   →  members         ← stays as-is, not aggregated
REC13–16 (IW/IB/IA/IO-series)         →  income_sources
REC04–12 (EG/EF-series)               →  expenditure
REC25 (AE-series)                     →  debt

VIEW: pmt_dataset = target JOIN household JOIN housing_assets ON household_id
```

**Alternatives considered**:
- *One table per record type (REC01, REC02…)*: Mirrors the source but forces every analyst to know which record has which variables
- *Single flat joined table*: Convenient but duplicates data and obscures provenance

**Rationale**: Thematic tables make EDA intuitive (`SELECT * FROM housing_assets WHERE owns_motorcycle > 0`). The `pmt_dataset` view collapses the join for ML use (`pd.read_sql("SELECT * FROM pmt_dataset", con)`) — no duplication since views are computed on demand.

### `pandas.to_sql` with `if_exists='replace'`

**Chose**: Load each CSV into a DataFrame, rename columns via a mapping dict, then write to SQLite with `if_exists='replace'`.

**Rationale**: Handles idempotency automatically. For 46k rows, pandas in-memory load is fast. Column renaming happens in-memory on the DataFrame before writing — no post-processing SQL needed. The `chunksize` parameter handles REC18 which is split across three part files (these are concatenated before insert).

### Column renaming strategy

**Chose**: Rename all 715 columns across all tables using a single `src/column_map.py` dict, derived from the official NSO data dictionary XLS files.

**Alternatives considered**:
- *Rename only PMT-relevant columns*: Simpler but forces analysts to keep the codebook open for any column outside the model's top features
- *Keep all original codes*: Makes the DB opaque and unusable without the codebook

**Rationale**: The column map was generated programmatically from the data dictionary, so the cost of full coverage is low. A fully readable DB is a better long-term asset for the thesis and any future extensions.

### CSV source path via config, not hardcoded

**Chose**: The CSV directory path is read from a `config.py` or environment variable (`SES_CSV_DIR`), defaulting to the known relative path.

**Rationale**: The SES data directory is excluded from git and may live at different paths on different machines. A configurable path avoids editing source files.

## Risks / Trade-offs

- **REC18 is split into 3 parts** → Concatenate `REC18part1`, `REC18part2`, `REC18part3` into a single `REC18` table. Risk: if parts have different schemas, concat fails. Mitigation: assert column consistency before concat.
- **CSV encoding** → Thai NSO CSVs are sometimes encoded in TIS-620 or Windows-874. Risk: mojibake in string columns. Mitigation: read with `encoding='utf-8-sig'` first; fall back to `cp874` on `UnicodeDecodeError`.
- **DB file size** → ~200MB source → expect ~150MB SQLite file. Not committed to git (`.gitignore`). Risk: analyst forgets to run ingest after clone. Mitigation: notebooks check for DB existence at startup and print a clear error.

## Migration Plan

1. Run `pip install -r requirements.txt`
2. Set `SES_CSV_DIR` to the local path of `Microdata SES 2564 CSV/` (or use the default if cloning with the data in the standard location)
3. Run `python src/data_loader.py`
4. Verify with `python -c "import sqlite3; c=sqlite3.connect('data/ses2564.db'); print([r[0] for r in c.execute(\"SELECT name FROM sqlite_master WHERE type IN ('table','view')\")])"` — should list 7 tables + 1 view (`pmt_dataset`)

No rollback needed — the DB is generated, not committed. Deleting `data/ses2564.db` returns to pre-migration state.
