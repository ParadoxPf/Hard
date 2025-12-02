from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, MONGO_DBNAME

client = AsyncIOMotorClient(MONGO_URI)
db = client[MONGO_DBNAME]

async def add_user(user_id):
    if await db.users.find_one({"_id": user_id}) is None:
        await db.users.insert_one({"_id": user_id, "files_uploaded": 0})

async def get_user(user_id):
    return await db.users.find_one({"_id": user_id})
