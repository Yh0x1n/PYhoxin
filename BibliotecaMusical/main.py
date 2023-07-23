"""
Programa de biblioteca musical, que contiene opciones para agregar, eliminar y
buscar canciones, álbumes y artistas.
"""

from tkinter import *
from functions import *

#Funciones para abrir las opciones
def open_agg():
    agg()

#Ventana
root = Tk()
root.title("Biblioteca Musical")
root.geometry('300x600')
root.configure(bg = 'gray')

#Lista
box = Listbox(root, borderwidth = 3, relief = "solid", font = ("Roboto", 12, "bold"))
box.place(x = 10, y = 50, width = 280, height = 500)
box.columnconfigure(0, weight = 1)
box.columnconfigure(1, weight = 1)
box.columnconfigure(2, weight = 1)

#Botones
btn_agregar = Button(root, text = "Agregar",width = 5, borderwidth = 3, relief = "solid",
                       bg = "dark slate gray", fg = "white", font = ("Roboto", 10, "bold"),
                       command = open_agg)
btn_agregar.place(x = 10, y = 10)

btn_buscar = Button(root, text = "Buscar", width = 5, borderwidth = 3, relief = "solid",
                       bg = "light gray", fg = "black", font = ("Roboto", 10, "bold"))
btn_buscar.place(x = 115, y = 10)

btn_eliminar = Button(root, text = "Eliminar", width = 5, borderwidth = 3, relief = "solid",
                         bg = "dark red", fg = "white", font = ("Roboto", 10, "bold"))
btn_eliminar.place(x = 218, y = 10)

btn_salir = Button(root, text = "Salir", width = 5, borderwidth = 3, relief = "solid",
                   bg = "white", fg = "black", font = ("Roboto", 10, "bold"),
                   command = root.destroy)
btn_salir.place(x = 218, y = 550)

#Scrollbar
vbar = Scrollbar(box, orient = VERTICAL, borderwidth = 2, relief = "flat")
vbar.pack(side = RIGHT, fill = Y)
hbar = Scrollbar(box, orient = HORIZONTAL, borderwidth = 2, relief = "flat")
hbar.pack(side = BOTTOM, fill = X)

root.mainloop()