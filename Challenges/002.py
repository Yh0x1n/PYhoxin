'''
Reto 002: ¿Es un anagrama?

Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
'''

def es_anagrama(palabra_1, palabra_2):
    match(palabra_1, palabra_2):
        case palabra_1, palabra_2 if sorted(palabra_1) == sorted(palabra_2):
            return True
        case palabra_1, palabra_2 if sorted(palabra_1) != sorted(palabra_2):
            return "No son anagramas"
        case palabra_1, palabra_2 if len(palabra_1) != len(palabra_2):
            return "No tienen la misma longitud"
        case _:
            return False

a = input("Palabra 1: ")
b = input("Palabra 2: ")

print(es_anagrama(a, b))