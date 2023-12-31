import tkinter as tk
import threading
import time

# Initialize variables
tasks = {}
next_task_id = 1
ok_thread = True

# Variables to store the selected task ID for updating
selected_task_id = None

# Functions for task management
def add_task(text, hours):
    global next_task_id
    seconds = int(hours * 3600)
    task_id = next_task_id
    tasks[task_id] = {"text": text, "seconds": seconds}
    next_task_id += 1
    timer = threading.Timer(seconds, task_time_up, args=[task_id])
    timer.start()

def save_updated_task(text, hours):
    global selected_task_id
    if selected_task_id is not None:
        task_info = tasks.get(selected_task_id)
        if task_info:
            task_info["text"] = text
            task_info["seconds"] = int(hours * 3600)
            selected_task_id = None
            update_task_list()

def task_time_up(task_id):
    task_info = tasks.get(task_id)
    if task_info:
        text = task_info["text"]
        del tasks[task_id]
        update_task_list()
        tk.messagebox.showinfo("Notification", f"Time for Task {task_id}: {text}")

def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        update_task_list()

def update_task(task_id):
    global selected_task_id
    selected_task_id = task_id
    task_info = tasks.get(task_id)
    if task_info:
        updated_task.set(task_info["text"])
        updated_time.set(task_info["seconds"] / 3600)
        updated_task_entry.focus_set()

def save_updated_changes():
    global selected_task_id
    if selected_task_id is not None:
        text = updated_task.get()
        hours = updated_time.get()
        save_updated_task(text, hours)

def real_time():
    if ok_thread:
        real_timer = threading.Timer(1.0, real_time)
        real_timer.start()
    for task_id, task_info in list(tasks.items()):
        if task_info["seconds"] == 0:
            del tasks[task_id]
        else:
            task_info["seconds"] -= 1
    update_task_list()

# GUI Functions
def get_entry(event=""):
    text = todo.get()
    hours = float(time.get())
    todo.delete(0, tk.END)
    time.delete(0, tk.END)
    todo.focus_set()
    if selected_task_id is None:
        add_task(text, hours)
    else:
        save_updated_task(text, hours)
    if 0 < hours < 1000:
        update_task_list()

def update_task_list():
    for widget in todolist.winfo_children():
        widget.destroy()
    for task_id, task_info in tasks.items():
        hours = task_info["seconds"] / 3600.0
        task_text = f"[Task {task_id}] {task_info['text']} - Time left: {hours:.2f} hours"
        task_label = tk.Label(todolist, text=task_text, font=("Arial", 12))
        task_label.pack()
        update_button = tk.Button(todolist, text="Update", command=lambda id=task_id: update_task(id))
        update_button.pack()
        delete_button = tk.Button(todolist, text="Delete", command=lambda id=task_id: delete_task(id))
        delete_button.pack()

# Main application
if _name_ == '_main_':
    app = tk.Tk()
    app.geometry("600x800")
    app.title("Todolist Reminder")
    app.rowconfigure(0, weight=1)

    frame = tk.Frame(app)
    frame.pack()

    label = tk.Label(app, text="Enter task:", wraplength=300, justify=tk.LEFT)
    label_hour = tk.Label(app, text="Enter time (hours)", wraplength=300, justify=tk.LEFT)

    todo = tk.Entry(app, width=50, font=("Arial", 14))
    time = tk.Entry(app, width=20, font=("Arial", 14))

    send = tk.Button(app, text='Add task', fg="#ffffff", bg='#4CAF50', height=2, width=40, font=("Arial", 14), command=get_entry)
    quit = tk.Button(app, text='Exit', fg="#ffffff", bg='#4CAF50', height=2, width=40, font=("Arial", 14), command=app.destroy)

    todolist = tk.Frame(app)

    updated_task = tk.StringVar()
    updated_time = tk.DoubleVar()
    updated_task_entry = tk.Entry(app, width=50, font=("Arial", 14), textvariable=updated_task)
    updated_time_entry = tk.Entry(app, width=20, font=("Arial", 14), textvariable=updated_time)

    update_button = tk.Button(app, text="Update", fg="#ffffff", bg='#3498DB', height=2, width=15, font=("Arial", 14), command=save_updated_changes)
    save_button = tk.Button(app, text="Save", fg="#ffffff", bg='#3498DB', height=2, width=15, font=("Arial", 14), command=get_entry)

    if tasks:
        real_time()

    app.bind('<Return>', get_entry)

    label.place(x=10, y=10, width=300, height=25)
    todo.place(x=120, y=40, width=400, height=30)
    label_hour.place(x=120, y=80, width=150, height=25)
    time.place(x=120, y=110, width=150, height=30)
    send.place(x=120, y=150, width=150, height=40)
    quit.place(x=280, y=150, width=150, height=40)
    todolist.place(x=120, y=200, width=400, height=400)
    updated_task_entry.place(x=120, y=620, width=300, height=30)
    updated_time_entry.place(x=430, y=620, width=70, height=30)
    update_button.place(x=510, y=620, width=60, height=40)

    app.mainloop()
    ok_thread = False
    sys.exit("FINISHED")
