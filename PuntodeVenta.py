#Programa de punto de venta, que cobra el monto de un producto + el IVA.

from tkinter import *
class PuntoVenta:
    def __init__(self): #Ventana de inicio
        self.root = Tk()
        self.root.title("Punto de Venta")
        self.root.geometry("300x300")
        self.root.resizable(0,0)
        self.root.config(bg = "blue")

    def calcular (self): #Calcula el monto total del producto, más el IVA
        self.monto = float(self.entry.get())
        self.iva = 1.5
        self.total = self.monto + self.iva
        self.total = round(self.total,2)
        self.total = str(self.total)
        self.total = self.total.replace(".",",")
        try:
            self.label.config(text = "El total es: " + self.total)
            self.entry.delete(0,END)
        except ValueError:
            self.label.config(text = "No puede dejar el campo vacío")
            self.entry.delete(0,END)

    def compra(self): #Ventana de compra, pide al usuario ingresar el monto del producto y lo multiplica por el IVA
            
        self.root.destroy()
        self.root2 = Tk()
        self.root2.title("Compra")
        self.root2.geometry("300x300")
        self.root2.resizable(0,0)
        self.root2.config(bg = "green")
        self.label = Label(self.root2, text = "Monto del producto: ", bg = "green", font = ("Arial", 12))
        self.label.pack()

        def regresar(): #Regresa a la ventana de inicio
            self.root2.destroy()
            self.__init__()
            self.main()

        self.entry = Entry(self.root2, bg = "white")
        self.entry.place(x = 80, y = 50)
        self.entry.focus()

        self.btn = Button(self.root2, text = "CALCULAR", command = self.calcular)
        self.btn.place(x = 80, y = 100)
        self.btn.config(bg = "white")
    
        self.btn2 = Button(self.root2, text = "REGRESAR", command = regresar)
        self.btn2.place(x = 80, y = 150)
        self.btn2.config(bg = "white")

        self.root2.mainloop()

    def main(self):
        label1 = Label(self.root, text = "SISTEMA DE\nPUNTO DE VENTA", bg = "blue", fg = "white", font = ("Arial", 12))
        label1.pack()
        label1.place(x = 50, y = 10, width = 200, height = 50)
        compra = Button(self.root, text = "COMPRA", bg = "white", fg = "blue", font = ("Arial", 12), command=self.compra)
        compra.pack()
        compra.place(x = 100, y = 70 , width = 100, height = 50)

        salir = Button(self.root, text = "SALIR", bg = "white", fg = "blue", font = ("Arial", 12), command=self.root.destroy)
        salir.pack()
        salir.place(x = 100, y = 130, width = 100, height = 50)

        self.root.mainloop()

pv = PuntoVenta()
pv.main()