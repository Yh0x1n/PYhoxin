#Pandas 1: Series

import pandas as pd #Importación

materias = pd.Series({'Math' : 15, 'Física' : 18, 'Química'  : 20})
print(materias) #Diccionario


colores = pd.Series(['rojo', 'amarillo', 'azul', 'verde'])
print(colores) #Lista

numeros = pd.Series([1, 2, 3, 4, 5 ,6 ,7 , 8, 9])
numeros.size
print(f"\n {numeros[2 : 7]}") #Lista

print(numeros.sum())
print(materias[materias > 15].sort_index(ascending = False))

data = 5
serie = pd.Series(data, index = [0, 1, 2, 3, 4, 5])
print(serie)

data_list = ['Yhoxin', 'Jesús', 'Messi', 'CR7']
indices = ['Inter Miami', 'Al-Nassr', 'Barcelona', 'Real Madrid']

furbo = pd.Series(index = indices, data = data_list)
print(furbo)
