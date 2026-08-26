## Purpose

Documents the thematic table structure of the SQLite database, the column name mapping for all SES 2564 variables, and the `pmt_dataset` view definition used for ML modeling.

## ADDED Requirements

### Requirement: Seven thematic tables

The database SHALL contain exactly 7 tables, each grouping a semantically related set of SES record types. All columns SHALL use readable snake_case names from `src/column_map.py`. The join key across all tables is `household_id`.

| Table | Source records | Rows | Description |
|---|---|---|---|
| `target` | REC01 (A13–A16) | 46,840 | Household income aggregates — the PMT target variables |
| `household` | REC01 (A-series member counts, C-series demographics) | 46,840 | Household composition and demographic summary |
| `housing_assets` | REC03 (HH-series) | 46,840 | Housing conditions, vehicles, and appliances |
| `members` | REC02 (HM-series) | 130,670 | Individual member records (one row per member, not aggregated) |
| `income_sources` | REC13–REC16 (IW/IB/IA/IO-series) | varies | Detailed income by source (wages, business, farm, other) |
| `expenditure` | REC04–REC12 (EG/EF-series) | varies | Detailed household expenditure by category |
| `debt` | REC25 (AE-series) | 46,840 | Household debt repayment records |

#### Scenario: Listing all tables

- **WHEN** a user runs `SELECT name FROM sqlite_master WHERE type='table'`
- **THEN** the result SHALL contain exactly 7 rows: `target`, `household`, `housing_assets`, `members`, `income_sources`, `expenditure`, `debt`

### Requirement: `target` table columns

The `target` table SHALL contain the household identifier, geographic identifiers, sampling weight, and all income aggregate columns from REC01:

| Readable name | Original | Description |
|---|---|---|
| `household_id` | `NEW_HH_NO` | Unique household identifier (primary key) |
| `region` | `REG` | Region (1=Bangkok, 2=Central, 3=North, 4=Northeast, 5=South) |
| `province` | `CWT` | Changwat (province) code |
| `area_type` | `AREA` | Administrative area (1=Municipal, 2=Non-Municipal) |
| `sampling_weight` | `A52` | Survey sampling weight |
| `monthly_income_household` | `A13` | Avg. monthly total income per household (THB) |
| `monthly_current_income_household` | `A14` | Avg. monthly current income per household (THB) |
| `monthly_income_percapita` | `A15` | **PMT target** — avg. monthly total income per capita excl. servants (THB) |
| `monthly_current_income_percapita` | `A16` | Avg. monthly current income per capita excl. servants (THB) |

#### Scenario: Loading the target variable

- **WHEN** an analyst runs `SELECT household_id, monthly_income_percapita FROM target`
- **THEN** the result SHALL return 46,840 rows with no nulls in `monthly_income_percapita`

### Requirement: `household` table columns

The `household` table SHALL contain household composition counts and C-series demographic summaries from REC01 (all columns NOT in `target`):

| Readable name | Original | Description |
|---|---|---|
| `household_id` | `NEW_HH_NO` | Unique household identifier (primary key) |
| `region` | `REG` | Region |
| `province` | `CWT` | Changwat code |
| `area_type` | `AREA` | Administrative area |
| `n_members_incl_servants` | `A04` | Household size including servants |
| `n_members_excl_servants` | `A04_1` | Household size excluding servants |
| `n_wage_employees` | `A05` | No. of members earning wages/salaries |
| `n_nonfarm_business_operators` | `A06` | No. of members in non-farm business/industry |
| `monthly_expenditure_household` | `A07` | Avg. monthly total expenditure per household (THB) |
| `monthly_expenditure_percapita` | `A10` | Avg. monthly total expenditure per capita (THB) |
| `hh_head_age` | `C02` | Age of household head |
| `n_members_under15` | `C05` | No. of members under 15 years old |
| `n_govt_medical_welfare` | `C10` | No. of members with govt/state-enterprise health reimbursement |
| `n_universal_health_card` | `C11` | No. of members with Gold Card (universal health card) |
| `n_govt_education_loan` | `C24` | No. of members with government student loan |
| `n_people_bank_loan` | `C25` | No. of members with People's Bank loan |
| *(remaining A/C-series columns)* | A17–A51, C01, C03–C04, C06–C09, C12–C23, C26–C27 | All other REC01 columns not in `target` |

#### Scenario: Querying household demographics

- **WHEN** an analyst runs `SELECT household_id, n_members_excl_servants, hh_head_age FROM household`
- **THEN** the result SHALL return 46,840 rows with self-describing column names

### Requirement: `housing_assets` table columns

The `housing_assets` table SHALL contain all REC03 (HH-series) columns. Selected key columns:

| Readable name | Original | Description |
|---|---|---|
| `household_id` | `NEW_HH_NO` | Unique household identifier (primary key) |
| `monthly_rent_or_estimated` | `HH05` | Monthly rent or estimated rental value (THB) |
| `n_rooms_total` | `HH07` | No. of rooms excluding bathroom |
| `cooking_fuel` | `HH10` | Fuel type (0=none, 4=gas, 5=electricity, etc.) |
| `owns_motorcycle` | `HH17` | No. of motorcycles owned (0=none) |
| `owns_pickup_van` | `HH19` | No. of pick-up trucks/vans owned (0=none) |
| `owns_air_conditioner` | `HH35` | No. of air conditioners owned |
| `n_smartphones` | `HH41` | No. of smartphones owned |
| `n_fluorescent_bulbs` | `HH42` | No. of fluorescent tube lights |
| `n_cfl_bulbs` | `HH44` | No. of compact fluorescent bulbs |
| `n_led_e27_bulbs` | `HH45` | No. of LED E27 bulbs |
| *(remaining HH-series columns)* | HH01–HH04, HH06, HH08–HH09, HH11–HH16, HH18, HH20–HH34, HH36–HH40, HH43, HH46–HH47 | All other REC03 columns |

#### Scenario: Querying household assets

- **WHEN** an analyst runs `SELECT household_id, owns_motorcycle, owns_air_conditioner, n_smartphones FROM housing_assets`
- **THEN** the result SHALL return 46,840 rows with self-describing column names

### Requirement: `members` table stays individual-level

The `members` table SHALL contain all REC02 (HM-series) columns at individual-member granularity — one row per household member, **not** aggregated. It SHALL be joinable to other tables via `household_id`.

#### Scenario: Querying individual members

- **WHEN** an analyst runs `SELECT household_id, COUNT(*) as n FROM members GROUP BY household_id`
- **THEN** the result SHALL return 46,840 groups whose counts sum to 130,670

### Requirement: `pmt_dataset` view

The database SHALL contain a SQLite VIEW named `pmt_dataset` defined as an INNER JOIN of `target`, `household`, and `housing_assets` on `household_id`. It SHALL return one row per household (46,840 rows) with all columns from the three joined tables (deduplicating `household_id`, `region`, `province`, `area_type`).

#### Scenario: Loading data for ML modeling

- **WHEN** an analyst runs `SELECT * FROM pmt_dataset`
- **THEN** the result SHALL return exactly 46,840 rows and include `monthly_income_percapita`, all `household` feature columns, and all `housing_assets` feature columns — ready to load directly into pandas for modeling

#### Scenario: View survives re-ingest

- **WHEN** the ingest script is re-run and all tables are replaced
- **THEN** `pmt_dataset` SHALL continue to work without being manually recreated (it is a VIEW, not a materialized table)

### Requirement: DB file is not committed to version control

The generated database file (`data/ses2564.db`) SHALL be excluded from git via `.gitignore`. Only the ingest script and `column_map.py` are committed.

#### Scenario: Fresh clone setup

- **WHEN** a user clones the repository and runs `python src/data_loader.py` pointing to their local SES CSV directory
- **THEN** all 7 tables and the `pmt_dataset` view SHALL be recreated locally without requiring any large binary file from git
