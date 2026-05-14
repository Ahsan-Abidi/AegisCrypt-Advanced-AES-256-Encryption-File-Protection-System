import tkinter as tk
from tkinter import messagebox

from core.auth import login_user, register_user
from core.password_checker import check_password_strength
from core.session_manager import create_session
from gui.dashboard import open_dashboard

def launch_login():

    root = tk.Tk()

    root.title("AegisCrypt")
    root.geometry("500x450")
    root.configure(bg="#111111")

    tk.Label(
        root,
        text="AegisCrypt",
        font=("Arial", 22, "bold"),
        fg="cyan",
        bg="#111111"
    ).pack(pady=20)

    username_entry = tk.Entry(root, width=30)
    username_entry.pack(pady=10)

    password_entry = tk.Entry(root, width=30, show="*")
    password_entry.pack(pady=10)

    strength_label = tk.Label(
        root,
        text="Password Strength",
        fg="white",
        bg="#111111"
    )

    strength_label.pack()

    def analyze_password(event):

        strength = check_password_strength(
            password_entry.get()
        )

        strength_label.config(
            text=f"Strength: {strength}"
        )

    password_entry.bind("<KeyRelease>", analyze_password)

    def login():

        username = username_entry.get()
        password = password_entry.get()

        if login_user(username, password):

            create_session(username)

            messagebox.showinfo(
                "Success",
                "Login Successful"
            )

            root.destroy()

            open_dashboard(username)

        else:
            messagebox.showerror(
                "Error",
                "Invalid Credentials"
            )

    def register():

        username = username_entry.get()
        password = password_entry.get()

        if register_user(username, password):

            messagebox.showinfo(
                "Success",
                "Registration Successful"
            )

        else:
            messagebox.showerror(
                "Error",
                "User Already Exists"
            )

    tk.Button(
        root,
        text="Login",
        command=login,
        bg="cyan",
        width=20
    ).pack(pady=10)

    tk.Button(
        root,
        text="Register",
        command=register,
        bg="orange",
        width=20
    ).pack(pady=10)

    root.mainloop()