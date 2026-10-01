import os
from dotenv import load_dotenv
load_dotenv()
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DB_NAME = os.getenv("DB_NAME", "vibe_events")
TICKETMASTER_API_KEY = os.getenv("TICKETMASTER_API_KEY", "")
FRONTEND_URL = os.getenv("FRONTEND_URL", "http://localhost:5173")
