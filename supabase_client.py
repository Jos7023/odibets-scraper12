import os
from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def upload_match_data(data):
    supabase.table("matches").insert(data).execute()

def upload_results_data(data):
    supabase.table("results").insert(data).execute()

def upload_standings_data(data):
    supabase.table("standings").insert(data).execute()