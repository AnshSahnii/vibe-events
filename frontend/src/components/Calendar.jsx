import { useState } from "react"; import ReactCalendar from "react-calendar";
import EventGrid from "./EventGrid";
const iso = d => `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;
export default function Calendar({ events }) {
  const [sel, setSel] = useState(new Date()); const dates = new Set(events.map(e => e.date));
  return <><ReactCalendar value={sel} onChange={setSel} tileClassName={({ date, view }) => view === "month" && dates.has(iso(date)) ? "has-event" : null} />
    <h3>Events on {iso(sel)}</h3><EventGrid events={events.filter(e => e.date === iso(sel))} /></>;
}
