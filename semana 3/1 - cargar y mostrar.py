enteros = [0] * 5
for i in range(len(enteros)):
    numero = int(input(f'Ingrese numero #{i+1}: '))
    enteros[i] = numero

for i in range(len(enteros)):
    print(f'Numero #{i+1}: {enteros[i]}')