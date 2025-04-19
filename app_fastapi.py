# uvicorn app_fastapi:app --reload

from fastapi import FastAPI
from typing import List, Dict
import sqlite3

app = FastAPI()

# Connect to SQLite database and retrieve user data
def get_users_from_db() -> List[Dict]:
    conn = sqlite3.connect('example.db')
    cursor = conn.execute("SELECT * FROM users")
    
    users = []
    for row in cursor:
        users.append({"id": row[0], "name": row[1], "age": row[2]})
    
    conn.close()
    return users

@app.get("/users", response_model=List[dict])
def get_users():
    # Call the function to fetch users from the database
    users = get_users_from_db()
    return users