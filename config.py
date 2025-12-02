import os
from dotenv import load_dotenv

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
ADMINS = list(map(int, os.getenv("ADMINS").split(",")))

MONGO_URI = os.getenv("MONGO_URI")
MONGO_DBNAME = os.getenv("MONGO_DBNAME")

SHORTENER_URL = os.getenv("SHORTENER_URL")
SHORTENER_API = os.getenv("SHORTENER_API")

FS_CHANNEL_ID = os.getenv("FS_CHANNEL_ID")
SPLIT_SIZE_MB = int(os.getenv("SPLIT_SIZE_MB", 1900))
MAX_UPLOAD_MB = int(os.getenv("MAX_UPLOAD_MB", 2048))
