# python tk_functions.py


FASTAPI_URL = "http://127.0.0.1:8000"


import tkinter as tk

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
