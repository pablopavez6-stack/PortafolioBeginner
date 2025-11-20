import random

print(f'Ca-chi-pun'.center(31,'!'))

opciones = ['piedra', 'papel', 'tijera']

while True:
    try:
        usuario = input('\nElije "piedra", "papel", "tijera" para continuar: ').lower()

        maquina = random.choice(opciones)
        print(f'Tu elejiste: {usuario}')
        print(f'La maquina eligio: {maquina}')
        if usuario == maquina:
            print('Empate'.center(31,'!'))
        elif usuario == "piedra" and maquina == "tijera" or usuario == "papel" and maquina == "piedra" or usuario == "tijera" and maquina == "papel":
            print(f'Elegiste {usuario}. GANASTE :D'.center(31,'!'))
        else:
            print(f'Elegiste {usuario}. Perdiste:('.center(31,'!'))

        seguir = input('\n¿Quiéres lanzar de nuevo (s/n)? ').lower()
        if seguir != 's':
            print('Hasta luego!!!')
            break
    except ValueError:
        print('Solo puedes escribir una de las tres opciones. Reintenta.')

