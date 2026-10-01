from pymongo.errors import DuplicateKeyError
from ..database import db, next_id, now
from . import ticketmaster
def friends_attending(event_id: int) -> int:
    return db.rsvps.count_documents({"event_id": event_id, "invite_id": {"$ne": None}})
def serialize(e: dict):
    return dict(id=e["id"], ticketmaster_id=e["ticketmaster_id"], title=e["title"], venue=e.get("venue"),
        city=e.get("city"), date=e.get("event_date"), time=e.get("event_time"), image_url=e.get("image_url"),
        ticket_url=e.get("ticket_url"), friends_attending=friends_attending(e["id"]))
def get_event(event_id: int):
    return db.events.find_one({"id": event_id}, {"_id": 0})
async def search(city=None, keyword=None):
    result = []
    for d in await ticketmaster.fetch(city, keyword):
        e = db.events.find_one({"ticketmaster_id": d["ticketmaster_id"]}, {"_id": 0})
        if not e:
            doc = {**d, "id": next_id("events"), "created_at": now()}
            try: db.events.insert_one(doc)
            except DuplicateKeyError: pass
            e = db.events.find_one({"ticketmaster_id": d["ticketmaster_id"]}, {"_id": 0})
        result.append(serialize(e))
    return result
