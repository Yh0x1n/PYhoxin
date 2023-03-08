import tkinter as tk
from tkinter import messagebox
from datetime import datetime

class Task:
    def __init__(self, description):
        self.description = description
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

class TaskListApp:
    def __init__(self, master):
        self.master = master
        master.title("Registro de Tareas")

        self.tasks = []

        # Create the listbox to display the tasks
        self.task_listbox = tk.Listbox(master, width=50, height=15)
        self.task_listbox.grid(row=0, column=0, padx=10, pady=10)

        # Create the label and entry for adding tasks
        self.add_task_label = tk.Label(master, text="Nueva tarea:")
        self.add_task_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.add_task_entry = tk.Entry(master, width=50)
        self.add_task_entry.grid(row=2, column=0, padx=10, pady=5)

        # Create the button to add tasks
        self.add_task_button = tk.Button(master, text="Agregar Tarea", command=self.add_task)
        self.add_task_button.grid(row=2, column=1, padx=5, pady=5)

        # Create the button to delete tasks
        self.delete_task_button = tk.Button(master, text="Eliminar Tarea", command=self.delete_task)
        self.delete_task_button.grid(row=3, column=1, padx=5, pady=5)

        # Display the current tasks in the listbox
        self.update_task_listbox()

    def add_task(self):
        # Get the description of the task from the entry box
        description = self.add_task_entry.get()

        # Create a new Task object and add it to the task list
        new_task = Task(description)
        self.tasks.append(new_task)

        # Update the task listbox with the new task
        self.update_task_listbox()

        # Clear the entry box
        self.add_task_entry.delete(0, "end")

    def delete_task(self):
        # Get the currently selected task from the listbox
        try:
            index = self.task_listbox.curselection()[0]
            task = self.tasks[index]
        except IndexError:
            messagebox.showerror("Error", "Por favor seleccione una tarea para eliminar.")
            return

        # Remove the selected task from the task list
        self.tasks.remove(task)

        # Update the task listbox
        self.update_task_listbox()

    def update_task_listbox(self):
        # Clear the listbox
        self.task_listbox.delete(0, "end")

        # Add each task to the listbox
        for task in self.tasks:
            self.task_listbox.insert("end", task.description)

# Create the main window and run the app
root = tk.Tk()
app = TaskListApp(root)
root.mainloop()