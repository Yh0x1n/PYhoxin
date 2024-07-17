#Pandas 2: Dataframes

import pandas as pd #Importación
import numpy as np

data = {'nombre' : ['Yhoxin', 'Josmer', 'Génesis'],  #A partir de un diccionario
        'carrera' : ['Sistemas', 'Diseño', 'Gastronomía'],
        'correo' : ['yhoxin@correo.com', 'josmerfurro@correo.com', 'gini20@correo.com']}

estudiantes = pd.DataFrame(data)
print(estudiantes)

df = pd.DataFrame([['Yhoxin', 22], ['Josmer', 21], ['Génesis', 21]], #A partir de una lista
                  columns = ['Nombre', 'Edad'])
print(df)

fd = pd.DataFrame(np.random.randn(4, 3), columns = ['a', 'b', 'c']) #A partir de un array 
print (fd) #Con valores generados aleatoriamente con NumPy

dataf = pd.read_csv('ModalidadVirtual.csv') #Leyendo un csv
dataf

dataf['carrera'][0]

dataf['edad'] > 25 #Buscar datos puntuales en el csv

filtrar = dataf['edad'] > 25 #Filtrar datos en el csv
dataf_filtrar = dataf[filtrar]
dataf_filtrar

#Atributos de un DataFrame:
dataf.head(10) #Primeras filas
dataf.tail(10) #Últimas filas