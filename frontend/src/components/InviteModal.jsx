import { useEffect, useState } from "react";
import { api, USER_ID } from "../api";
export default function InviteModal({ event, onClose }) {
  const [url, setUrl] = useState(""); const [err, setErr] = useState("");
  useEffect(() => { api.post("/invites", { user_id: USER_ID, event_id: event.id }).then(r => setUrl(r.data.share_url)).catch(() => setErr("RSVP first to share.")); }, [event.id]);
  return <div className="modal" onClick={onClose}><div onClick={e => e.stopPropagation()}>
    <h3>Invite friends to {event.title}</h3>{err || <input readOnly value={url} style={{ width: "100%" }} onFocus={e => e.target.select()} />}
    <p><button onClick={() => navigator.clipboard.writeText(url)}>Copy link</button><button onClick={onClose}>Close</button></p></div></div>;
}
