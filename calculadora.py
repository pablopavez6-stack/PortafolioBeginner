
def mostrar_menu():
    while True:
        try:
            print(f'Calculadora'.center(50, '-'),)
            print('''\tOperaciones
        1- Sumar
        2- Restar
        3- Multiplicacion
        4- Division
        5- Potencia
        6- Salir''')
            return int(input('Selecciona la operación a realizar: '))
        except ValueError:
            print('Por favor ingresa la opción correcta (números)\n')

def valores():
    while True:
        try:
            a = float(input('Primer número de la operación: '))
            b = float(input('Segundo número de la operación: '))
            return a, b
        except ValueError:
            print('Por favor ingresa solo números.')

def operacion(opcion, salir):
    if 1 <= opcion <= 5:
        a, b = valores()

        if opcion == 1:
            print(f'\tEl resultado de la suma de {a} + {b} es = {a + b}')
        elif opcion == 2:
            print(f'\tEl resultado de la resta de {a} - {b} es = {a - b}')
        elif opcion == 3:
            print(f'\tEl resultado de la multiplicación de {a} * {b} es = {a * b}')
        elif opcion == 4:
            if b == 0:
                print(f'No se puede dividir por 0')
            else:
                print(f'\tEl resultado de la division de {a} / {b} es = {a / b}')
        elif opcion == 5:
            print(f'\tEl resultado de la potencia de {a} ^ {b} es = {a ** b}')
    elif opcion == 6:
        print('Saliendo...')
        salir = True
    else:
        print('Opción incorrecta!!! intenta nuevamente.')
    return salir


if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = operacion(opcion, salir)