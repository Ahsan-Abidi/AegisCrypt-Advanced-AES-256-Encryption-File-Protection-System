import tkinter as tk

def create_title(parent, text):

    title = tk.Label(
        parent,
        text=text,
        font=("Arial", 22, "bold"),
        fg="cyan",
        bg="#0d1117"
    )

    return title

def create_button(
    parent,
    text,
    command,
    color="#1f6feb"
):

    button = tk.Button(
        parent,
        text=text,
        command=command,
        width=25,
        height=2,
        bg=color,
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    )

    return button

def create_entry(
    parent,
    hidden=False
):

    entry = tk.Entry(
        parent,
        width=40,
        font=("Arial", 12),
        show="*" if hidden else ""
    )

    return entry

def create_label(
    parent,
    text
):

    label = tk.Label(
        parent,
        text=text,
        fg="white",
        bg="#0d1117",
        font=("Arial", 11)
    )

    return label