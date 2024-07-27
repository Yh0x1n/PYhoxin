#Pandas 3: Excel a CSV

import pandas as pd

convertir = pd.read_excel('datos.xls')

convertir.to_csv('datos.csv', index = None, header = True)