# python tk_functions.py

# app_tk_functions.py

import requests
import tkinter as tk
from tkinter import messagebox

FASTAPI_URL = "http://127.0.0.1:8000"

# Function to create a user (via FastAPI)
def create_user(username, label):
    try:
        r = requests.post(f"{FASTAPI_URL}/create-user/{username}")
        if r.status_code == 200:
            label.config(text=f"User {username} created.")
        else:
            label.config(text=f"Error: {r.json()}")
    except Exception as e:
        label.config(text=f"Error: {str(e)}")

# Function to check if a user exists (via FastAPI)
def check_user_exists(username, label):
    try:
        check_url = f"{FASTAPI_URL}/check-users/{username}"
        response = requests.get(check_url)
        response.raise_for_status()
        exists = response.json().get("exists", False)
        if exists:
            return True
        else:
            label.config(text="User does not exist.")
            return False
    except requests.exceptions.RequestException as e:
        label.config(text=f"Error checking user: {e}")
        return False

# Function to list all users (via FastAPI)
def list_users(label):
    try:
        response = requests.get(f"{FASTAPI_URL}/list-users")
        response.raise_for_status()  # Raise exception if the response code is not 200
        users = response.json().get("users", [])  # Ensure that you get the "users" list
        return users
    except Exception as e:
        label.config(text=f"Error fetching users: {str(e)}")
        return []  # Return an empty list on error

# Function to add a character (via FastAPI)
def add_character(username, name, level, label):
    try:
        r = requests.post(f"{FASTAPI_URL}/add-character/{username}", json={"name": name, "level": level})
        if r.status_code == 200:
            label.config(text="Character added successfully!")
        else:
            label.config(text=f"Failed to add character: {r.json().get('detail', 'Unknown error')}")
    except Exception as e:
        label.config(text=f"Error adding character: {str(e)}")

# Function to list characters (via FastAPI)
def list_characters(username, label):
    try:
        r = requests.get(f"{FASTAPI_URL}/list-character/{username}")
        return r.json()
    except Exception as e:
        label.config(text=f"Error fetching characters: {str(e)}")
        return []

# Function to open the profile window
def open_profile_window(root):
    profile_window = tk.Toplevel(root)
    profile_window.title("Profile")
    profile_window.geometry("800x600")
    
    username = "User"  # Fetch from session or FastAPI
    characters = list_characters(username, profile_window)  # Fetch characters from FastAPI or your logic
    
    label = tk.Label(profile_window, text=f"Welcome, {username}", font=("Arial", 16))
    label.pack(pady=10)

    char_listbox = tk.Listbox(profile_window, width=40, height=10, font=("Arial", 12))
    char_listbox.pack(pady=10)

    for char in characters:
        char_listbox.insert(tk.END, f"{char['name']} (Level {char['level']})")
    
    # Character add form
    name_label = tk.Label(profile_window, text="Character Name", font=("Arial", 12))
    name_label.pack(pady=5)
    name_entry = tk.Entry(profile_window)
    name_entry.pack(pady=5)

    level_label = tk.Label(profile_window, text="Character Level", font=("Arial", 12))
    level_label.pack(pady=5)
    level_entry = tk.Entry(profile_window)
    level_entry.pack(pady=5)

    def add_character_to_profile():
        name = name_entry.get()
        level = level_entry.get()
        add_character(username, name, level, profile_window)
        profile_window.destroy()  # Close the window after adding

    add_button = tk.Button(profile_window, text="Add Character", command=add_character_to_profile)
    add_button.pack(pady=10)

# Function to open the login window
def open_login_window(root):
    login_window = tk.Toplevel(root)
    login_window.title("Login")
    login_window.geometry("800x600")
    
    login_label = tk.Label(login_window, text="Username:", font=("Arial", 14))
    login_label.pack(pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.pack(pady=5)

    def login():
        username = username_entry.get()
        if check_user_exists(username, login_window):
            messagebox.showinfo("Login", f"Logged in as {username}")
            login_window.destroy()
        else:
            messagebox.showerror("Login", "User does not exist.")

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=10)

# Function to open the register window
def open_register_window(root):
    register_window = tk.Toplevel(root)
    register_window.title("Register")
    register_window.geometry("800x600")
    
    register_label = tk.Label(register_window, text="Username:", font=("Arial", 14))
    register_label.pack(pady=10)
    username_entry = tk.Entry(register_window)
    username_entry.pack(pady=5)

    def register():
        username = username_entry.get()
        if username:
            create_user(username, register_window)
            messagebox.showinfo("Register", f"User {username} created successfully!")
            register_window.destroy()
        else:
            messagebox.showerror("Register", "Username cannot be empty.")

    register_button = tk.Button(register_window, text="Register", command=register)
    register_button.pack(pady=10)

# Function to update the registered users list
def update_user_list(users_listbox, label):
    users = list_users(label)  # Fetch the list of users
    users_listbox.delete(0, tk.END)  # Clear the current entries in the listbox
       
    # Insert the users into the listbox
    for user in users:
        users_listbox.insert(tk.END, user)  # Add each user to the listbox

# Function to log out a user
def logout(label):
    label.config(text="Logged out successfully.")
