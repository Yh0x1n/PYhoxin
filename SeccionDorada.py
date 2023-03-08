#Programa que utiliza el método de la sección dorada para optimizar una función

#Importar librerías
import math

#Definir funcion
def f(x):
    return x**3 - 13*(x)/10

#Definir intervalos de búsqueda con entradas del usuario
xl = int(input("Ingrese el valor de Xl: "))
xu = int(input("Ingrese el valor de Xu: "))
float(xl)
float(xu)

#Definir número de iteraciones
n = 15

#Definir margen de error o tolerancia con entrada de usuario
tol = float(input("Ingrese el margen de error: "))

#Definir ciclo de iteraciones
for i in range(n):
    a = 0.618*(xu - xl)
    b = (0.618**2)*(xu - xl)    
    x1 = xl + a
    x2 = xl + b
    f1 = f(x1)
    f2 = f(x2)
    if f1 > f2:
        xl = xl
        xu = x1
        margen = abs(x1 - x2)
        if margen < tol:
            break
    else:
        xl = x2
        xu = xu
        margen = abs(x1 - x2)
        if margen < tol:
            print(f"Iteración {i+1}:\nX1 = {x1},\nX2 = {x2},\nF1 = {f1},\nF2 = {f2}, \nMargen = {margen}\n")
            break
    print(f"Iteración {i+1}:\nX1 = {x1},\nX2 = {x2},\nF1 = {f1},\nF2 = {f2}, \nMargen = {margen}\n")