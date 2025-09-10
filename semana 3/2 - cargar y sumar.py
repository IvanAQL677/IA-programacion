enteros = [0] * 10
acumulacion_total = 0
for i in range(len(enteros)):
    numero = int(input(f'Ingrese numero #{i+1}: '))
    enteros[i] = numero
        
for i in range(len(enteros)):
    acumulacion_total += enteros[i]
print(f'Suma de todos los numeros: {acumulacion_total}')