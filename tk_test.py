# python tk_test.py

import tkinter as tk
from tkinter import ttk, messagebox

# Define your API options and descriptions
api_options = {
    "POST /create-user/{table_name}": "Api Create Table",
    "DELETE /delete-user/{table_name}": "Api Delete Table",
    "GET /check-users/{table_name}": "Api Check Table",
    "POST /add-character/{table_name}": "Api Add User",
    "GET /list-character/{table_name}": "Api List Users",
    "GET /show-character/{table_name}/{user_id}": "Api Get User By Id",
    "GET /search-character/{table_name}": "Api Find User By Name",
    "PUT /change-character/{table_name}/{user_id}": "Api Update User",
    "DELETE /delete-character/{table_name}/{user_id}": "Api Delete User",
    "GET /count/{table_name}": "Api Count Users"
}

# Main Tkinter Window
root = tk.Tk()
root.title("API Option Selector")
root.geometry("500x300")

# Label
label = tk.Label(root, text="Select API Action:", font=("Arial", 14))
label.pack(pady=10)

# Combobox with API options
combo = ttk.Combobox(root, values=list(api_options.keys()), width=60)
combo.pack(pady=5)

# Function to handle selection
def open_api_window():
    selected = combo.get()
    if not selected:
        messagebox.showwarning("Warning", "Please select an API action.")
        return

    # Create a new window
    win = tk.Toplevel(root)
    win.title(f"{selected}")
    win.geometry("400x300")

    # Description
    description = api_options[selected]
    tk.Label(win, text=f"Action: {description}", font=("Arial", 12, "bold")).pack(pady=10)

    # Based on the selected API, show relevant inputs
    if "{table_name}" in selected:
        tk.Label(win, text="Table Name:").pack()
        table_entry = tk.Entry(win)
        table_entry.pack()

    if "{user_id}" in selected:
        tk.Label(win, text="User ID:").pack()
        user_id_entry = tk.Entry(win)
        user_id_entry.pack()

    if "add-character" in selected or "change-character" in selected:
        tk.Label(win, text="Character Name:").pack()
        name_entry = tk.Entry(win)
        name_entry.pack()

        tk.Label(win, text="Level:").pack()
        level_entry = tk.Entry(win)
        level_entry.pack()

    # Submit button (just for demo)
    def submit():
        messagebox.showinfo("Submitted", f"You chose:\n{selected}")

    tk.Button(win, text="Submit", command=submit).pack(pady=20)

# Button to confirm selection
tk.Button(root, text="Open API Window", command=open_api_window).pack(pady=20)

root.mainloop()