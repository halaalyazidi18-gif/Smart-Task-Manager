import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

tasks = []

def convert_time(time_str):

    if time_str.endswith("s"):
        return int(time_str[:-1])

    elif time_str.endswith("m"):
        return int(time_str[:-1]) * 60

    elif time_str.endswith("h"):
        return int(time_str[:-1]) * 3600

    else:
        return int(time_str)



def add_task():

    name = task_entry.get()
    importance = priority_entry.get()
    time = time_entry.get()

    if name == "" or importance == "" or time == "":
        messagebox.showwarning("Error", "Fill all fields")
        return

    importance = int(importance)
    time = convert_time(time)

    score = importance * 10 - time

    tasks.append([name, importance, time, score])

    task_entry.delete(0, tk.END)
    priority_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

    show_tasks()


def show_tasks():

    task_list.delete(0, tk.END)

    for i, task in enumerate(tasks):

        name = task[0]
        importance = task[1]
        time = task[2]

        task_list.insert(
            tk.END,
            f"{name} | Priority:{importance} | Time:{time}"
        )

        if importance >= 4:
            task_list.itemconfig(i, {'bg':'#ff8a80'})  # red

        elif importance == 3:
            task_list.itemconfig(i, {'bg':'#fff59d'})  # yellow

        else:
            task_list.itemconfig(i, {'bg':'#a5d6a7'})  # green


def delete_task():

    selected = task_list.curselection()

    if not selected:
        return

    index = selected[0]
    tasks.pop(index)

    show_tasks()


def edit_task():

    selected = task_list.curselection()

    if not selected:
        return

    index = selected[0]

    name = task_entry.get()
    importance = int(priority_entry.get())
    time = convert_time(time_entry.get())

    score = importance * 10 - time

    tasks[index] = [name, importance, time, score]

    show_tasks()


def organize_tasks():

    tasks.sort(key=lambda x: x[3], reverse=True)
    show_tasks()

def suggest_task():

    if len(tasks) == 0:
        messagebox.showinfo("Suggestion", "No tasks available")
        return

    tasks.sort(key=lambda x: x[3], reverse=True)

    best_task = tasks[0]

    messagebox.showinfo(
        "Next Task",
        f"You should start with:\n\n{best_task[0]}"
    )


def show_chart():

    if len(tasks) == 0:
        return

    names = [task[0] for task in tasks]
    scores = [task[3] for task in tasks]

    plt.bar(names, scores)
    plt.title("Task Priority")
    plt.xlabel("Tasks")
    plt.ylabel("Priority Score")
    plt.show()


root = tk.Tk()
root.title("Task Organizer")
root.geometry("520x560")
root.configure(bg="#e8f0fe")

title = tk.Label(
    root,
    text="Task Organizer",
    font=("Arial",18,"bold"),
    bg="#e8f0fe"
)
title.pack(pady=10)

tk.Label(root,text="Task Name",bg="#e8f0fe").pack()
task_entry = tk.Entry(root,width=35)
task_entry.pack()

tk.Label(root,text="Importance (1-5)",bg="#e8f0fe").pack()
priority_entry = tk.Entry(root,width=35)
priority_entry.pack()

tk.Label(root,text="Time (60s / 10m / 2h)",bg="#e8f0fe").pack()
time_entry = tk.Entry(root,width=35)
time_entry.pack()

tk.Button(
    root,
    text="Add Task",
    bg="#4CAF50",
    fg="white",
    width=20,
    command=add_task
).pack(pady=5)

tk.Button(
    root,
    text="Edit Task",
    bg="#2196F3",
    fg="white",
    width=20,
    command=edit_task
).pack(pady=5)

tk.Button(
    root,
    text="Delete Task",
    bg="#f44336",
    fg="white",
    width=20,
    command=delete_task
).pack(pady=5)

tk.Button(
    root,
    text="Organize Tasks",
    bg="#9C27B0",
    fg="white",
    width=20,
    command=organize_tasks
).pack(pady=5)

tk.Button(
    root,
    text="Suggest Next Task",
    bg="#00BCD4",
    fg="white",
    width=20,
    command=suggest_task
).pack(pady=5)

tk.Button(
    root,
    text="Show Priority Chart",
    bg="#FF9800",
    fg="white",
    width=20,
    command=show_chart
).pack(pady=5)

task_list = tk.Listbox(root,width=60,height=12)
task_list.pack(pady=10)

root.mainloop()