enteros = [0] * 7
mayor_actual = 0
mayor_posicion = 1
primer_flag = False
for i in range(len(enteros)):
    numero = int(input(f'Ingrese el numero #{i+1}: '))
    enteros[i] = numero

for i in range(len(enteros)):
    if not primer_flag:
        mayor_actual = enteros[i]
        primer_flag = True
    else:
        if enteros[i] > mayor_actual:
            mayor_actual = enteros[i]
            mayor_posicion = i+1

print(f'El mayor de sus numeros es {mayor_actual} en la posicion {mayor_posicion}')