import tkinter as tk
from tkinter import messagebox
import json

# File to save the tasks
TASKS_FILE = "tasks.json"

# Function to load tasks from the file
def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

# Function to save tasks to the file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file)

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append({"task": task, "completed": False})
        task_entry.delete(0, tk.END)
        update_task_list()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to remove a task
def remove_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks.pop(task_index)
        update_task_list()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

# Function to toggle task completion
def toggle_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_index = selected_task_index[0]
        tasks[task_index]["completed"] = not tasks[task_index]["completed"]
        update_task_list()
        save_tasks(tasks)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to update the task list display
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        display_text = task["task"]
        if task["completed"]:
            display_text = f"✔ {display_text}"
        task_listbox.insert(tk.END, display_text)

# Initialize the main application window
root = tk.Tk()
root.title("To-Do List")

# Load existing tasks from file
tasks = load_tasks()

# Task input field
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Add task button
add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack(pady=5)

# Task listbox (to display tasks)
task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
task_listbox.pack(pady=10)

# Mark as completed button
complete_button = tk.Button(root, text="Mark as Completed", width=20, command=toggle_task)
complete_button.pack(pady=5)

# Remove task button
remove_button = tk.Button(root, text="Remove Task", width=20, command=remove_task)
remove_button.pack(pady=5)

# Update task list to reflect current tasks
update_task_list()

# Start the Tkinter event loop
root.mainloop()
