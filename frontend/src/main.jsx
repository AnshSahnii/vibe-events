import React from "react"; import { createRoot } from "react-dom/client";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import "react-calendar/dist/Calendar.css"; import "./styles.css";
import Navbar from "./components/Navbar"; import Home from "./pages/Home";
import CalendarPage from "./pages/CalendarPage"; import Dashboard from "./pages/Dashboard"; import InvitePage from "./pages/InvitePage";
createRoot(document.getElementById("root")).render(
  <BrowserRouter><Navbar /><Routes>
    <Route path="/" element={<Home />} /><Route path="/calendar" element={<CalendarPage />} />
    <Route path="/dashboard" element={<Dashboard />} /><Route path="/invite/:token" element={<InvitePage />} />
  </Routes></BrowserRouter>);
