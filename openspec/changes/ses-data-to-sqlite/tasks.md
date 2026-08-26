## 1. Project Scaffolding

- [x] 1.1 Create `src/`, `data/`, `notebooks/`, and `outputs/figures/` directories; verify they exist with `ls`
- [x] 1.2 Create `requirements.txt` with `pandas` and `tqdm`; verify `pip install -r requirements.txt` succeeds without errors
- [x] 1.3 Add `data/ses2564.db` and `data/*.db` to `.gitignore`; verify `git status` does not show the DB file after it is created

## 2. Config and Path Setup

- [x] 2.1 Create `src/config.py` exposing `SES_CSV_DIR` (env var `SES_CSV_DIR`, defaulting to `SES 2564 (2021)/Microdata SES 2564/Microdata SES 2564 CSV`) and `DB_PATH` (`data/ses2564.db`); verify the defaults resolve correctly when imported from the project root

## 3. Column Map

- [x] 3.1 Verify `src/column_map.py` is importable and complete: `python3 -c "from src.column_map import COLUMN_MAP; assert len(COLUMN_MAP) >= 715, len(COLUMN_MAP)"` — generated from the NSO data dictionary, 715 entries covering all record types

## 4. Ingest Script — Raw Loading

- [x] 4.1 Create `src/data_loader.py` with a `read_csv_records(csv_dir)` helper that reads all SES CSV files into a dict of DataFrames keyed by record type (e.g., `{"REC01": df, "REC02": df, ...}`), handles encoding (`utf-8-sig` with `cp874` fallback), concatenates the three REC18 part files into one `REC18` DataFrame, and shows `tqdm` progress per file; verify it returns 21 keys
- [x] 4.2 Add column renaming: after reading each DataFrame, apply `df.rename(columns=COLUMN_MAP, inplace=True)` so all columns use readable names; verify `monthly_income_percapita` exists in the REC01 DataFrame after renaming

## 5. Ingest Script — Thematic Table Building

- [x] 5.1 Define a `build_target(rec01_df)` function that selects `household_id`, `region`, `province`, `area_type`, `sampling_weight`, and the four income aggregate columns (`monthly_income_household`, `monthly_current_income_household`, `monthly_income_percapita`, `monthly_current_income_percapita`) from REC01; verify the result has 46,840 rows and 9 columns
- [x] 5.2 Define a `build_household(rec01_df)` function that selects all remaining REC01 columns not in `target` (member counts, expenditure aggregates, C-series demographics); verify the result has 46,840 rows and shares only `household_id` with `target`
- [x] 5.3 Define `build_housing_assets(rec03_df)` that passes through all REC03 columns (already renamed); verify 46,840 rows and `household_id` as key
- [x] 5.4 Define `build_members(rec02_df)` that passes through all REC02 columns as-is (individual-level, 130,670 rows); verify row count and that `household_id` is present
- [x] 5.5 Define `build_income_sources(recs)` that concatenates REC13, REC14, REC15, REC16 into a single `income_sources` table, retaining `household_id` and all IW/IB/IA/IO-series columns; verify all four record types are represented
- [x] 5.6 Define `build_expenditure(recs)` that concatenates REC04 through REC12 into a single `expenditure` table, retaining `household_id` and all EG/EF-series columns
- [x] 5.7 Define `build_debt(rec25_df)` that passes through all REC25 columns; verify 46,840 rows and that column `has_debt` (original `AE00`) is present

## 6. Ingest Script — Write to SQLite

- [x] 6.1 Create a `write_to_db(tables: dict[str, pd.DataFrame], db_path)` function that writes each table to SQLite using `if_exists='replace'` and sets `household_id` as the index for all household-level tables; verify all 7 tables exist in the DB after writing
- [x] 6.2 Create the `pmt_dataset` SQLite VIEW after writing all tables:
  ```sql
  CREATE VIEW IF NOT EXISTS pmt_dataset AS
  SELECT t.*, h.* EXCLUDE (household_id, region, province, area_type),
         ha.* EXCLUDE (household_id, region, province, area_type)
  FROM target t
  JOIN household h USING (household_id)
  JOIN housing_assets ha USING (household_id)
  ```
  If SQLite version does not support `EXCLUDE`, list columns explicitly; verify the view returns 46,840 rows
- [x] 6.3 Add a `if __name__ == "__main__":` block that wires together `read_csv_records`, the 7 `build_*` functions, `write_to_db`, and view creation; verify running `python src/data_loader.py` produces `data/ses2564.db`

## 7. Validation

- [x] 7.1 Verify the DB contains 7 tables + 1 view: `SELECT name, type FROM sqlite_master WHERE type IN ('table','view') ORDER BY type, name` should return 8 rows
- [x] 7.2 Verify row counts: `target`, `household`, `housing_assets`, `debt` each have 46,840 rows; `members` has 130,670 rows
- [x] 7.3 Verify `SELECT * FROM pmt_dataset LIMIT 1` returns one row with `monthly_income_percapita` and housing asset columns present
- [x] 7.4 Verify idempotency: run `python src/data_loader.py` a second time and confirm row counts are unchanged (no duplication)

## 8. Starter EDA Notebook

- [x] 8.1 Create `notebooks/01_eda.ipynb` that connects to `data/ses2564.db`, lists all tables and the view, loads `pmt_dataset` into a pandas DataFrame, and plots a histogram of `monthly_income_percapita`; verify the notebook runs end-to-end without errors using `jupyter nbconvert --to notebook --execute notebooks/01_eda.ipynb`
