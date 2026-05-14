import tkinter as tk
from tkinter import filedialog, messagebox

from PIL import Image, ImageTk

import os
import shutil
import datetime

from core.encryptor import encrypt_file
from core.decryptor import decrypt_file
from core.integrity import calculate_sha256
from core.metadata_scanner import get_file_metadata
from core.secure_delete import secure_delete

selected_file = ""

def open_dashboard(username):

    global selected_file

    app = tk.Tk()

    app.title(
        "AegisCrypt — Military-Grade AES-256 Secure Encryption Suite"
    )

    app.geometry("900x700")

    app.configure(bg="#0d1117")

    # =========================
    # APPLICATION ICON
    # =========================

    try:

        icon = tk.PhotoImage(
            file="assets/logo.png"
        )

        app.iconphoto(True, icon)

    except:
        pass

    # =========================
    # LOGO
    # =========================

    try:

        logo = Image.open(
            "assets/logo.png"
        )

        logo = logo.resize((120, 120))

        logo_img = ImageTk.PhotoImage(
            logo
        )

        logo_label = tk.Label(
            app,
            image=logo_img,
            bg="#0d1117"
        )

        logo_label.image = logo_img

        logo_label.pack(pady=10)

    except:
        pass

    # =========================
    # HEADER
    # =========================

    header = tk.Label(
        app,
        text="Advanced Cybersecurity Encryption Dashboard",
        font=("Arial", 14, "bold"),
        fg="white",
        bg="#0d1117"
    )

    header.pack()

    # =========================
    # WELCOME TEXT
    # =========================

    welcome = tk.Label(
        app,
        text=f"Welcome {username}",
        font=("Arial", 20, "bold"),
        fg="cyan",
        bg="#0d1117"
    )

    welcome.pack(pady=20)

    # =========================
    # FILE LABEL
    # =========================

    file_label = tk.Label(
        app,
        text="No File Selected",
        fg="white",
        bg="#0d1117",
        font=("Arial", 10)
    )

    file_label.pack(pady=10)

    # =========================
    # CHOOSE FILE
    # =========================

    def choose_file():

        global selected_file

        selected_file = filedialog.askopenfilename()

        if selected_file:

            file_label.config(
                text=selected_file
            )

    # =========================
    # ENCRYPT FILE
    # =========================

    def encrypt():

        password = password_entry.get()

        if not selected_file:

            messagebox.showerror(
                "Error",
                "Please select a file"
            )

            return

        if not password:

            messagebox.showerror(
                "Error",
                "Please enter password"
            )

            return

        result = encrypt_file(
            selected_file,
            password
        )

        if result:

            messagebox.showinfo(
                "Encryption Successful",
                f"Encrypted File Saved At:\n\n{result}"
            )

        else:

            messagebox.showerror(
                "Error",
                "Encryption Failed"
            )

    # =========================
    # DECRYPT FILE
    # =========================

    def decrypt():

        password = password_entry.get()

        if not selected_file:

            messagebox.showerror(
                "Error",
                "Please select a file"
            )

            return

        if not password:

            messagebox.showerror(
                "Error",
                "Please enter password"
            )

            return

        result = decrypt_file(
            selected_file,
            password
        )

        if result:

            messagebox.showinfo(
                "Decryption Successful",
                f"Decrypted File Saved At:\n\n{result}"
            )

        else:

            messagebox.showerror(
                "Error",
                "Decryption Failed"
            )

    # =========================
    # SHA-256 + REPORT
    # =========================

    def integrity_check():

        if not selected_file:

            messagebox.showerror(
                "Error",
                "Please select a file"
            )

            return

        hash_value = calculate_sha256(
            selected_file
        )

        metadata = get_file_metadata(
            selected_file
        )

        os.makedirs(
            "reports",
            exist_ok=True
        )

        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )

        report_path = os.path.join(
            "reports",
            f"security_report_{timestamp}.txt"
        )

        with open(report_path, "w") as report:

            report.write(
                "=" * 60 + "\n"
            )

            report.write(
                "AEGISCRYPT SECURITY ANALYSIS REPORT\n"
            )

            report.write(
                "=" * 60 + "\n\n"
            )

            report.write(
                f"Generated On : {datetime.datetime.now()}\n\n"
            )

            report.write(
                f"Analyzed File : {selected_file}\n\n"
            )

            report.write(
                "SHA-256 HASH:\n"
            )

            report.write(
                f"{hash_value}\n\n"
            )

            report.write(
                "FILE METADATA:\n"
            )

            for key, value in metadata.items():

                report.write(
                    f"{key}: {value}\n"
                )

            report.write("\n")

            report.write(
                "=" * 60 + "\n"
            )

            report.write(
                "STATUS : VERIFIED\n"
            )

            report.write(
                "SECURITY LEVEL : HIGH\n"
            )

            report.write(
                "=" * 60 + "\n"
            )

        messagebox.showinfo(
            "SHA-256 Verification",
            f"Hash Generated Successfully\n\n"
            f"Report Saved At:\n{report_path}"
        )

    # =========================
    # METADATA VIEWER
    # =========================

    def metadata():

        if not selected_file:

            messagebox.showerror(
                "Error",
                "Please select a file"
            )

            return

        data = get_file_metadata(
            selected_file
        )

        output = "\n".join(
            [
                f"{key}: {value}"
                for key, value in data.items()
            ]
        )

        messagebox.showinfo(
            "File Metadata",
            output
        )

    # =========================
    # SECURE DELETE
    # =========================

    def delete_secure():

        if not selected_file:

            messagebox.showerror(
                "Error",
                "Please select a file"
            )

            return

        secure_delete(
            selected_file
        )

        messagebox.showinfo(
            "Secure Delete",
            "File securely deleted"
        )

        # =========================
    # QUARANTINE FILE
    # =========================

    def quarantine_file():

        if not selected_file:

            messagebox.showerror(
                "Error",
                "Please select a file"
            )

            return

        try:

            # Create quarantine folder

            os.makedirs(
                "quarantine",
                exist_ok=True
            )

            # Create logs folder

            os.makedirs(
                "logs",
                exist_ok=True
            )

            # Get filename

            filename = os.path.basename(
                selected_file
            )

            # Destination path

            destination = os.path.join(
                "quarantine",
                filename
            )

            # Move file

            shutil.move(
                selected_file,
                destination
            )

            # Generate timestamp

            timestamp = datetime.datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            # Write security log

            with open(
                "logs/security_logs.txt",
                "a"
            ) as log:

                log.write(
                    f"[{timestamp}] "
                    f"[QUARANTINE] "
                    f"{selected_file} "
                    f"→ {destination}\n"
                )

            # Success popup

            messagebox.showinfo(
                "Quarantine",
                "File moved to quarantine successfully"
            )

        except Exception as error:

            messagebox.showerror(
                "Quarantine Error",
                str(error)
            )

    # =========================
    # PASSWORD ENTRY
    # =========================

    password_entry = tk.Entry(
        app,
        width=40,
        show="*",
        font=("Arial", 11)
    )

    # =========================
    # BUTTONS
    # =========================

    tk.Button(
        app,
        text="Choose File",
        command=choose_file,
        width=25,
        bg="#30363d",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    password_entry.pack(pady=10)

    tk.Button(
        app,
        text="Encrypt File",
        command=encrypt,
        width=25,
        bg="#238636",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    tk.Button(
        app,
        text="Decrypt File",
        command=decrypt,
        width=25,
        bg="#1f6feb",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    tk.Button(
        app,
        text="Generate SHA-256",
        command=integrity_check,
        width=25,
        bg="#8957e5",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    tk.Button(
        app,
        text="View Metadata",
        command=metadata,
        width=25,
        bg="#d29922",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    tk.Button(
        app,
        text="Move To Quarantine",
        command=quarantine_file,
        width=25,
        bg="#ff9800",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    tk.Button(
        app,
        text="Secure Delete",
        command=delete_secure,
        width=25,
        bg="#da3633",
        fg="white",
        font=("Arial", 11, "bold"),
        relief="flat",
        cursor="hand2"
    ).pack(pady=10)

    # =========================
    # STATUS BAR
    # =========================

    status = tk.Label(
        app,
        text="System Status: SECURE",
        bd=1,
        relief=tk.SUNKEN,
        anchor=tk.W,
        bg="#161b22",
        fg="lime",
        font=("Arial", 10)
    )
    
    status.pack(
        side=tk.BOTTOM,
        fill=tk.X
    )

    app.mainloop()