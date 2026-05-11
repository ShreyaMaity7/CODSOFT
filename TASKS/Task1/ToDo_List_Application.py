import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import json, os
from datetime import datetime

FILE_NAME = "tasks.json"

#FILE 
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    return []

def save_tasks():
    with open(FILE_NAME, "w") as f:
        json.dump(tasks, f, indent=4)

#LOGIC
def update_dashboard():
    total = len(tasks)
    done = sum(1 for t in tasks if t["done"])
    pending = total - done
    dashboard_label.config(
        text=f"Total: {total} | Done: {done} | Pending: {pending}"
    )

def update_list():
    listbox.delete(0, tk.END)

    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✗"
        text = f"{t['task']} | {t['deadline']} [{status}]"
        listbox.insert(tk.END, text)

        #Highlight overdue tasks
        if not t["done"]:
            try:
                due = datetime.strptime(t["deadline"], "%Y-%m-%d")
                if due < datetime.now():
                    listbox.itemconfig(i, fg="red")
            except:
                pass

    update_dashboard()

#ACTIONS
def add_task():
    task = task_entry.get().strip()
    deadline = cal.get_date().strftime("%Y-%m-%d")

    if not task:
        messagebox.showwarning("Warning", "Task cannot be empty!")
        return

    tasks.append({
        "task": task,
        "done": False,
        "deadline": deadline
    })

    task_entry.delete(0, tk.END)
    save_tasks()
    update_list()

def mark_done():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    index = selected[0]
    tasks[index]["done"] = True
    save_tasks()
    update_list()

def delete_task():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    index = selected[0]
    tasks.pop(index)
    save_tasks()
    update_list()

def clear_completed():
    global tasks
    tasks = [t for t in tasks if not t["done"]]
    save_tasks()
    update_list()

#UI
root = tk.Tk()
root.title("To-Do List")
root.geometry("500x550")
root.configure(bg="#1e1e2f")

tasks = load_tasks()

#Title
tk.Label(
    root,
    text="To-Do List",
    font=("Arial", 20, "bold"),
    bg="#1e1e2f",
    fg="white"
).pack(pady=10)

#Dashboard
dashboard_label = tk.Label(
    root,
    text="",
    font=("Arial", 12),
    bg="#1e1e2f",
    fg="#00ffcc"
)
dashboard_label.pack()

#Task input
task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.pack(pady=5)

#Calendar
cal = DateEntry(
    root,
    width=20,
    background='darkblue',
    foreground='white',
    date_pattern='yyyy-mm-dd'
)
cal.pack(pady=5)

#Buttons
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame, text="Add", width=12,
    bg="#4CAF50", fg="white",
    command=add_task
).grid(row=0, column=0, padx=5)

tk.Button(
    btn_frame, text="Complete", width=12,
    bg="#2196F3", fg="white",
    command=mark_done
).grid(row=0, column=1, padx=5)

tk.Button(
    btn_frame, text="Delete", width=12,
    bg="#f44336", fg="white",
    command=delete_task
).grid(row=0, column=2, padx=5)

tk.Button(
    btn_frame,
    text="Clear Completed",
    width=26,
    bg="#9C27B0",
    fg="white",
    command=clear_completed
).grid(row=1, column=0, columnspan=3, pady=5)

#Listbox
listbox = tk.Listbox(
    root,
    width=60,
    height=15,
    bg="#2e2e3e",
    fg="white"
)
listbox.pack(pady=10)

#Initial load
update_list()

root.mainloop()