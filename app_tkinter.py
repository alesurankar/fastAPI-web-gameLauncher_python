# python app_tkinter.py

import tkinter as tk
from app_database import create_table, insert_data, retrieve_data, delete_table

# Create the main window
root = tk.Tk()

# Function to create the table
def create():
    create_table()

# Function to insert data into the table
def insert():
    name = name_entry.get()
    age = age_entry.get()
    insert_data(name, age)

# Function to display data from the table
def display():
    users = retrieve_data()
    display_text = "\n".join([f"{user['name']} - Age: {user['age']}" for user in users])
    label.config(text=display_text)

# Create widgets
label = tk.Label(root, text="Welcome to Tkinter!")
label.pack()

create_button = tk.Button(root, text="Create Table", command=create)
create_button.pack()

insert_button = tk.Button(root, text="Insert Data", command=insert)
insert_button.pack()

delete_button = tk.Button(root, text="Delete Table", command=delete_table)
delete_button.pack()

name_entry = tk.Entry(root)
name_entry.pack()

age_entry = tk.Entry(root)
age_entry.pack()

display_button = tk.Button(root, text="Display Data", command=display)
display_button.pack()

# Start the Tkinter event loop
root.mainloop()