# python app_tkinter.py

import tkinter as tk
import app_tk_functions


class NinjaStrikeApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NinjaStrike")
        self.geometry("800x600")

        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}

        for PageClass in (HomePage, LoginPage, RegisterPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

        # Call a custom method when the frame is shown
        if hasattr(frame, "on_show"):
            frame.on_show()
    

# ---------------- Pages ---------------- #

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="NinjaStrike", font=("Arial", 24))
        label.pack(pady=20)

        # Initial message
        self.message_label = tk.Label(self, text="Not logged in.", font=("Arial", 12))
        self.message_label.pack(side="top", pady=5)

        nav = tk.Frame(self)
        nav.pack(pady=10)

        tk.Button(nav, text="Login", command=lambda: controller.show_frame("LoginPage")).pack(side="left", padx=5)
        tk.Button(nav, text="Register", command=lambda: controller.show_frame("RegisterPage")).pack(side="left", padx=5)
        tk.Button(nav, text="Launch the Game", command=lambda: app_tk_functions.profile_call(controller)).pack(side="left", padx=5)

        self.data_content = tk.Frame(self)
        self.data_content.pack(pady=10)

    def on_refresh(self):
        if hasattr(self.controller, 'username') and self.controller.username:
            message = f"Logged in as {self.controller.username}."
        else:
            message = "Not logged in."

        # Update the message label with the correct text
        self.message_label.config(text=message)

        # Remove and add the "Logout" button based on login status
        for widget in self.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") == "Logout":
                widget.pack_forget()  # Remove the "Logout" button

        # Add the "Logout" button if the user is logged in
        if hasattr(self.controller, 'username') and self.controller.username:
            tk.Button(self, text="Logout", command=lambda: app_tk_functions.handle_logout(self.controller)).pack(side="left", padx=5)

            # Placeholder for the list of characters
            self.character_list_label = tk.Label(self, text="Character List:", font=("Arial", 14))
            self.character_list_label.pack(pady=10)
            self.character_list_frame = tk.Frame(self)
            self.character_list_frame.pack(pady=10)

            # Call the utility function to fetch and display the character list
            app_tk_functions.refresh_character_list(self)  # Passing self to update the HomePage UI
            

    def on_show(self):
        self.on_refresh()

    



class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        label = tk.Label(self, text="Login Page", font=("Arial", 24))
        label.pack(pady=20)

        nav = tk.Frame(self)
        nav.pack(pady=10)

        tk.Button(nav, text="Home", command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=5)
        tk.Button(nav, text="Register", command=lambda: controller.show_frame("RegisterPage")).pack(side="left", padx=5)

        # Add login input fields and buttons
        app_tk_functions.create_input_field(self, label_text="Username:", button_text="Login",
                                            callback=lambda username: app_tk_functions.handle_login(username, controller))

        self.data_content = tk.Frame(self)
        self.data_content.pack(pady=10)

    def on_show(self):
        if self.controller.loged_in:  # Check if the user is logged in
            print("User is logged in:", self.controller.username)
        else:
            print("User is not logged in.")


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Register Page", font=("Arial", 24))
        label.pack(pady=20)

        nav = tk.Frame(self)
        nav.pack(pady=10) 

        tk.Button(nav, text="Home", command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=5)
        tk.Button(nav, text="Login", command=lambda: controller.show_frame("LoginPage")).pack(side="left", padx=5)

        app_tk_functions.create_input_field(self,label_text="Username:",button_text="Register",
            callback=lambda username: app_tk_functions.handle_registration(username, controller))

        self.data_content = tk.Frame(self)
        self.data_content.pack(pady=10)

    def on_show(self):
        pass


# -------- Run App -------- #

if __name__ == "__main__":
    app = NinjaStrikeApp()
    app.mainloop()