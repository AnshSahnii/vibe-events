import httpx
from ..config import TICKETMASTER_API_KEY
URL = "https://app.ticketmaster.com/discovery/v2/events.json"
async def fetch(city=None, keyword=None, size=30):
    params = {"apikey": TICKETMASTER_API_KEY, "size": size, "sort": "date,asc"}
    if city: params["city"] = city
    if keyword: params["keyword"] = keyword
    async with httpx.AsyncClient(timeout=15) as c:
        r = await c.get(URL, params=params); r.raise_for_status()
    out = []
    for e in r.json().get("_embedded", {}).get("events", []):
        v = (e.get("_embedded", {}).get("venues") or [{}])[0]
        s = e.get("dates", {}).get("start", {})
        imgs = e.get("images") or [{}]
        out.append(dict(ticketmaster_id=e["id"], title=e["name"], venue=v.get("name"),
            city=(v.get("city") or {}).get("name"), event_date=s.get("localDate"),
            event_time=(s.get("localTime") or "")[:5] or None, image_url=imgs[0].get("url"), ticket_url=e.get("url")))
    return out
