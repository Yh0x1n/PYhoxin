#Calculadora de índice de masa corporal (IMC) con Tkinter

from tkinter import *

class IMC:
    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("Calculadora de IMC")
        self.ventana.geometry("300x200")
        self.etiqueta_peso = Label(self.ventana, text="Peso (kg):")
        self.etiqueta_peso.grid(row=0, column=0)
        self.peso = Entry(self.ventana)
        self.peso.grid(row=0, column=1)
        self.etiqueta_altura = Label(self.ventana, text="Altura (m):")
        self.etiqueta_altura.grid(row=1, column=0)
        self.altura = Entry(self.ventana)
        self.altura.grid(row=1, column=1)
        self.boton_calcular = Button(self.ventana, text="Calcular IMC", command=self.calcular)
        self.boton_calcular.grid(row=2, column=0 , columnspan=2)
        self.etiqueta_resultado = Label(self.ventana, text="Resultado:")
        self.etiqueta_resultado.grid(row=3, column=0)
        self.resultado = Label(self.ventana, text="")
        self.resultado.grid(row=3, column=1)
        self.ventana.mainloop()
    def calcular(self):
        try:
            peso = float(self.peso.get())
            altura = float(self.altura.get())
            imc = peso / (altura**2)
            imc = round(imc, 2)

            if imc < 18.5:
                self.resultado.config(text=f"{imc} - Bajo peso")
                self.resultado.config(fg="blue")
            elif imc < 25:
                self.resultado.config(text=f"{imc} - Normal")
                self.resultado.config(fg="green")
            elif imc < 30:
                self.resultado.config(text=f"{imc} - Sobrepeso")
                self.resultado.config(fg="red")
            else:
                self.resultado.config(text=f"{imc} - Obesidad")
                self.resultado.config(fg="red")
        except:
            self.resultado.config(text="Error")

calc = IMC()