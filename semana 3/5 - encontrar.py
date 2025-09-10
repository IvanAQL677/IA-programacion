enteros = [0] * 10

for i in range(len(enteros)):
    numero = int(input(f'Ingrese el numero #{i+1}: '))
    enteros[i] = numero

encontrar_flag = False
posicion_encontrada = 0
numero_a_buscar = int(input('Ingrese un numero para encontrar: '))
for i in range(len(enteros)):
    if enteros[i] == numero_a_buscar:
        encontrar_flag = True
        posicion_encontrada = i + 1
        break
    
if encontrar_flag:
    print(f'Su numero {numero_a_buscar} se encuentra en la posicion {posicion_encontrada}.')
else:
    print(f'Su numero {numero_a_buscar} no se encontro en el array.')