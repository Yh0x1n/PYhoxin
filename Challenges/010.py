"""
Reto 010: Código morse

Crea una función que convierta un texto en código morse y viceversa.
- Debe detectar automáticamente de qupe tipo se trata y realizar la conversión.
- En morse se soporta raya "-", punto "." y un espacio " " entre letras.
- El alfabeto morse se puede encontrar en https://es.wikipedia.org/wiki/Alfabeto_morse
"""

def texto_a_morse(texto_normal):
    mc = {
        'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..',
        'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---',
        'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.',
        'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--',
        'x' : '-..-', 'y' : '-.--', 'z' : '--..', '1' : '.----', '2' : '..---', '3' : '...--',
        '4' : '....-', '5' : '.....', '6' : '-....', '7' : '--...', '8' : '---..', '9' : '----.',
        '0' : '-----', ' ':' ', '.' : '.-.-.-', ',' : '--..--', '?' : '..--..', '!' : '-.-.--',
        '/' : '-..-.', '(' : '-.--.', ')' : '-.--.-', '&' : '.-...', ':' : '---...', ';' : '-.-.-.',
        '=' : '-...-', '+' : '.-.-.', '-' : '-....-', '$' : '...-..-', '@' : '.--.-.'
    }

    if type(texto_normal) == str:
        texto_morse = ""
        for i in texto_normal.lower():
            texto_morse += mc[i] + " "
        return texto_morse
    else:
        raise TypeError

def morse_a_texto(morse_code):
    mc = {
        '.-' : 'a', '-...' : 'b', '-.-.' : 'c', '-..' : 'd',
        '.' : 'e', '..-.' : 'f', '--.' : 'g', '....' : 'h', '..' : 'i', '.---' : 'j',
        '-.-' : 'k', '.-..' : 'l', '--' : 'm', '-.' : 'n', '---' : 'o', '.--.' : 'p',
        '--.-' : 'q', '.-.' : 'r', '...' : 's', '-' : 't', '..-' : 'u', '...-' : 'v',
        '.--' : 'w', '-..-' : 'x', '-.--' : 'y', '--..' : 'z', '.----' : '1', '..---' : '2',
        '...--' : '3', '....-' : '4', '.....' : '5', '-....' : '6', '--...' : '7', '---..' : '8',
        '----.' : '9', '-----' : '0', ' ' : ' ', '.-.-.-' : '.', '--..--' : ',', '..--..' : '?',
        '-.-.--' : '!', '-..-.' : '/', '-.--.' : '(', '-.--.-' : ')', '.-...' : '&', '---...' : ':',
        '-.-.-.' : ';', '-...-' : '=', '.-.-.' : '+', '-....-' : '-', '...-..-' : '$', '.--.-.' : '@',
    }

    if type(morse_code) == str:
        morse_texto = ""
        for i in morse_code.split():
            morse_texto += mc[i] + " "
        return morse_texto
    else:
        raise TypeError

x = int(input("Ingresa una opción para convertir:\n1- Texto a Código morse\n2- Código morse a Texto\n->"))
match (x):
    case 1:
        print(texto_a_morse(input("Ingresa el texto a convertir:\n->")))
    case 2:
        print(morse_a_texto(input("Ingresa el código morse a convertir:\n->")))