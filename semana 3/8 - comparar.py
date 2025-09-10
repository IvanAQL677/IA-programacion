enteros = [0] * 5
enteros_2 = [0] * 5
array_verdad = [False] * 5
todos_falsos = True
for i in range(len(enteros)):
    numero = int(input(f'Ingrese el numero #{i+1} para el primer array: '))
    numero_2 = int(input(f'Ingrese el numero #{i+1} para el segundo array: '))
    enteros[i] = numero
    enteros_2[i] = numero_2

for i in range(len(enteros)):
    if enteros[i] == enteros_2[i]:
        array_verdad[i] = True
    else:
        array_verdad[i] = False

print('Las siguientes posiciones en cada array son iguales: ')
for i in range(len(enteros)):
    if array_verdad[i]:
        print(f'La posicion #{i+1}. ({enteros[i]} y {enteros_2[i]}).')
        todos_falsos = False
if todos_falsos:
    print('Ninguna posicion coincide.')