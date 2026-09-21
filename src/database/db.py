from src.database.config import supabase
import bcrypt

def check_teacher_exists(username):
    response=supabase.table("teacher").select("username").eq("username",username).execute()
    return len(response.data)>0

def create_teacher(username,password,name):
    data={"username":username, "password": hash_pass(password), "name":name}
    response=supabase.table("teacher").insert(data).execute()
    return response.data
