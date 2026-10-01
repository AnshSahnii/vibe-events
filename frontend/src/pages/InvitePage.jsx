import { useEffect, useRef, useState } from "react"; import { useParams } from "react-router-dom";
import { api, fmtDate, fmtTime } from "../api";
const FRIEND_ID = 2; // demo friend user (seeded). Change via ?uid= if desired.
export default function InvitePage() {
  const { token } = useParams(); const [inv, setInv] = useState(null); const [done, setDone] = useState(false); const once = useRef(false);
  useEffect(() => { if (once.current) return; once.current = true; api.get(`/invites/${token}`).then(r => setInv(r.data)).catch(() => setInv(false)); }, [token]);
  if (inv === false) return <div className="wrap">Invalid invite.</div>; if (!inv) return <div className="wrap">Loading…</div>;
  const e = inv.event, uid = +(new URLSearchParams(location.search).get("uid") || FRIEND_ID);
  const go = async () => { await api.post("/rsvp", { user_id: uid, event_id: e.id, invite_id: inv.invite_id }); setDone(true); };
  return <div className="wrap"><h2>You've been invited!</h2><h3>{e.title}</h3><div>📍 {e.venue}</div><div>📅 {fmtDate(e.date)}</div><div>🕖 {fmtTime(e.time)}</div>
    <p><button className={done ? "on" : ""} onClick={go} disabled={done}>{done ? "✓ Going" : "RSVP to Event"}</button></p></div>;
}
