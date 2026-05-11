import tkinter as tk
from tkinter import messagebox

#FUNCTIONS

def click(value):
    current = display_var.get()
    display_var.set(current + str(value))


def clear():
    display_var.set("")


def backspace():
    current = display_var.get()
    display_var.set(current[:-1])


def calculate():
    try:
        expression = display_var.get()
        result = eval(expression)
        display_var.set(str(result))

    except:
        messagebox.showerror("Error", "Invalid Expression")
        display_var.set("")


#WINDOW

root = tk.Tk()
root.title("Calculator")
root.geometry("380x600")
root.config(bg="#090e1a")   
root.resizable(False, False)

#DISPLAY

display_var = tk.StringVar()

display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 28, "bold"),
    bd=0,
    bg="#1e293b",   
    fg="#ffffff",
    justify="right"
)

display.pack(
    fill="both",
    ipadx=8,
    ipady=25,
    padx=15,
    pady=20
)

#BUTTON FRAME

button_frame = tk.Frame(root, bg="#0f172a")
button_frame.pack()

#BUTTON STYLE

button_font = ("Arial", 16, "bold")

def create_button(text, row, col, command, bg, fg="white"):
    button = tk.Button(
        button_frame,
        text=text,
        command=command,
        font=button_font,
        width=5,
        height=2,
        bg=bg,
        fg=fg,
        bd=0,
        activebackground="#ffffff",
        cursor="hand2"
    )

    button.grid(row=row, column=col, padx=8, pady=8)


#ROW 1

create_button("C", 0, 0, clear, "#ef4444")        # Bright red
create_button("⌫", 0, 1, backspace, "#f97316")   # Orange
create_button("%", 0, 2, lambda: click("%"), "#8b5cf6") # Purple
create_button("/", 0, 3, lambda: click("/"), "#06b6d4") # Cyan

#ROW 2

create_button("7", 1, 0, lambda: click("7"), "#334155")
create_button("8", 1, 1, lambda: click("8"), "#334155")
create_button("9", 1, 2, lambda: click("9"), "#334155")
create_button("*", 1, 3, lambda: click("*"), "#06b6d4")

#ROW 3

create_button("4", 2, 0, lambda: click("4"), "#334155")
create_button("5", 2, 1, lambda: click("5"), "#334155")
create_button("6", 2, 2, lambda: click("6"), "#334155")
create_button("-", 2, 3, lambda: click("-"), "#06b6d4")

#ROW 4

create_button("1", 3, 0, lambda: click("1"), "#334155")
create_button("2", 3, 1, lambda: click("2"), "#334155")
create_button("3", 3, 2, lambda: click("3"), "#334155")
create_button("+", 3, 3, lambda: click("+"), "#06b6d4")

#ROW 5

create_button("0", 4, 0, lambda: click("0"), "#334155")
create_button(".", 4, 1, lambda: click("."), "#334155")
create_button("(", 4, 2, lambda: click("("), "#8b5cf6")
create_button(")", 4, 3, lambda: click(")"), "#8b5cf6")

#EQUAL BUTTON

equal_button = tk.Button(
    root,
    text="ENTER",
    command=calculate,
    font=("Arial", 20, "bold"),
    bg="#22c55e",   # Neon green
    fg="white",
    bd=0,
    height=2,
    activebackground="#16a34a",
    cursor="hand2"
)

equal_button.pack(fill="x", padx=20, pady=15)

#RUN

root.mainloop()