costos = 0
montaña_usos = 0
terror_usos = 0
carrusel_usos = 0

montaña_permitido = False
terror_permitido = False


nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
while edad < 0 or edad > 110:
    edad = int(input('Edad invalida. Intentelo de nuevo.\nIngrese su edad: '))
cantidad_a_usar = int(input('Ingrese la cantidad de atracciones que visitara: '))
while cantidad_a_usar < 1:
    cantidad_a_usar = int(input('Opcion invalida.\nIngrese la cantidad de atracciones que visitara (Maximo de 3): '))

if edad > 6 and edad < 13:
    terror_permitido = True
elif edad > 12:
    terror_permitido = True
    montaña_permitido = True

lista_opciones = '1) Montaña rusa.\n2) Casa del terror.\n3) Carrusel.\n0) Salir\n'

while cantidad_a_usar != 0:
    opcion = input('Elija la atraccion que desea subir ahora ("ayuda" para ver la lista de comandos):\n')
    if opcion == '0':
        break
    elif opcion == 'ayuda':
        print(lista_opciones)
    elif opcion == '1':
        confirmar = input('Va a subir a la montaña rusa ($1500). Esta seguro? (si/no)\n')
        if confirmar != 'si':
            continue
        if montaña_permitido:
            costos += 1500
            montaña_usos += 1
            cantidad_a_usar -= 1
        else:
            print('No tiene permitido usar la montaña rusa.')

    elif opcion == '2':
        confirmar = input('Va a entrar a la casa del terror ($1200). Esta seguro? (si/no)\n')
        if confirmar != 'si':
            continue
        if terror_permitido:
            costos += 1200
            terror_usos += 1
            cantidad_a_usar -= 1
        else:
            print('No tiene permitido usar la casa del terror.')

    elif opcion == '3':
        confirmar = input('Va a subir al carrusel ($800). Esta seguro? (si/no)\n')
        if confirmar != 'si':
            continue
        costos += 800
        carrusel_usos += 1
        cantidad_a_usar -= 1

    else:
        print('Opcion no valida.')

print(f'Nombre: {nombre} \nGastos: {costos}')
print('Attraciones habilitadas:')
if edad < 6:
    print('Carrusel')
elif edad > 5 and edad < 13:
    print('Carrusel,\nCasa del terror')
else:
    print('Carrusel,\nCasa del terror,\nMontaña rusa')
if montaña_usos > 0:
    print(f'Visitas a la montaña rusa: {montaña_usos}')
if terror_usos > 0:
    print(f'Visitas a la casa del terror: {terror_usos}')
if carrusel_usos > 0:
    print(f'Visitas al carrusel: {terror_usos}')
if cantidad_a_usar > 0:
    print(f'Pases sin usar: {cantidad_a_usar}')