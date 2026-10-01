from pydantic import BaseModel
from typing import Optional
class RSVPIn(BaseModel):
    user_id: int; event_id: int; invite_id: Optional[int] = None
class InviteIn(BaseModel):
    user_id: int; event_id: int
class ReminderIn(BaseModel):
    user_id: int; event_id: int; enabled: bool = True; hours_before: int = 24
class ChatIn(BaseModel):
    message: str
