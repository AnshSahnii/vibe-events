from fastapi import APIRouter, HTTPException
from pymongo.errors import DuplicateKeyError
from ..database import db, next_id, now
from ..schemas import RSVPIn
from ..services import event_service
from ..websocket import manager
router = APIRouter(prefix="/api", tags=["rsvp"])
@router.post("/rsvp")
async def rsvp(body: RSVPIn):
    if not event_service.get_event(body.event_id): raise HTTPException(404, "Event not found")
    if body.invite_id and not db.invites.find_one({"id": body.invite_id}): raise HTTPException(404, "Invite not found")
    try:
        db.rsvps.insert_one({"id": next_id("rsvps"), "user_id": body.user_id, "event_id": body.event_id,
                             "invite_id": body.invite_id, "status": "interested", "created_at": now()})
        created = True
    except DuplicateKeyError:
        created = False
    n = event_service.friends_attending(body.event_id)
    if created:
        await manager.broadcast({"type": "friends_count_update", "event_id": body.event_id, "friends_attending": n})
    return {"status": "interested", "created": created, "friends_attending": n}
