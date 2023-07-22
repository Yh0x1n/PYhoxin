"""
Módulo para las funciones de agregar, buscar y eliminar canciones.
"""

from tkinter import *

#Función para agregar canciones
def agg():
    
    def clear_placeholder(event):
        if opt_window.focus_get() == entry1 and entry1.get() == placeholder_text[0]:
            entry1.delete(0, END)
        
        if opt_window.focus_get() == entry2 and entry2.get() == placeholder_text[1]:
            entry2.delete(0, END)
        
        if opt_window.focus_get() == entry3 and entry3.get() == placeholder_text[2]:
            entry3.delete(0, END)

    def restore_placeholder(event):
        if entry1.get() == "":
            entry1.insert(0, placeholder_text[0])

        if entry2.get() == "":
            entry2.insert(0, placeholder_text[1])
        
        if entry3.get() == "":
            entry3.insert(0, placeholder_text[2])
    
    opt_window = Tk()
    opt_window.geometry("200x250")
    opt_window.title("Agregar canción a la lista")
    opt_window.configure(bg = "dark slate gray")
    
    placeholder_text = ["Ej: Welcome To The Jungle", "Ej: Guns N' Roses", "Ej: Appetite For Destruction"]

    label1 = Label(opt_window, text = "Nombre de la canción",
                   bg = "dark slate gray", fg = "white", font = ("Roboto", 12, "bold"))
    label1.pack()

    entry1 = Entry(opt_window, fg = "black", font = ("Roboto", 10, "bold"))
    entry1.insert(0, placeholder_text[0])
    entry1.bind("<FocusIn>", clear_placeholder)
    entry1.bind("<FocusOut>", restore_placeholder)
    entry1.pack()

    label2 = Label(opt_window, text = "Nombre del artista",
                   bg = "dark slate gray", fg = "white", font = ("Roboto", 12, "bold"))
    label2.pack()

    entry2 = Entry(opt_window, fg = "black", font = ("Roboto", 10, "bold"))
    entry2.insert(0, placeholder_text[1])
    entry2.bind("<FocusIn>", clear_placeholder)
    entry2.bind("<FocusOut>", restore_placeholder)
    entry2.pack()

    label3 = Label(opt_window, text = "Nombre del artista",
                   bg = "dark slate gray", fg = "white", font = ("Roboto", 12, "bold"))
    label3.pack()

    entry3 = Entry(opt_window, fg = "black", font = ("Roboto", 10, "bold"))
    entry3.insert(0, placeholder_text[2])
    entry3.bind("<FocusIn>", clear_placeholder)
    entry3.bind("<FocusOut>", restore_placeholder)
    entry3.pack()

    Button(opt_window, text = "Cancelar", borderwidth = 3, relief = "solid",
            fg = "black", bg = "light gray", font = ("Roboto", 10, "bold"),
            command = opt_window.destroy).place(x = 100, y = 200)

    Button(opt_window, text = "Agregar", borderwidth = 3, relief = "solid",
            fg = "white", bg = "dark green", font = ("Roboto", 10, "bold")).place(x = 10, y = 200)