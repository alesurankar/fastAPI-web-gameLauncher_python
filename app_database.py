# python app_database.py

import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('example.db')

# Create a table
conn.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data
conn.execute("INSERT INTO users (name, age) VALUES ('John Doe', 30)")

# Commit changes
conn.commit()

# Retrieve data
cursor = conn.execute("SELECT * FROM users")
for row in cursor:
    print(row)

# Close the connection
conn.close()