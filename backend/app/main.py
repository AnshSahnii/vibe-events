from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from .config import FRONTEND_URL
from .database import init_db
from .routers import events, rsvp, invites, users, chat
from .websocket import manager
app = FastAPI(title="Vibe Events")
app.add_middleware(CORSMiddleware, allow_origins=[FRONTEND_URL], allow_methods=["*"], allow_headers=["*"])
for r in (events, rsvp, invites, users, chat): app.include_router(r.router)
@app.on_event("startup")
def startup(): init_db()
@app.websocket("/ws/events")
async def ws(socket: WebSocket):
    await manager.connect(socket)
    try:
        while True: await socket.receive_text()
    except WebSocketDisconnect: manager.disconnect(socket)
