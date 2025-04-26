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

        for PageClass in (HomePage, ProfilePage, LoginPage, RegisterPage):
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
        message = "Not logged in."
        self.message_label = tk.Label(self, text=message, font=("Arial", 12))
        self.message_label.pack(side="top", pady=5)

        nav = tk.Frame(self)
        nav.pack(pady=10)

        tk.Button(nav, text="Profile", command=lambda: app_tk_functions.pro(controller)).pack(side="left", padx=5)
        tk.Button(nav, text="Login", command=lambda: controller.show_frame("LoginPage")).pack(side="left", padx=5)
        tk.Button(nav, text="Register", command=lambda: controller.show_frame("RegisterPage")).pack(side="left", padx=5)

        self.data_content = tk.Frame(self)
        self.data_content.pack(pady=10)

    def on_refresh(self):
        # Dynamically update the login status message
        if hasattr(self.controller, 'username') and self.controller.username:
            message = f"Logged in as {self.controller.username}."
        else:
            message = "Not logged in."

        self.message_label.config(text=message)
        self.after(5000, self.on_refresh)  # Continuous refresh

    def on_show(self):
        self.on_refresh()
        app_tk_functions.update_data(self.data_content)


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Profile Page", font=("Arial", 24))
        label.pack(pady=20)

        nav = tk.Frame(self)
        nav.pack(pady=10)

        tk.Button(nav, text="Home", command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=5)
        tk.Button(nav, text="Logout", command=lambda: app_tk_functions.handle_logout(controller)).pack(side="left", padx=5)
        
        self.data_content = tk.Frame(self)
        self.data_content.pack(pady=10)

    def on_show(self):
        pass


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Login Page", font=("Arial", 24))
        label.pack(pady=20)

        nav = tk.Frame(self)
        nav.pack(pady=10) 

        tk.Button(nav, text="Home", command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=5)
        tk.Button(nav, text="Register", command=lambda: controller.show_frame("RegisterPage")).pack(side="left", padx=5)

        app_tk_functions.create_input_field(self,label_text="Username:",button_text="Login",
            callback=lambda username: app_tk_functions.handle_login(username, controller))

        self.data_content = tk.Frame(self)
        self.data_content.pack(pady=10)

    def on_show(self):
        pass


class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        label = tk.Label(self, text="Register Page", font=("Arial", 24))
        label.pack(pady=20)

        nav = tk.Frame(self)
        nav.pack(pady=10) 

        tk.Button(nav, text="Home", command=lambda: controller.show_frame("HomePage")).pack(side="left", padx=5)
        tk.Button(nav, text="Profile", command=lambda: controller.show_frame("ProfilePage")).pack(side="left", padx=5)
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