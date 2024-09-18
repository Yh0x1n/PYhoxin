'''
Reto 003: Fibonacci

Escribe un programa que genere los 50 primeros números de la secuencia de Fibonacci
empezando en 0.
'''

#Esto se realizará usando una función recursiva
def fibonacci(n):
    match(n):
        case 0:
            return 0
        case 1:
            return 1
        case _:
            return fibonacci(n-1) + fibonacci(n-2)

for i in range(0, 50):
    print(fibonacci(i))