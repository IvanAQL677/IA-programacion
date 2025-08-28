def calcular_edad(anio_nacimiento, anio_actual):
    edad = anio_actual - anio_nacimiento
    return edad
anio = 2025

anio_nacimiento = int(input('Ingrese su año de nacimiento: '))
edad = calcular_edad(anio_nacimiento, anio)
print(f'Usted tiene {edad} años.')