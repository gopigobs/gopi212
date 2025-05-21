import tkinter as tk
from tkinter import messagebox
import os

TASKS_FILE = "tasks.txt"

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.task_var = tk.StringVar()

        tk.Entry(root, textvariable=self.task_var, width=40).pack(pady=10)
        tk.Button(root, text="Add Task", command=self.add_task).pack()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)

        tk.Button(root, text="Delete Task", command=self.delete_task).pack()
        tk.Button(root, text="Mark as Done", command=self.mark_done).pack()
        tk.Button(root, text="Save Tasks", command=self.save_tasks).pack()

        self.load_tasks()

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_var.set("")
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def delete_task(self):
        try:
            index = self.listbox.curselection()[0]
            self.listbox.delete(index)
        except IndexError:
            messagebox.showwarning("Select Error", "Please select a task to delete.")

    def mark_done(self):
        try:
            index = self.listbox.curselection()[0]
            task = self.listbox.get(index)
            if not task.startswith("✓ "):
                self.listbox.delete(index)
                self.listbox.insert(index, "✓ " + task)
        except IndexError:
            messagebox.showwarning("Select Error", "Please select a task to mark as done.")

    def save_tasks(self):
        tasks = self.listbox.get(0, tk.END)
        with open(TASKS_FILE, 'w') as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Success", "Tasks saved!")

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as f:
                for line in f:
                    self.listbox.insert(tk.END, line.strip())

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
