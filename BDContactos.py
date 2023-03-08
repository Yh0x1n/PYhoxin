"""Programa de base de datos de contactos, donde el usuario puede guardar sus contactos por nombre,
apellido y teléfono en archivos JSON"""

from tkinter import *
import json

class Contactos:
    def __init__(self, master):
        self.master = master
        master.title("Lista de contactos")
        
        self.lista = Listbox(master, borderwidth=3, relief="solid", font=("Arial", 13))
        self.lista.place(x=50, y=30, width=300, height=300)
        
        self.label1 = Label(master, text="Nombre", font=("Arial", 12, "bold"),
                               fg="black", bg="dark green")
        self.label1.place(x=75, y=5)
        self.label2 = Label(master, text="Teléfono", font=("Arial", 12, "bold"),
                               fg="black", bg="dark green")
        self.label2.place(x=250, y=5)
        self.label_nombre = Label(master, text="Nombre:", font=("Arial", 10, "bold"),
                                     fg="black", bg="dark green")
        self.label_nombre.place(x=50, y=350)
        self.label_tlf = Label(master, text="Teléfono:", font=("Arial", 10, "bold"),
                                  fg="black", bg="dark green")
        self.label_tlf.place(x=50, y=380)
        self.entrada_nombre = Entry(master, font=("Arial", 10), fg="black")
        self.entrada_nombre.place(x=120, y=350)
        self.entrada_tlf = Entry(master, font=("Arial", 10), fg="black")
        self.entrada_tlf.place(x=120, y=380)
        self.entrada_tlf.bind("<Return>", lambda event: self.agregar())
        
        self.scrollbar = Scrollbar(master, command=self.lista.yview)
        self.scrollbar.place(x=350, y=30, height=300)
        self.lista.config(yscrollcommand=self.scrollbar.set)
        
        self.linea = Canvas(master, width=2, height=285, bg="black")
        self.linea.place(x=200, y=35)
        
        self.boton1 = Button(master, text="Agregar", command=self.agregar, font=("Arial", 10, "bold"),
                             bg="light blue", borderwidth=2, relief="solid")
        self.boton1.place(x=275, y=335)
        self.boton2 = Button(master, text="Eliminar", command=self.eliminar, font=("Arial", 10, "bold"),
                             bg="tomato", borderwidth=2, relief="solid")
        self.boton2.place(x=275, y=365)
        self.boton3 = Button(master, text="Guardar y salir", command=self.guardar_salir, font=("Arial", 10, "bold"),
                             bg="light green", borderwidth=2, relief="solid")
        self.boton3.place(x=275, y=395)
        self.cargar()

    def agregar(self):
        nombre = self.entrada_nombre.get()
        tlf = self.entrada_tlf.get()
        self.lista.insert(END, f"> {nombre:<25}{tlf:>10}")
        self.entrada_nombre.delete(0, END)
        self.entrada_tlf.delete(0, END)
        self.entrada_nombre.focus()

    def eliminar(self):
        seleccionado = self.lista.curselection()
        if seleccionado:
            self.lista.delete(seleccionado)

    def guardar_salir(self):
        contactos = []
        for i in range(self.lista.size()):
            contacto = self.lista.get(i)
            nombre, tlf = contacto.split()
            contactos.append({"nombre": nombre, "tlf": tlf})
        with open("contactos.json", "w") as archivo:
            json.dump(contactos, archivo)
        self.master.destroy()

    def cargar(self):
        try:
            with open("contactos.json", "r") as archivo:
                datos = json.load(archivo)
                for i in datos:
                    nombre = i.get("nombre")
                    tlf = i.get("tlf")
                    contador = 1
                    self.lista.insert(END, f"{contador+1} > {nombre:<25}{tlf:>10}")
        except FileNotFoundError:
            pass

ventana = Tk()
ventana.geometry("400x450")
ventana.configure(bg = "dark green", relief = SOLID)
contactos = Contactos(ventana)
app = Contactos(ventana)
ventana.mainloop()