import random

print(f'Lanzador de dados'.center(31, '-'))

while True:
    input('\nPresione Enter para continuar...')
    numero = random.randint(1, 6)
    print(f'Salio el numero {numero}\n')

    seguir = input('¿Quiéres lanzar de nuevo (s/n)? ').lower()
    if seguir != 's':
        print('Hasta luego!!!')
        break