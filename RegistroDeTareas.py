from tkinter import *
import datetime
from tkinter import messagebox

class Tarea: #Clase con los atributos de la tarea
    def __init__(self, nombre):
        self.nombre = nombre
        self.fecha = datetime.datetime.now().strftime("%d/%m/%Y")

class Manager(Tarea): #Clase que permite guardar y cargar las tareas en archivos, con el nombre y fecha exactos
    def __init__(self, nombre):
        super().__init__(nombre)
        self.tareas = []
    def guardar(self):
        with open("tareas.txt", "w") as f: #Abrir el archivo en modo escritura
            for i in range(len(self.tareas)): #Recorrer la lista de tareas
                f.write(f"{self.tareas[i].nombre},{self.tareas[i].fecha}\n") #Escribir en el archivo

    def cargar(self):
        with open("tareas.txt", "r") as f: #Abrir el archivo en modo lectura
            for linea in f: #Recorrer el archivo
                self.nombre = linea.split(",")[0] #Separar la descripción de la fecha
                self.fecha = datetime.datetime.strptime(linea.split(",")[1], "%d/%m/%Y\n") #Separar la fecha
                self.tareas.append(Tarea(self.nombre)) #Agregar la tarea a la lista
            return self.tareas

class RegistroTareas(Tarea):
    def __init__(self):
        super().__init__(self)
        self.tareas = []

        self.ventana = Tk()
        self.ventana.title("Registro de tareas")
        self.ventana.geometry("385x410")
        self.ventana.configure(bg = "dark slate gray")
        self.ventana.resizable(0, 0)
    
        #Creando listbox para mostrar las tareas
        self.listbox = Listbox(self.ventana, borderwidth = 3, relief = "solid")
        self.listbox.place(x = 10, y = 10, width = 350, height = 300)
        self.listbox.config(font = ("Arial", 14))

        #Creando scrollbar para la listbox
        self.scrollbar = Scrollbar(self.ventana)
        self.scrollbar.pack(side = RIGHT, fill = Y)
        self.scrollbar.config(command = self.listbox.yview)
        self.listbox.config(yscrollcommand = self.scrollbar.set)

        #Creando botones para agregar y eliminar tareas
        self.boton1 = Button(self.ventana, text = "Agregar", bg = "light blue", font = ("Arial", 10, "bold"), borderwidth = 2, relief = "solid")
        self.boton1.place(x = 10, y = 350, width = 100, height = 30)
        self.boton1.config(command = self.agg_tarea)
        
        self.boton2 = Button(self.ventana, text = "Eliminar", bg = "tomato", font = ("Arial", 10, "bold"), borderwidth = 2, relief = "solid")
        self.boton2.place(x = 135, y = 350, width = 100, height = 30)
        self.boton2.config(command = self.elim_tarea)

        self.boton3 = Button(self.ventana, text = "Completar", bg = "light green", font = ("Arial", 10, "bold"), borderwidth = 2, relief = "solid")
        self.boton3.place(x = 260, y = 350, width = 100, height = 30)
        self.boton3.config(command = self.marcar_tarea)

        #Creando un menú superior con las opciones de guardar y cargar tareas
        self.menu = Menu(self.ventana)
        self.ventana.config(menu = self.menu)
        self.menu.add_command(label = "Guardar", command = self.guardar)
        self.menu.add_command(label = "Cargar", command = self.cargar)
        self.menu.add_command(label = "Salir", command = self.ventana.destroy)

        #Creando campo de texto para introducir el nombre de la tarea, y presionar enter para agregar
        self.texto = Entry(self.ventana, borderwidth = 1.5, relief = "solid")
        self.texto.place(x = 10, y = 320, width = 350)
        self.texto.bind("<Return>", lambda event : self.agg_tarea())

    def agg_tarea(self): #Método para agregar la tarea del usuario, la lista se actualiza al presionar el botón
        try:
            descripcion = self.texto.get()
            self.tareas.append(Tarea(descripcion))
            self.listbox.insert(END, f"> {descripcion} | {self.fecha}")

            #Limpiar el cuadro de entrada de texto
            self.texto.delete(0, END)
        
        except: #excepción por si se presiona el botón con el campo vacío
            messagebox.showinfo("Error", "No se puede agregar un campo vacío")

    def marcar_tarea(self): #Método para marcar la tarea con una casilla verde al ser completada
        self.listbox.itemconfig(self.listbox.curselection(), fg = "green")
        self.listbox.itemconfig(self.listbox.curselection(), bg = "white")
    
    def elim_tarea(self): #Método para eliminar la tarea, la lista se actualiza al presionar el botón
        seleccion = self.listbox.curselection()[0]
        try:
            self.listbox.delete(seleccion)
            self.tareas.pop(seleccion)
            self.actualizar_lista()

        except:
            messagebox.showinfo("Error", "No hay tareas que eliminar")
    
    def actualizar_lista(self): #Método para actualizar la lista si se agrega o elimina una tarea
        self.listbox.delete(0, END)
        for i in range(len(self.tareas)):
            self.listbox.insert(i+1, f"{self.tareas[i].nombre} | {self.tareas[i].fecha}")
        self.listbox.update()
    
    def guardar(self): #Guarda las tareas en los archivos de la clase Manager
        Manager.guardar(self)
        self.actualizar_lista()
        messagebox.showinfo("Guardado", "Tareas guardadas")
        
    def cargar(self): #Carga las tareas
        self.tareas = Manager.cargar(self)
        self.actualizar_lista()

reg = RegistroTareas()
reg.ventana.mainloop()
