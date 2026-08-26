import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SES_CSV_DIR = Path(
    os.environ.get(
        "SES_CSV_DIR",
        ROOT / "SES 2564 (2021)" / "Microdata SES 2564" / "Microdata SES 2564 CSV",
    )
)

DB_PATH = Path(os.environ.get("DB_PATH", ROOT / "data" / "ses2564.db"))
