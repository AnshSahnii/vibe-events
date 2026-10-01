import { Link } from "react-router-dom";
export default function Navbar() {
  return <nav><b>🎉 Vibe Events</b><Link to="/">Home</Link><Link to="/calendar">Calendar</Link><Link to="/dashboard">My Events</Link></nav>;
}
