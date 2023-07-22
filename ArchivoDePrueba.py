from tkinter import *

def clear_placeholder(event):
    if entry.get() == placeholder_text:
        entry.delete(0, END)

root = Tk()

placeholder_text = "Enter a song"

entry = Entry(root)
entry.insert(0, placeholder_text)
entry.bind("<FocusIn>", clear_placeholder)
entry.pack()

root.mainloop()