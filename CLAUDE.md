# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an economics thesis research project on **Proxy Means Testing (PMT)** — building indirect income measurement models using Machine Learning methods applied to Thai household survey data (Socio-Economic Survey 2564/2021, abbreviated SES 2564).

The thesis explores using ML techniques to estimate household income/welfare from observable proxy indicators, with the Thai SES dataset as the primary data source.

## Data

Raw survey microdata lives locally in `SES 2564 (2021)/` and is **excluded from git** (201MB). It contains:
- `Datadic SES 2564/` — data dictionary
- `Microdata SES 2564/` — raw household survey microdata
- `Questionnaire SES 2564/` — original questionnaire

Do not commit data files or add the `SES 2564 (2021)/` directory to version control.

## Workflow: OpenSpec

This project uses the **OpenSpec** workflow for managing research changes and tasks. Use the slash commands:

- `/propose` — propose a new research change (generates design doc + tasks)
- `/apply` — implement tasks from an open change
- `/sync` — sync delta specs to main specs
- `/archive` — finalize and archive a completed change

OpenSpec artifacts live in `openspec/` (config, specs, changes). The config is at `openspec/config.yaml`.

## Literature Review Skill

The project has a custom `literature-review` skill (`SKILL.md`) for conducting systematic academic literature reviews. Key scripts it references (to be created under `scripts/`):

```bash
# Aggregate and deduplicate search results from multiple databases
python scripts/search_databases.py combined_results.json --deduplicate --format markdown --output search_results.md

# Verify all DOIs in a review document
python scripts/verify_citations.py my_review.md

# Generate professional PDF from markdown
python scripts/generate_pdf.py my_review.md --citation-style apa --output my_review.pdf
```

PDF generation requires `pandoc` and `mactex`:
```bash
brew install pandoc && brew install --cask mactex
python scripts/generate_pdf.py --check-deps
```

## Thesis Documents

Finalized thesis/conference documents are stored in `thesis_doc/` as PDFs.

## Key Domain Concepts

- **PMT (Proxy Means Testing)**: Estimating household income/poverty using observable proxy variables rather than direct income reporting
- **SES 2564**: Thailand's National Statistical Office Socio-Economic Survey, Buddhist year 2564 (2021 CE)
- The thesis title translates to: *"Building Indirect Income Measurement Models Using Machine Learning"*
