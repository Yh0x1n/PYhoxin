"""
Reto 008: Contando palabras

Crea un programa que cuente cuantas veces se repite cada palabra y que
muestre el recuento final de todas ellas.

- Los signos de puntuación no forman parte de la palabra.
- Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
- No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
"""

def count_words(x):
    x = ''.join(c for c in x if c.isalpha() or c.isspace()).lower()
    return {word : x.count(word) for word in set(x.split())}

x = "Hola, mi nombre es brais. Mi nombre completo es Brais Moure (MoureDev)."

print(count_words(x))