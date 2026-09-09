import json
import os
import tkinter as tk

FILENAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x400")

        self.tasks = load_tasks()
        self.check_vars = []

        # Entry field + Add button
        entry_frame = tk.Frame(root)
        entry_frame.pack(pady=10, padx=10, fill="x")

        self.entry = tk.Entry(entry_frame)
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", lambda event: self.add_task())

        tk.Button(entry_frame, text="Add", command=self.add_task).pack(side="left", padx=5)

        # Frame that holds the task checkboxes
        self.task_frame = tk.Frame(root)
        self.task_frame.pack(fill="both", expand=True, padx=10)

        # Delete button for checked tasks
        tk.Button(root, text="Delete Checked", command=self.delete_checked).pack(pady=10)

        self.render_tasks()

    def render_tasks(self):
        # Clear current checkboxes
        for widget in self.task_frame.winfo_children():
            widget.destroy()
        self.check_vars = []

        for task in self.tasks:
            var = tk.BooleanVar(value=task["done"])
            self.check_vars.append(var)

            cb = tk.Checkbutton(
                self.task_frame,
                text=task["title"],
                variable=var,
                command=lambda t=task, v=var: self.toggle_done(t, v),
                anchor="w",
                justify="left"
            )
            cb.pack(fill="x", anchor="w")

    def add_task(self):
        title = self.entry.get().strip()
        if not title:
            return

        self.tasks.append({"title": title, "done": False})
        save_tasks(self.tasks)
        self.entry.delete(0, tk.END)
        self.render_tasks()

    def toggle_done(self, task, var):
        task["done"] = var.get()
        save_tasks(self.tasks)

    def delete_checked(self):
        self.tasks = [t for t in self.tasks if not t["done"]]
        save_tasks(self.tasks)
        self.render_tasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()