import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# -------------------- Environment Variables -------------------- #
API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()

MONGO_URL = os.getenv("MONGO_URL", "").strip()        # MongoDB (Main DB)
DATABASE_URL = os.getenv("DATABASE_URL", "").strip()  # Optional (Postgres / stats)

# -------------------- Validation -------------------- #
if not API_ID:
    raise SystemExit("❌ API_ID not found. Exiting...")
elif not API_HASH:
    raise SystemExit("❌ API_HASH not found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("❌ BOT_TOKEN not found. Exiting...")
elif not MONGO_URL:
    raise SystemExit("❌ MONGO_URL not found. Exiting...")

# -------------------- Type Correction -------------------- #
try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("❌ API_ID must be an integer. Exiting...")

# -------------------- Database Fixes -------------------- #
# Fix DATABASE_URL if using PostgreSQL (Heroku / VPS)
if DATABASE_URL:
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace(
            "postgres://", "postgresql://", 1
        )
