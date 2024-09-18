'''
Reto 001: Fizz Buzz

Escribir un programa que miestre por consola (Con un print()) los números del 1 al 100
(ambos incluidos y con un salto de línea en cada impresión), sustituyendo los siguientes:

- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y 5 a la vez por la palabra "fizzbuzz".
'''

for i in range (1, 101):
    match(i):
        case i if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        case i if i % 3 == 0:
            print("fizz")
        case i if i % 5 == 0:
            print("buzz")
        case _:
            print(i)