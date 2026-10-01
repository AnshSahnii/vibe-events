import { useState } from "react"; import { api, USER_ID } from "../api";
export default function ReminderSettings({ eventId, initial }) {
  const [on, setOn] = useState(initial?.enabled ?? false); const [h, setH] = useState(initial?.hours_before ?? 24);
  const save = (en, hr) => api.put("/reminders", { user_id: USER_ID, event_id: eventId, enabled: en, hours_before: hr });
  return <div><label><input type="checkbox" checked={on} onChange={e => { setOn(e.target.checked); save(e.target.checked, h); }} /> Enable reminders</label>{" "}
    <select value={h} onChange={e => { setH(+e.target.value); save(on, +e.target.value); }}>{[1, 6, 24, 48].map(x => <option key={x} value={x}>{x} hours before</option>)}</select></div>;
}
