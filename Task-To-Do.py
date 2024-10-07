import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        status_label.config(text="Status: None")
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def remove_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
        update_button.config(state=tk.DISABLED)
        completed_button.config(state=tk.DISABLED)
        pending_button.config(state=tk.DISABLED)
        status_label.config(text="Status: None")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def update_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            tasks_listbox.delete(selected_index)
            tasks_listbox.insert(selected_index, new_task)
            task_entry.delete(0, tk.END)
            update_status_label()
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def mark_as_completed():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_index)
        tasks_listbox.delete(selected_index)
        tasks_listbox.insert(selected_index, task + " [Completed]")
        status_label.config(text="Status: Completed")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def mark_as_pending():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_index)
        tasks_listbox.delete(selected_index)
        tasks_listbox.insert(selected_index, task + " [Pending]")
        status_label.config(text="Status: Pending")
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

def on_select(event):
    if tasks_listbox.curselection():
        update_button.config(state=tk.NORMAL)
        completed_button.config(state=tk.NORMAL)
        pending_button.config(state=tk.NORMAL)
        update_status_label()
    else:
        update_button.config(state=tk.DISABLED)
        completed_button.config(state=tk.DISABLED)
        pending_button.config(state=tk.DISABLED)
        status_label.config(text="Status: None")

def update_status_label():
    try:
        selected_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_index)
        if "[Completed]" in task:
            status_label.config(text="Status: Completed")
        elif "[Pending]" in task:
            status_label.config(text="Status: Pending")
        else:
            status_label.config(text="Status: None")
    except IndexError:
        status_label.config(text="Status: None")

def main():
    global task_entry, tasks_listbox, update_button, completed_button, pending_button, status_label

    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("600x400")

    main_frame = tk.Frame(root)
    main_frame.pack(expand=True, fill=tk.BOTH)

    input_frame = tk.Frame(main_frame)
    input_frame.pack(pady=20)

    task_entry = tk.Entry(input_frame, width=40, font=('Arial', 14))
    task_entry.pack(side=tk.LEFT, padx=(0,8))

    add_button = tk.Button(input_frame, text="Add Task", command=add_task, font=('Arial', 12))
    add_button.pack(side=tk.LEFT)

    status_label = tk.Label(main_frame, text="Status: None", font=('Arial', 12))
    status_label.pack(pady=10)

    display_frame = tk.Frame(main_frame)
    display_frame.pack(pady=20)

    tasks_listbox = tk.Listbox(display_frame, width=50, height=10, font=('Arial', 12))
    tasks_listbox.pack(side=tk.LEFT, padx=(0, 10))
    tasks_listbox.bind('<<ListboxSelect>>', on_select)

    button_frame = tk.Frame(display_frame)
    button_frame.pack(side=tk.RIGHT)

    update_button = tk.Button(button_frame, text="Update Task", command=update_task, state=tk.DISABLED, font=('Arial', 12))
    update_button.pack(pady=5)

    completed_button = tk.Button(button_frame, text="Mark as Completed", command=mark_as_completed, state=tk.DISABLED, font=('Arial', 12))
    completed_button.pack(pady=5)

    pending_button = tk.Button(button_frame, text="Mark as Pending", command=mark_as_pending, state=tk.DISABLED, font=('Arial', 12))
    pending_button.pack(pady=5)

    remove_button = tk.Button(button_frame, text="Remove Task", command=remove_task, font=('Arial', 12))
    remove_button.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    main()
