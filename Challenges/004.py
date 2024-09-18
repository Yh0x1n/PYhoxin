'''
Reto 004: ¿Es un número primo?

Escribe un programa que se encargue de comprobar si un número es
o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
'''

def es_primo():
    for i in range (2, 100):
      match (True): 
        case True:
            for j in range (2, i):
               match (j):
                  case j if i % j == 0: 
                     break
                  case j if j == i - 1:
                     print(i)
es_primo()