print('*** Calcular IMC ***')


def calcularIMC():
    IMC = peso / ((altura/100) ** 2)
    return IMC

peso = float(input('¿Cuál es tu peso (KG)? '))
altura = float(input('¿Cuál es tu altura (CM)? '))

print(f'''Tus datos:
    Tu altura corresponde a: {altura}
    Tu peso corresponde a: {peso}
    Tu indice de masa corporal (IMC) es: {calcularIMC():.2f}''')
