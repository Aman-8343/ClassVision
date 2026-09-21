from src.database.config import supabase
import bcrypt

def check_teacher_exists(username):
    response=supabase.table("teacher").select("username").eq("username",username).execute()
    return len(response.data)>0

