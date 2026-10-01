import { useState } from "react";
import { api, USER_ID, fmtDate, fmtTime } from "../api";
import InviteModal from "./InviteModal";
export default function EventCard({ event, going, onRsvp, friends }) {
  const [share, setShare] = useState(false);
  const rsvp = async () => { await api.post("/rsvp", { user_id: USER_ID, event_id: event.id, invite_id: null }); onRsvp(event.id); };
  return <div className="card">
    {event.image_url && <img src={event.image_url} alt="" />}
    <div className="b"><h3>{event.title}</h3><div>📍 {event.venue || "TBA"}</div><div>📅 {fmtDate(event.date)}</div><div>🕖 {fmtTime(event.time)}</div>
      <p>👥 {friends ?? event.friends_attending} friends attending</p>
      <button className={going ? "on" : ""} onClick={rsvp} disabled={going}>{going ? "✓ Interested" : "Interested"}</button>
      {going && <button onClick={() => setShare(true)}>Share</button>}
    </div>{share && <InviteModal event={event} onClose={() => setShare(false)} />}</div>;
}
