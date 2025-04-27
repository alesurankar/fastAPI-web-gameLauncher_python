# python tk_functions.py

import tkinter as tk
import requests
from tkinter import messagebox
import os
import subprocess


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
    print("Logging username:", username)
    try:
        response = requests.get(f"{FASTAPI_URL}/check-users/{username}")
        response.raise_for_status()
        exists = response.json().get("exists", False)

        if exists:
            controller.username = username
            controller.loged_in = True  # Store login status in controller
            controller.show_frame("HomePage")
        else:
            messagebox.showerror("Login Failed", "User does not exist.")
            controller.loged_in = False  # Ensure the login status is False
    except requests.RequestException as e:
        messagebox.showerror("Error", f"Could not reach server:\n{e}")
        controller.loged_in = False  # Ensure the login status is False
        


def handle_registration(username, controller):
    if not username or len(username) < 3:
        messagebox.showerror("Registration", "Username must be at least 3 characters.")
        return
    
    print("Registering username:", username)

    try:
        response = requests.get(f"{FASTAPI_URL}/check-users/{username}")
        response.raise_for_status()
        exists = response.json().get("exists", False)

        if exists:
            messagebox.showerror("Registration", "User already exist.")
            return
        else:
            response = requests.post(f"{FASTAPI_URL}/create-user/{username}")
            response.raise_for_status()
            controller.username = username
            
            # If the user was successfully created, show the success message and move to the profile page
            messagebox.showinfo("Registration", "User successfully registered!")
            controller.username = username
            controller.show_frame("ProfilePage")


    except requests.RequestException as e:
        messagebox.showerror("Error", f"Could not reach server:\n{e}")


def profile_call(controller):
    # Check if the controller has a logged-in username
    if hasattr(controller, 'username') and controller.username:
        # If logged in, call the game launch function
        play_game(controller)
    else:
        # If not logged in, show an error
        messagebox.showerror("Login Required", "Please log in first.")


def handle_logout(controller):
    print("Successfully logged out")
    
    # Clear the username or any other login-related data
    if hasattr(controller, 'username'):
        del controller.username  # Remove the username attribute
    
    # Optionally reset any other variables or flags related to the user session here
    
    # Show the HomePage and update the UI to reflect that the user is logged out
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


def update_user_data(parent_frame):
    # Clear existing user labels before adding new ones
    for widget in parent_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()
            

def update_data(parent_frame):
    # Clear existing user labels before adding new ones
    for widget in parent_frame.winfo_children():
        if isinstance(widget, tk.Label):
            widget.destroy()

    users = fetch_users()

    for user in users:
        user_label = tk.Label(parent_frame, text=user, font=("Arial", 12))
        user_label.pack(pady=2)

def play_game(controller, event=None):
    # Ensure the absolute path to the executable is correct
    exe_directory = r'C:\Users\Uporabnik\Desktop\NinjaStrike'  # Update with the new directory
    exe_path = os.path.join(exe_directory, 'MojFramework.exe')  # Make sure the file name is correct

    # Check if the executable exists at the specified path
    if os.path.exists(exe_path):
        # Launch the C++ game client with the correct working directory
        subprocess.Popen([exe_path], cwd=exe_directory)
    else:
        print(f"Error: {exe_path} not found")