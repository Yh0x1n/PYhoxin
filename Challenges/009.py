"""
Reto 009: Decimal a binario

Crea una función que convierta un número decimal en binario.
Sin utilizar funciones propias del lenguaje que lo resuelva.
"""

def dectobin(bin):
    match (bin):
        case 0:
            return '0'
        case 1:
            return '1'
        case _:
            return dectobin(bin // 2) + str(bin % 2)

x = int(input("Ingresa un número decimal: "))
print(dectobin(x))