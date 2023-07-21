import tkinter as tk
from tkinter import ttk

def main():
    root = tk.Tk()
    root.title("Listbox Example")

    # Create a Treeview widget with 3 columns
    treeview = ttk.Treeview(root, columns=("col1", "col2", "col3"), show="headings")
    treeview.pack(fill="both", expand=True)

    # Set the column headings
    treeview.heading("col1", text="Column 1")
    treeview.heading("col2", text="Column 2")
    treeview.heading("col3", text="Column 3")

    # Add some sample data
    for i in range(10):
        treeview.insert("", "end", values=("Item " + str(i), "Value " + str(i), "Description " + str(i)))

    root.mainloop()

if __name__ == "__main__":
    main()