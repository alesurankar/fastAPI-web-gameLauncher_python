# python app_database.py

import sqlite3

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('example.db')
    conn.row_factory = sqlite3.Row  # To allow access by column name
    return conn

# Function to create a table if it doesn't exist
def create_table():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER)''')
    conn.commit()
    conn.close()

# Function to insert data into the table
def insert_data(name, age):
    conn = get_db_connection()
    conn.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    conn.close()

# Function to retrieve data from the database
def retrieve_data():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()
    return users

# Function to delete the users table
def delete_table():
    conn = get_db_connection()
    conn.execute("DROP TABLE IF EXISTS users")
    conn.commit()
    conn.close()

# Function to check if the table exists
def check_table_exists():
    conn = get_db_connection()
    cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users'")
    table_exists = cursor.fetchone() is not None
    conn.close()
    return table_exists