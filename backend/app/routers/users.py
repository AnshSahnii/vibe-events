from fastapi import APIRouter
from ..database import db, now
from ..schemas import ReminderIn
from ..services import event_service
router = APIRouter(prefix="/api", tags=["users"])
@router.get("/users/{user_id}/rsvps")
def my_rsvps(user_id: int):
    ids = [r["event_id"] for r in db.rsvps.find({"user_id": user_id})]
    out = []
    for e in db.events.find({"id": {"$in": ids}}, {"_id": 0}):
        d = event_service.serialize(e)
        r = db.reminders.find_one({"user_id": user_id, "event_id": e["id"]})
        d["reminder"] = {"enabled": r["enabled"], "hours_before": r["hours_before"]} if r else None
        out.append(d)
    return out
@router.put("/reminders")
def set_reminder(body: ReminderIn):
    db.reminders.update_one({"user_id": body.user_id, "event_id": body.event_id},
        {"$set": {"enabled": body.enabled, "hours_before": body.hours_before},
         "$setOnInsert": {"created_at": now()}}, upsert=True)
    return {"enabled": body.enabled, "hours_before": body.hours_before}
