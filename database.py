from motor.motor_asyncio import AsyncIOMotorClient
from datetime import datetime
from config import *

class Database:
    def __init__(self):
        self.client = None
        self.db = None
        self.connected = False
    
    async def connect(self):
        try:
            self.client = AsyncIOMotorClient(MONGO_URL)
            self.db = self.client[MONGO_DB_NAME]
            await self.client.admin.command('ping')
            self.connected = True
            print("Connected to MongoDB")
        except Exception as e:
            print(f"MongoDB error: {e}")
            self.connected = False

db = Database()
