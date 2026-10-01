import { useEffect, useState } from "react"; import { api } from "../api";
import EventGrid from "../components/EventGrid"; import ChatBox from "../components/ChatBox";
const CATS = ["", "music", "comedy", "sports", "theatre"];
export default function Home() {
  const [events, setEvents] = useState([]); const [city, setCity] = useState("Pune"); const [kw, setKw] = useState(""); const [err, setErr] = useState("");
  const load = (k = kw) => api.get("/events", { params: { city, keyword: k || undefined } }).then(r => { setEvents(r.data); setErr(""); }).catch(() => setErr("Could not load events (check API key/backend)."));
  useEffect(() => { load(); }, []);
  return <div className="wrap"><div className="bar">
    <input value={city} onChange={e => setCity(e.target.value)} placeholder="City" /><input value={kw} onChange={e => setKw(e.target.value)} placeholder="Keyword" />
    <button onClick={() => load()}>Search</button>
    {CATS.map(c => <button key={c} className={"chip" + (kw === c ? " sel" : "")} onClick={() => { setKw(c); load(c); }}>{c || "all"}</button>)}</div>
    {err && <p>{err}</p>}<EventGrid events={events} /><ChatBox onResults={setEvents} /></div>;
}
