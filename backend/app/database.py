from datetime import datetime
from pymongo import MongoClient, ReturnDocument, ASCENDING
from .config import MONGODB_URL, DB_NAME
client = MongoClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
db = client[DB_NAME]
def now(): return datetime.utcnow()
def next_id(name: str) -> int:
    return db.counters.find_one_and_update({"_id": name}, {"$inc": {"seq": 1}}, upsert=True,
                                           return_document=ReturnDocument.AFTER)["seq"]
def init_db():
    db.events.create_index("ticketmaster_id", unique=True)
    db.events.create_index("id", unique=True)
    db.invites.create_index("token", unique=True)
    db.invites.create_index("id", unique=True)
    db.rsvps.create_index([("user_id", ASCENDING), ("event_id", ASCENDING)], unique=True)
    db.reminders.create_index([("user_id", ASCENDING), ("event_id", ASCENDING)], unique=True)
    db.users.create_index("id", unique=True)
    users = [(1, "Demo User", "demo@example.com")] + [(i, f"Friend {i}", f"friend{i}@example.com") for i in range(2, 6)]
    for uid, name, email in users:
        db.users.update_one({"id": uid}, {"$setOnInsert": {"id": uid, "name": name, "email": email,
                            "city": "Pune", "created_at": now()}}, upsert=True)
