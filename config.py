from dotenv import load_dotenv
import os

load_dotenv()

MATCH_URL = "https://odibets.com/odileague"
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
EMAIL = os.getenv("EMAIL")
EMAIL_PASS = os.getenv("EMAIL_PASS")
ALERT_TO = os.getenv("ALERT_TO")