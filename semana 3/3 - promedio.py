flotantes = [0.0] * 6
acumulacion = 0
for i in range(len(flotantes)):
    flotantes[i] = float(input(f'Ingrese el numero #{i+1}: '))
    acumulacion += flotantes[i]
promedio = acumulacion / 6
print(f'El promedio de los numeros es {promedio}')