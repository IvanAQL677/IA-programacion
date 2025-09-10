enteros = [0] * 6
enteros_malvado = [0] * 6
for i in range(len(enteros)):
    numero = int(input(f'Ingrese el numero #{i+1}: '))
    enteros[i] = numero
    enteros_malvado[len(enteros)-i-1] = numero

print(f'Su array es {enteros}. \nSu inverso es {enteros_malvado}.')