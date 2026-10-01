# 🎟️ Vibe Events

Vibe Events is a full-stack event discovery and tracking platform that helps users discover local events, search using natural language, save events, track RSVPs, interact with friends, and manage their event calendar.

The application combines a **React frontend**, **FastAPI backend**, **MongoDB Atlas**, **Ticketmaster Discovery API**, and **WebSockets** to provide a real-time event experience.

---

## 🚀 Features

### 🔎 Event Discovery
- Search for events by:
  - City
  - Keyword
  - Category
- Fetches real-world event data using the Ticketmaster Discovery API.
- Displays event details such as:
  - Event name
  - Date and time
  - Venue
  - Location
  - Event category
  - Event image
  - Ticket information

### 💬 Conversational Event Search
Users can interact with the application through a chat-style interface to discover events.

Example:

> "Find music events in Pune this weekend"

The backend processes the request and retrieves relevant events.

### ❤️ Interested Events
Users can mark events as **Interested**.

Interested events are persisted in MongoDB and can be viewed later from the **My Events** section.

### 📅 Event Calendar
A calendar interface allows users to:

- View upcoming events
- Identify dates containing events
- Select dates to view events
- Track their event schedule

### 👥 Friend RSVPs
Users can interact with friends around events.

Features include:

- RSVP to events
- View friend RSVP information
- Display live friend counts
- Share events with friends

### 🔗 Event Sharing
Events can be shared with other users through the application's sharing/invite functionality.

### ⚡ Real-Time Updates
The application uses **WebSockets** for real-time communication.

This allows features such as:

- Live RSVP updates
- Friend count updates
- Real-time chat communication
- Event interaction updates

### 🔔 Event Reminders
The application supports event reminder functionality so users can keep track of upcoming events.

### 💾 Persistent Data
User interactions and application data are stored in **MongoDB Atlas**, allowing data to persist across sessions.

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │      User           │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   React + Vite      │
                    │     Frontend        │
                    │                     │
                    │ • Event Discovery   │
                    │ • Calendar          │
                    │ • Chat              │
                    │ • My Events         │
                    │ • RSVP              │
                    └──────────┬──────────┘
                               │
                         HTTP / WebSocket
                               │
                               ▼
                    ┌─────────────────────┐
                    │      FastAPI        │
                    │       Backend       │
                    │                     │
                    │ • REST APIs         │
                    │ • Event Search      │
                    │ • Chat Logic        │
                    │ • RSVP Logic        │
                    │ • WebSockets        │
                    └───────┬───────┬─────┘
                            │       │
                 ┌──────────┘       └──────────────┐
                 ▼                                 ▼
       ┌───────────────────┐             ┌───────────────────┐
       │   MongoDB Atlas   │             │ Ticketmaster API  │
       │                   │             │                   │
       │ • Events          │             │ • Event Search    │
       │ • Users           │             │ • Event Data      │
       │ • RSVPs           │             │ • Venues          │
       │ • Interests       │             │ • Ticket Links    │
       └───────────────────┘             └───────────────────┘
