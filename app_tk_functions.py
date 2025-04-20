# python tk_functions.py

import tkinter as tk
import requests


FASTAPI_URL = "http://127.0.0.1:8000"

def create_input_field(parent, label_text, button_text, callback=None):
    label = tk.Label(parent, text=label_text)
    label.pack(pady=5)

    entry = tk.Entry(parent)
    entry.pack(pady=5)

    def on_submit():
        value = entry.get()
        if callback:
            callback(value)

    submit_button = tk.Button(parent, text=button_text, command=on_submit)
    submit_button.pack(pady=10)

    return entry


def handle_login(username, controller):
    print("Username submitted:", username)
    controller.show_frame("ProfilePage")

def handle_registration(username, controller):
    print("Registering username:", username)
    controller.show_frame("ProfilePage")

def handle_logout(controller):
    print("Successfully logged out")
    controller.show_frame("HomePage")

def fetch_users():
    try:
        # Send a GET request to FastAPI server to get the list of users
        response = requests.get(f"{FASTAPI_URL}/list-users")
        # Extract the 'tables' list from the response JSON
        tables = response.json().get("tables", [])
    except Exception:
        # If there's an error, set tables to an empty list
        tables = []
    return tables
