"""Programa de biblioteca musical, que contiene módulos para agregar, buscar, seleccionar y
seleccionar artistas, álbumes y canciones"""

from tkinter import *
from ttkthemes import ThemedStyle

class Biblioteca:
    def __init__(self):
        #Ventana
        self.master = Tk()
        self.master.geometry("300x600")
        self.master.title("Biblioteca Musical")
        self.master.configure(bg = "gray")
        self.style = ThemedStyle(self.master)
        self.style.set_theme("clam")
        
        #Lista
        self.box = Listbox(self.master, borderwidth = 3, relief = "solid", font = ("Roboto", 10, "bold"))
        self.box.place(x = 10, y = 30, width = 275, height = 500)

        

musik = Biblioteca()
musik.master.mainloop()