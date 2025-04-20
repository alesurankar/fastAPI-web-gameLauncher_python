# python tk_interface.py

import tkinter as tk
from tkinter import messagebox
import app_tk_functions

root = tk.Tk()
root.title("NinjaStrike")
root.geometry("800x600")

# Create a header frame
header = tk.Frame(root)
header.pack(fill=tk.X)

# Title Label in header
header_label = tk.Label(header, text="NinjaStrike", font=("Arial", 24, "bold"))
header_label.pack(side=tk.LEFT, padx=10)

# Navigation
nav_frame = tk.Frame(header)
nav_frame.pack(side=tk.RIGHT, padx=10)

profile_button = tk.Button(nav_frame, text="Profile", command=lambda: app_tk_functions.open_profile_window(root))
profile_button.pack(side=tk.LEFT, padx=5)

login_button = tk.Button(nav_frame, text="Login", command=lambda: app_tk_functions.open_login_window(root))
login_button.pack(side=tk.LEFT, padx=5)

register_button = tk.Button(nav_frame, text="Register", command=lambda: app_tk_functions.open_register_window(root))
register_button.pack(side=tk.LEFT, padx=5)

# Main content area
main_frame = tk.Frame(root)
main_frame.pack(padx=20, pady=20)

# Status Section
status_label = tk.Label(main_frame, text="Status", font=("Arial", 18))
status_label.pack(pady=10)

status_text = tk.Label(main_frame, text="Not logged in.", font=("Arial", 14))
status_text.pack(pady=5)

# Registered Users Section
users_label = tk.Label(main_frame, text="Registered Users:", font=("Arial", 16))
users_label.pack(pady=10)

# List of users
users_listbox = tk.Listbox(main_frame, width=40, height=10, font=("Arial", 12))
users_listbox.pack()

# Footer Section
footer = tk.Frame(root)
footer.pack(side=tk.BOTTOM, fill=tk.X)

footer_label = tk.Label(footer, text="© 2024 NinjaStrike Application", font=("Arial", 10))
footer_label.pack()

# Call to initially load users list
app_tk_functions.update_user_list(users_listbox, status_text)

# Start the Tkinter event loop
root.mainloop()
