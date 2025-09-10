enteros = [0] * 10
for i in range(len(enteros)):
    numero = int(input(f'Ingresar el numero #{i+1}: '))
    enteros[i] = numero
    if enteros[i] % 2 == 0:
        enteros[i] = 0

print(f'Su array final con los numeros pares redactados es: {enteros}')