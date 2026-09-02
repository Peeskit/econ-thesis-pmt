import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SES_CSV_DIR = Path(
    os.environ.get(
        "SES_CSV_DIR",
        ROOT / "SES 2564 (2021)" / "Microdata SES 2564" / "Microdata SES 2564 CSV",
    )
)

# SQLite fallback (kept for reference / lightweight use)
DB_PATH = Path(os.environ.get("DB_PATH", ROOT / "data" / "ses2564.db"))

# PostgreSQL connection URL
# Override with env var: export PG_URL="postgresql://user:pass@host:5432/dbname"
PG_URL = os.environ.get("PG_URL", "postgresql://localhost/ses2564")
