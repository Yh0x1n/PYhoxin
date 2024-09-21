"""
Reto 007: Invirtiendo cadenas

Crea un programa que invierta el orden de una cadena de texto
sin usar funciones del lenguaje que lo haga de forma automática
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""


def inverted_string(word):
    return f"Palabra ingresada: {word}\n\nPalabra invertida: {word[::-1]}"

x = input("Escriba la palabra a invertir: ")
print(inverted_string(x))