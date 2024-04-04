import os

if os.getenv("FLASK_ENV") in ["development", "production"]:
    RDS_PORT = os.getenv("RDS_PORT", 5432)
    RDS_HOST = os.getenv("RDS_HOST", "localhost")
    RDS_USERNAME = os.getenv("RDS_USERNAME", "postgres")
    RDS_PASSWORD = os.getenv("RDS_PASSWORD", "postgres")
    RDS_DB_NAME = os.getenv("RDS_DB_NAME", "blacklists")
    DATABASE_URI = f"postgresql://{RDS_USERNAME}:{RDS_PASSWORD}@{RDS_HOST}:{RDS_PORT}/{RDS_DB_NAME}"
else:
    DATABASE_URI = os.getenv("DATABASE_URI", "sqlite:///blacklists.db")
