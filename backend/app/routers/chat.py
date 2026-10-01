import re
from fastapi import APIRouter
from ..schemas import ChatIn
from ..services import event_service
router = APIRouter(prefix="/api/chat", tags=["chat"])
CATEGORIES = ["music", "comedy", "sports", "theatre", "theater", "tech", "art", "family", "festival", "concert"]
def extract(msg: str):
    m = re.search(r"\bin ([A-Za-z ]+?)(?:[?.!]|$)", msg)
    city = m.group(1).strip().title() if m else None
    cat = next((c for c in CATEGORIES if c in msg.lower()), None)
    return city, cat
@router.post("")
async def chat(body: ChatIn):
    city, cat = extract(body.message)
    try: events = await event_service.search(city, cat)
    except Exception: return {"message": "Sorry, I couldn't reach the events service.", "events": []}
    what = f"{cat} events" if cat else "events"
    msg = f"I found {what}{' in ' + city if city else ''}." if events else f"No {what} found{' in ' + city if city else ''}."
    return {"message": msg, "events": events}
