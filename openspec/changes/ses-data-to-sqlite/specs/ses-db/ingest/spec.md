## Purpose

Defines the ETL pipeline that reads all SES 2564 CSV record files and loads them into a local SQLite database, giving all downstream analysis a fast, single-file data source.

## ADDED Requirements

### Requirement: Ingest all SES CSV files

The system SHALL read every CSV file from the `SES 2564 (2021)/Microdata SES 2564/Microdata SES 2564 CSV/` directory and load each into a corresponding SQLite table named after its record type (e.g., `REC01`, `REC25`).

#### Scenario: All record files are present

- **WHEN** the ingest script is run and all 21 CSV files are present
- **THEN** the SQLite database SHALL contain 21 tables, each with the same columns as its source CSV and row counts matching the source

#### Scenario: A CSV file is missing

- **WHEN** the ingest script is run and one or more expected CSV files are absent
- **THEN** the script SHALL log a warning for each missing file and continue ingesting the remaining files without error

### Requirement: Deterministic re-ingest

The system SHALL support re-running the ingest script without manual cleanup — if the database file already exists, each table SHALL be replaced with the current CSV contents.

#### Scenario: Database already exists

- **WHEN** the ingest script is run a second time after a prior successful run
- **THEN** all tables SHALL be overwritten with fresh data and no duplicate rows SHALL be present

### Requirement: Primary key on NEW_HH_NO

Every ingested table SHALL preserve the `NEW_HH_NO` column as the household identifier. Tables with one row per household (REC01, REC03, REC25, etc.) SHALL have `NEW_HH_NO` declared as the primary key.

#### Scenario: Joining across tables

- **WHEN** a query joins REC01 and REC03 on `NEW_HH_NO`
- **THEN** the join SHALL return exactly one matching row per household with no duplicates

### Requirement: Ingest progress feedback

The system SHALL display per-file progress during ingest so the user can see that work is happening.

#### Scenario: Running ingest interactively

- **WHEN** the ingest script is run in a terminal
- **THEN** a progress indicator SHALL update for each file being loaded, showing at minimum the file name and completion status
