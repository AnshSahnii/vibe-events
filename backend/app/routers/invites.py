import secrets
from fastapi import APIRouter, HTTPException
from pymongo import ReturnDocument
from ..config import FRONTEND_URL
from ..database import db, next_id, now
from ..schemas import InviteIn
from ..services import event_service
router = APIRouter(prefix="/api/invites", tags=["invites"])
@router.post("")
def create(body: InviteIn):
    if not db.rsvps.find_one({"user_id": body.user_id, "event_id": body.event_id}):
        raise HTTPException(403, "RSVP first to generate an invite")
    inv = db.invites.find_one({"creator_user_id": body.user_id, "event_id": body.event_id})
    if not inv:
        inv = {"id": next_id("invites"), "token": secrets.token_urlsafe(6), "event_id": body.event_id,
               "creator_user_id": body.user_id, "click_count": 0, "created_at": now()}
        db.invites.insert_one(inv)
    return {"token": inv["token"], "share_url": f"{FRONTEND_URL}/invite/{inv['token']}"}
@router.get("/{token}")
def open_invite(token: str):
    inv = db.invites.find_one_and_update({"token": token}, {"$inc": {"click_count": 1}},
                                         return_document=ReturnDocument.AFTER)
    if not inv: raise HTTPException(404, "Invalid invite")
    return {"invite_id": inv["id"], "click_count": inv["click_count"],
            "event": event_service.serialize(event_service.get_event(inv["event_id"]))}
