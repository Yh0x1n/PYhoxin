#Pandas 1: Series

import pandas as pd

materias = pd.Series({'Math' : 15, 'Física' : 18, 'Química'  : 20})
print(materias) #Diccionario


colores = pd.Series(['rojo', 'amarillo', 'azul', 'verde'])
print(colores) #Lista

numeros = pd.Series([1, 2, 3, 4, 5 ,6 ,7 , 8, 9])
numeros.size
print(f"\n {numeros[2 : 7]}") #Lista

