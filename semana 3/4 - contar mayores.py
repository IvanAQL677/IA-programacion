enteros = [0] * 8
mayores = 0
for i in range(len(enteros)):
    numero = int(input(f'Ingrese el numero #{i+1}: '))
    if numero > 100:
        mayores += 1
    enteros[i] = numero

print(f'Un total de {mayores} numeros son mayores a 100, incluyendo:')
for i in range(len(enteros)):
    if enteros[i] > 100:
        print(enteros[i])