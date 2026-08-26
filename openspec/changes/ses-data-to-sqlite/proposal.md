## Why

The SES 2564 microdata ships as 21 separate CSV files that must be re-read and merged on every analysis run, making iteration slow and fragile. Loading them once into a local SQLite database gives all downstream notebooks and scripts a fast, queryable, single source of truth.

## What Changes

- New ETL script (`src/data_loader.py`) reads all SES 2564 CSV files, renames all columns to readable snake_case names, and writes **thematic tables** into `data/ses2564.db`
- Raw CSV record types are grouped into 7 thematic tables (`target`, `household`, `housing_assets`, `members`, `income_sources`, `expenditure`, `debt`) plus one SQLite VIEW (`pmt_dataset`) that pre-joins the tables used for ML modeling
- `src/column_map.py` maps all 715 original SES field codes to readable names
- A `requirements.txt` is introduced with the needed Python dependencies (`pandas`, `tqdm`)
- A `notebooks/01_eda.ipynb` starter notebook connects to the DB and confirms the schema

## Capabilities

### New Capabilities

- `ses-db/ingest`: ETL pipeline that loads SES 2564 CSVs into a local SQLite database with thematic tables and a `pmt_dataset` view
- `ses-db/schema`: Documented table schema — thematic groupings, readable column names, join keys, and the `pmt_dataset` view definition

### Modified Capabilities

(none)

## Impact

- **New files**: `src/data_loader.py`, `data/ses2564.db` (generated, not committed), `requirements.txt`, `notebooks/01_eda.ipynb`
- **Dependencies**: `pandas`, `tqdm` (progress bar during ingest)
- **`.gitignore`**: `data/ses2564.db` must be excluded (too large to commit)
- No existing code is modified
