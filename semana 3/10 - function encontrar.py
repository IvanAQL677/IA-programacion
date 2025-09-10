
def encontrar(numero:int, array):
    for i in range(len(array)):
        if array[i] == numero:
            return i+1
    
    return -1
        

enteros = [0] * 10
for i in range(len(enteros)):
    numero = int(input(f'Ingrese el numero #{i+1}: '))
    enteros[i] = numero

numero_a_encontrar = int(input('Ingrese un numero para encontrar: '))
posicion = encontrar(numero_a_encontrar, enteros)
if posicion == -1:
    print('No se encontro su numero en el array.')
else:
    print(f'La primera instancia de su numero se encontro en la posicion {posicion}.')