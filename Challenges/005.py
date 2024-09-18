'''
Reto 005: Área de un polígono

Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.

- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.
'''

import os
def area(pol):
    #Se calcula el tamaño del polígono
    match(pol):
        case 1:
            os.system('clear')
            base = int(input('¿De cuántos cm es la base?\n->'))
            height = int(input('¿De cuántos cm es la altura?\n->'))

            os.system('clear')
            res = (base * height) / 2
            print (f'El área del triángulo es {res}')

        case 2:
            os.system('clear')
            lado = int(input('¿De cuántos cm son los lados?\n->'))

            os.system('clear')
            res = lado * lado
            print (f'El área del cuadrado es {res}')
        
        case 3:
            os.system('clear')
            width = int(input('¿Cuántos cm mide de ancho?\n->'))
            height = int(input('¿Cuántos cm mide de alto?\n->'))

            os.system('clear')
            res = (width * height)
            print (f'El área del rectángulo es {res}')
        
        case _:
            pass

menu = int(input('¿Qué área quieres calcular?\n'
                 '1- Triángulo\n'
                 '2- Cuadrado\n'
                 '3- Rectángulo\n'
                 '->'))
area(menu)