"""
Programa de biblioteca musical, que contiene opciones para agregar, eliminar y
buscar canciones, álbumes y artistas.
"""

from tkinter import *

#Ventana
root = Tk()
root.geometry('300x600')
root.configure(bg = 'gray')

#Lista
box = Listbox(root, borderwidth = 3, relief = "solid")
box.place(x = 10, y = 50, width = 280, height = 500)

root.mainloop()