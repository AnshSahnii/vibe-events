import { useEffect, useState } from "react";
import { api, API, USER_ID } from "../api";
import EventCard from "./EventCard";
export default function EventGrid({ events }) {
  const [going, setGoing] = useState(new Set()); const [counts, setCounts] = useState({});
  useEffect(() => { api.get(`/users/${USER_ID}/rsvps`).then(r => setGoing(new Set(r.data.map(e => e.id)))); }, []);
  useEffect(() => {
    const ws = new WebSocket(API.replace("http", "ws") + "/ws/events");
    ws.onmessage = m => { const d = JSON.parse(m.data); if (d.type === "friends_count_update") setCounts(c => ({ ...c, [d.event_id]: d.friends_attending })); };
    return () => ws.close();
  }, []);
  return <div className="grid">{events.map(e => <EventCard key={e.id} event={e} going={going.has(e.id)} friends={counts[e.id]} onRsvp={id => setGoing(s => new Set(s).add(id))} />)}</div>;
}
