import random

print('*** Adivina el número ***')

print('\nAdivina el número...')
aleatorio = random.randint(1, 20)
intentos = 0
usuario = None
INTENTOS_MAX = 5

while usuario != aleatorio and intentos < INTENTOS_MAX:
    usuario = int(input('Elije tu número y acierta: '))

    if usuario < aleatorio:
        print('\tTe daré una pista, el número es mayor')
    elif usuario > aleatorio:
        print('\tCasi, pero el número es menor')
    intentos +=1

if usuario == aleatorio:
    print('Felicidades. Ganaste el número sorteado :D'.center(70,'!'))
else:
    print('Lo siento:( realizaste el máximo de intentos...')