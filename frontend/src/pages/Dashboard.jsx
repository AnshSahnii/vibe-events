import { useEffect, useState } from "react"; import { api, USER_ID, fmtDate } from "../api"; import ReminderSettings from "../components/ReminderSettings";
export default function Dashboard() {
  const [ev, setEv] = useState([]);
  useEffect(() => { api.get(`/users/${USER_ID}/rsvps`).then(r => setEv(r.data)); }, []);
  return <div className="wrap"><h2>My Events</h2>{!ev.length && <p>No RSVPs yet.</p>}
    {ev.map(e => <div className="card" key={e.id} style={{ padding: 12, marginBottom: 10 }}><b>✓ {e.title}</b><div>{fmtDate(e.date)} • {e.venue}</div><div>👥 {e.friends_attending} friends attending</div><ReminderSettings eventId={e.id} initial={e.reminder} /></div>)}</div>;
}
