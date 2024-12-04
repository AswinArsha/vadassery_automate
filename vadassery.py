from supabase import create_client, Client

# Supabase URL and Key
supabase_url = 'https://aobcelfbawxxsalayguh.supabase.co'
supabase_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImFvYmNlbGZiYXd4eHNhbGF5Z3VoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjQwNDEwMDQsImV4cCI6MjAzOTYxNzAwNH0.9Y6PK59s7-2WXh1k4BMueB4j6yeKyVLL6K4IZk0tri4'
``
# Initialize Supabase Client
supabase: Client = create_client(supabase_url, supabase_key)

# Insert a letter 'a' into the 'test' table
def insert_letter():
    data = {"letter": "a"}
    response = supabase.table("test").insert(data).execute()

    if 'error' in response and response['error']:
        print(f"Error inserting letter: {response['error']}")
    else:
        print("Successfully inserted letter 'a' into the test table.")

if __name__ == "__main__":
    insert_letter()
