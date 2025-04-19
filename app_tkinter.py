# python app_tkinter.py

import tkinter as tk
import requests

# Function to fetch user data from FastAPI
def get_users_from_fastapi():
    try:
        response = requests.get("http://127.0.0.1:8000/users")
        if response.status_code == 200:
            return response.json()
        else:
            return []
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

# Function to update the Tkinter window with user data
def display_users():
    users = get_users_from_fastapi()
    
    # Create a label for each user in the list
    for user in users:
        user_info = f"{user['name']} - Age: {user['age']}"
        label = tk.Label(root, text=user_info)
        label.pack()

# Create the main Tkinter window
root = tk.Tk()

# Create a label for the title
title_label = tk.Label(root, text="User List")
title_label.pack()

# Create a button to fetch and display users
fetch_button = tk.Button(root, text="Fetch Users", command=display_users)
fetch_button.pack()

# Start the Tkinter event loop
root.mainloop()