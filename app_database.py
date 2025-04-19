# python app_database.py

import sqlite3
import re



# --- Utility Functions ---
def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    return conn

def validate_table_name(table_name):
    if not re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', table_name):
        raise ValueError("Invalid table name.")



# --- Table Management ---
def create_table(table_name):
    validate_table_name(table_name)
    conn = get_db_connection()
    conn.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def delete_table(table_name):
    validate_table_name(table_name)
    conn = get_db_connection()
    conn.execute(f"DROP TABLE IF EXISTS {table_name}")
    conn.commit()
    conn.close()

def check_table_exists(table_name):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
        (table_name,)
    )
    exists = cursor.fetchone() is not None
    conn.close()
    return exists



# --- Data Manipulation ---
def insert_data(table_name, name, age):
    validate_table_name(table_name)
    conn = get_db_connection()
    conn.execute(f"INSERT INTO {table_name} (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

def retrieve_data(table_name):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_user_by_id(table_name, user_id):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(f"SELECT * FROM {table_name} WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def find_users_by_name(table_name, name):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(f"SELECT * FROM {table_name} WHERE name = ?", (name,))
    users = cursor.fetchall()
    conn.close()
    return users

def update_user(table_name, user_id, name=None, age=None):
    validate_table_name(table_name)
    conn = get_db_connection()
    if name is not None and age is not None:
        conn.execute(f"UPDATE {table_name} SET name = ?, age = ? WHERE id = ?", (name, age, user_id))
    elif name is not None:
        conn.execute(f"UPDATE {table_name} SET name = ? WHERE id = ?", (name, user_id))
    elif age is not None:
        conn.execute(f"UPDATE {table_name} SET age = ? WHERE id = ?", (age, user_id))
    conn.commit()
    conn.close()

def delete_user(table_name, user_id):
    validate_table_name(table_name)
    conn = get_db_connection()
    conn.execute(f"DELETE FROM {table_name} WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()

def count_users(table_name):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchone()[0]
    conn.close()
    return count