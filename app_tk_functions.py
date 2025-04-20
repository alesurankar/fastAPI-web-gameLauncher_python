# python tk_functions.py

import tkinter as tk
import requests
from tkinter import messagebox


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
    try:
        response = requests.get(f"{FASTAPI_URL}/check-users/{username}")
        response.raise_for_status()
        exists = response.json().get("exists", False)

        if exists:
            controller.username = username
            controller.show_frame("ProfilePage")
        else:
            messagebox.showerror("Login Failed", "User does not exist.")
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Could not reach server:\n{e}")


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
        tables = []
    return tables

def update_data(parent_frame):
    # Clear existing user labels before adding new ones
    for widget in parent_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    users = fetch_users()

    for user in users:
        user_label = tk.Label(parent_frame, text=user, font=("Arial", 12))
        user_label.pack(pady=2)

def login(self):
        username = self.username_entry.get()

        try:
            response = requests.get(f"{FASTAPI_URL}/check-users/{username}")
            response.raise_for_status()
            exists = response.json().get("exists", False)

            if exists:
                self.controller.username = username  # Save to controller if you want to reuse
                self.controller.show_frame("ProfilePage")
            else:
                messagebox.showerror("Login Failed", "User does not exist.")
        except requests.RequestException as e:
            messagebox.showerror("Error", f"Could not reach server:\n{e}")