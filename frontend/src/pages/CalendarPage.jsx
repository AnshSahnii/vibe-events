import { useEffect, useState } from "react"; import { api } from "../api"; import Calendar from "../components/Calendar";
export default function CalendarPage() {
  const [events, setEvents] = useState([]);
  useEffect(() => { api.get("/events", { params: { city: "Chicago" } }).then(r => setEvents(r.data)).catch(() => {}); }, []);
  return <div className="wrap"><h2>Calendar</h2><Calendar events={events} /></div>;
}
