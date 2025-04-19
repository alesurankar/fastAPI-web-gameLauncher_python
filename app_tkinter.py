# python app_tkinter.py

import tkinter as tk
import requests

# FastAPI URL (ensure this matches your FastAPI server URL)
FASTAPI_URL = "http://127.0.0.1:8000"

# Create the main window
root = tk.Tk()

# Function to create the table (via FastAPI)
def create():
    username = name_entry.get()  # Use the name as the table name (e.g., username)
    r = requests.post(f"{FASTAPI_URL}/create-user/{username}")
    if r.status_code == 200:
        label.config(text=f"Table for {username} created.")
    else:
        label.config(text=f"Error: {r.json()}")

# Function to insert data into the table (via FastAPI)
def insert():
    username = name_entry.get()
    age = age_entry.get()
    data = {"name": username, "age": age}

    # Insert user data via FastAPI
    r = requests.post(f"{FASTAPI_URL}/add-character/{username}", json=data)
    if r.status_code == 200:
        label.config(text=f"User {username} added.")
    else:
        label.config(text=f"Error: {r.json()}")

# Function to display data from the table (via FastAPI)
def display():
    username = name_entry.get()
    
    # Retrieve data via FastAPI
    r = requests.get(f"{FASTAPI_URL}/list-character/{username}")
    if r.status_code == 200:
        users = r.json()
        display_text = "\n".join([f"{user['name']} - Age: {user['age']}" for user in users])
        label.config(text=display_text)
    else:
        label.config(text=f"Error: {r.json()}")

# Function to delete the table (via FastAPI)
def delete():
    username = name_entry.get()
    r = requests.delete(f"{FASTAPI_URL}/delete-user/{username}")
    if r.status_code == 200:
        label.config(text=f"Table for {username} deleted.")
    else:
        label.config(text=f"Error: {r.json()}")

# Create widgets
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

name_label = tk.Label(root, text="Enter Username:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Enter Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

# Buttons for actions
create_button = tk.Button(root, text="Create Table", command=create)
create_button.pack()

insert_button = tk.Button(root, text="Insert Data", command=insert)
insert_button.pack()

display_button = tk.Button(root, text="Display Data", command=display)
display_button.pack()

delete_button = tk.Button(root, text="Delete Table", command=delete)
delete_button.pack()

# Start the Tkinter event loop
root.mainloop()
