from tkinter import *

class Propinas:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora de propinas") #Titulo del programa

        #Se crean los widgets:
        self.label_total = Label(master, text="Total a pagar: ", bg = "dark slate gray")
        self.label_propina = Label(master, text = "Porcentaje de\npropina", bg = "dark slate gray")
        self.entry_total = Entry(master, width= 20)
        self.entry_propina = Entry(master, width = 20)
        self.btn = Button(master, text = "Calcular propina", command = self.calc_propina)
        self.label_resultado = Label(master, text = "El resultado se mostrará aquí")

        #Se ubican los widgets en la ventana
        self.label_total.place(x = 10, y = 10)
        self.label_propina.place(x = 10, y = 40)
        self.entry_total.place(x = 100, y = 10)
        self.entry_propina.place(x = 100, y = 40)
        self.btn.place(x = 10, y = 80)
        self.label_resultado.place(x = 10, y = 110)
        self.label_resultado.config(text = "")

    def calc_propina(self):
        self.total = float(self.entry_total.get())
        self.propina = float(self.entry_propina.get()) / 100
        resultado = self.total * self.propina
        self.label_resultado.configure(text=f"Propina: {resultado:.2f}", bg = "dark slate gray", font= ("Arial", 12, "bold"))

root = Tk()
calculadora = Propinas(root)
root.config(bg = "dark slate gray")
root.mainloop()