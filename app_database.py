# python app_database.py

import sqlite3
import re



# --- Utility Functions ---
def get_db_connection():
    conn = sqlite3.connect('data.db')
    conn.row_factory = sqlite3.Row
    conn.isolation_level = None  # Enable autocommit mode
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
            level INTEGER,
            x INTEGER DEFAULT 10,
            y INTEGER DEFAULT 10
        )
    ''')

    cursor = conn.execute(f"SELECT COUNT(*) as count FROM {table_name}")
    count = cursor.fetchone()["count"]
    if count == 0:
        conn.execute(f"INSERT INTO {table_name} (name, level) VALUES (?, ?)", ("DefaultName", 1))
        
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

def list_tables():
    conn = get_db_connection()
    cursor = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'"
    )
    tables = [row["name"] for row in cursor.fetchall()]
    conn.close()
    return tables



# --- Position management --- 
def update_position(table_name, x, y):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(f"SELECT COUNT(*) FROM {table_name} WHERE id = 1")
    exists = cursor.fetchone()[0]
    if exists:
        conn.execute(f"UPDATE {table_name} SET x = ?, y = ? WHERE id = 1", (x, y))
    else:
        conn.execute(f"INSERT INTO {table_name} (id, name, level, x, y) VALUES (1, ?, ?, ?, ?)",
                     (table_name, 1, x, y))
    conn.commit()
    conn.close()

def get_position(table_name):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(f'''
        SELECT x, y FROM {table_name} WHERE id = 1
    ''')
    row = cursor.fetchone()
    conn.close()
    return {"x": row["x"], "y": row["y"]} if row else {"x": 0.0, "y": 0.0}




# --- Data Manipulation ---
def insert_data(table_name, name, level):
    validate_table_name(table_name)
    conn = get_db_connection()
    conn.execute(f"INSERT INTO {table_name} (name, level) VALUES (?, ?)", (name, level))
    conn.commit()
    conn.close()

def retrieve_data(table_name):
    validate_table_name(table_name)
    conn = get_db_connection()
    cursor = conn.execute(f"SELECT name, level FROM {table_name}") 
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

def update_user(table_name, user_id, name=None, level=None):
    validate_table_name(table_name)
    conn = get_db_connection()
    if name is not None and level is not None:
        conn.execute(f"UPDATE {table_name} SET name = ?, level = ? WHERE id = ?", (name, level, user_id))
    elif name is not None:
        conn.execute(f"UPDATE {table_name} SET name = ? WHERE id = ?", (name, user_id))
    elif level is not None:
        conn.execute(f"UPDATE {table_name} SET level = ? WHERE id = ?", (level, user_id))
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