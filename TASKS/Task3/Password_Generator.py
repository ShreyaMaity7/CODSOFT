import tkinter as tk
from tkinter import messagebox
import random
import string

#PASSWORD FUNCTION

def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4:
            messagebox.showwarning("Weak Password", "Use at least 4 characters")
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if number_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation

        if characters == "":
            messagebox.showerror("Error", "Select at least one option")
            return

        password = "".join(random.choice(characters) for _ in range(length))

        password_box.delete(0, tk.END)
        password_box.insert(0, password)

        #PASSWORD STRENGTH

        if length <= 5:
            strength_label.config(text="Weak Password", fg="#ef4444")

        elif length <= 8:
            strength_label.config(text="Medium Password", fg="#f59e0b")

        else:
            strength_label.config(text="Strong Password", fg="#22c55e")

    except:
        messagebox.showerror("Error", "Enter a valid number")


#COPY FUNCTION

def copy_password():
    password = password_box.get()

    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        copied_label.config(text="Password Copied ✓")

    else:
        copied_label.config(text="Generate a password first")


#WINDOW

root = tk.Tk()
root.title("Dark Password Generator")
root.geometry("500x600")
root.config(bg="#0f172a")   # Dark navy background
root.resizable(False, False)

#TITLE

title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Segoe UI", 24, "bold"),
    bg="#0f172a",
    fg="#e2e8f0"
)

title.pack(pady=25)

#LENGTH

tk.Label(
    root,
    text="Password Length",
    font=("Segoe UI", 14),
    bg="#0f172a",
    fg="#cbd5e1"
).pack()

length_entry = tk.Entry(
    root,
    font=("Segoe UI", 18),
    justify="center",
    bg="#1e293b",
    fg="white",
    insertbackground="white",
    bd=0,
    width=15
)

length_entry.pack(pady=15, ipady=8)

#OPTIONS

upper_var = tk.IntVar(value=1)
lower_var = tk.IntVar(value=1)
number_var = tk.IntVar(value=1)
symbol_var = tk.IntVar(value=1)

frame = tk.Frame(root, bg="#0f172a")
frame.pack(pady=10)

def custom_checkbox(text, variable):
    tk.Checkbutton(
        frame,
        text=text,
        variable=variable,
        font=("Segoe UI", 12),
        bg="#0f172a",
        fg="#e2e8f0",
        activebackground="#0f172a",
        activeforeground="white",
        selectcolor="#1e293b"
    ).pack(anchor="w", pady=5)

custom_checkbox("Uppercase Letters", upper_var)
custom_checkbox("Lowercase Letters", lower_var)
custom_checkbox("Numbers", number_var)
custom_checkbox("Symbols", symbol_var)

#GENERATE BUTTON

generate_btn = tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    font=("Segoe UI", 14, "bold"),
    bg="#6366f1",
    fg="white",
    bd=0,
    padx=20,
    pady=12,
    activebackground="#4f46e5",
    cursor="hand2"
)

generate_btn.pack(pady=25)

#PASSWORD BOX

password_box = tk.Entry(
    root,
    font=("Consolas", 18),
    justify="center",
    width=28,
    bg="#1e293b",
    fg="#22c55e",
    insertbackground="white",
    bd=0
)

password_box.pack(ipady=10)

#COPY BUTTON

copy_btn = tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    font=("Segoe UI", 12, "bold"),
    bg="#14b8a6",
    fg="white",
    bd=0,
    padx=15,
    pady=10,
    activebackground="#0f766e",
    cursor="hand2"
)

copy_btn.pack(pady=20)

#STATUS LABELS

strength_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 13, "bold"),
    bg="#0f172a"
)

strength_label.pack()

copied_label = tk.Label(
    root,
    text="",
    font=("Segoe UI", 11),
    bg="#0f172a",
    fg="#94a3b8"
)

copied_label.pack(pady=10)

#FOOTER

footer = tk.Label(
    root,
    text="Python Tkinter Project",
    font=("Segoe UI", 10),
    bg="#0f172a",
    fg="#64748b"
)

footer.pack(side="bottom", pady=10)

#RUN

root.mainloop()