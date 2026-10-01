import axios from "axios";
export const API = "http://localhost:8000";
export const USER_ID = 1;
export const api = axios.create({ baseURL: API + "/api" });
export const fmtTime = (t) => { if (!t) return "TBA"; const [h, m] = t.split(":"); const H = +h; return `${H % 12 || 12}:${m} ${H >= 12 ? "PM" : "AM"}`; };
export const fmtDate = (d) => d ? new Date(d + "T00:00").toLocaleDateString("en-US", { month: "short", day: "numeric" }) : "TBA";
