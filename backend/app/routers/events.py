from fastapi import APIRouter, HTTPException
from ..services import event_service
router = APIRouter(prefix="/api/events", tags=["events"])
@router.get("")
async def list_events(city: str = None, keyword: str = None):
    return await event_service.search(city, keyword)
@router.get("/{event_id}")
def get_event(event_id: int):
    e = event_service.get_event(event_id)
    if not e: raise HTTPException(404, "Event not found")
    return event_service.serialize(e)
