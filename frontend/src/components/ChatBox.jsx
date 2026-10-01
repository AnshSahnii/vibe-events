import { useState } from "react"; import { api } from "../api";
export default function ChatBox({ onResults }) {
  const [text, setText] = useState(""); const [log, setLog] = useState([]);
  const send = async () => {
    if (!text.trim()) return; const m = text; setText("");
    const r = await api.post("/chat", { message: m }); setLog(l => [...l, "🧑 " + m, "🤖 " + r.data.message]); onResults(r.data.events);
  };
  return <div className="chat"><h3>💬 Ask for events</h3>{log.map((l, i) => <div className="msg" key={i}>{l}</div>)}
    <input value={text} onChange={e => setText(e.target.value)} onKeyDown={e => e.key === "Enter" && send()} placeholder="Find music events in Pune" style={{ width: "70%" }} /> <button onClick={send}>Send</button></div>;
}
