import os
def f(o, x, y):
    match o:
        case 1:
            return x+y
        case 2:
            return x-y
        case 3:
            return x*y
        case 4:
            return x/y

while True:
    try:
        os.system('clear')
        op = int(input("Ingrese la operación que desee realizar.\n"
                       "1. Suma\n"
                       "2. Resta\n"
                       "3. Multiplicación\n"
                       "4. División\n"
                       "5. Salir\n\n"
                       "->"))
        try:
            os.system('clear')
            match op:
                case 1:
                    a, b = int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))
                    print(f"El resultado es {f(op, a, b)}")
                case 2:
                    a, b = int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))
                    print(f"El resultado es {f(op, a, b)}")
                case 3:
                    a, b = int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))
                    print(f"El resultado es {f(op, a, b)}")
                case 4:
                    try:
                        a, b = int(input("Ingrese un número: ")), int(input("Ingrese otro número: "))
                        print(f"El resultado es {f(op, a, b)}")
                    except ZeroDivisionError:
                        print("No se puede dividir entre 0")
                case 5:
                    print("Programa terminado")
                    break
                case _:
                    print("Ingrese la opción correcta.")
        except ValueError:
            print("Valor incorrecto.")
        finally:
            input("Pulsa Enter para continuar...")
    except ValueError:
        print()