import gestion_parque.parque as parque

atracciones_usadas = 0
costo_total = 0

print('Bienvenido a Pythonland!')
nombre = input('Para iniciar, ingrese su nombre: ')
edad = int(input('Ahora ingrese su edad: '))

while True:
    if atracciones_usadas > 0:
        resumen_actual = parque.registrar_visita(nombre, edad, atracciones_usadas, costo_total)
        opcion = input('Elija un numero para subir a otra atraccion (0 para ver la lista de atracciones, "salir" para salir) \n')
    else:
        opcion = input('Elija un numero para subir a una atraccion (0 para ver la lista de atracciones, "salir" para salir) \n')

    if opcion == '0':
        parque.mostrar_atracciones()

    elif opcion == 'salir':
        print('Gracias, vuelva pronto!')
        if atracciones_usadas > 0:
            parque.registrar_visita(nombre, edad, atracciones_usadas, costo_total)
        break

    elif opcion == '1':
        puede_subir = parque.puede_subir(edad, 'montaña rusa')
        if puede_subir:
            confirmar = input('Va a subir a la montaña rusa (Costo: $1500). Esta seguro? (si para confirmar) \n')
            if confirmar == 'si':
                atracciones_usadas = atracciones_usadas + 1
                costo = parque.calcular_precio('montaña rusa', atracciones_usadas)
                costo_total = costo_total + costo
                print('Usted se subio a la montaña rusa y se divirtio.')
        else:
            print('Usted no puede subir a la montaña rusa.')

    elif opcion == '2':
        puede_subir = parque.puede_subir(edad, 'casa del terror')
        if puede_subir:
            confirmar = input('Va a subir a la casa del terror (Costo: $1200). Esta seguro? (si para confirmar) \n')
            if confirmar == 'si':
                atracciones_usadas = atracciones_usadas + 1
                costo = parque.calcular_precio('casa del terror', atracciones_usadas)
                costo_total = costo_total + costo
                print('Usted se subio a la casa del terror y se divirtio.')
        else:
            print('Usted no puede subir a la casa del terror.')

    elif opcion == '3':
        puede_subir = parque.puede_subir(edad, 'carrusel')
        if puede_subir:
            confirmar = input('Va a subir al carrusel (Costo: $800). Esta seguro? (si para confirmar) \n')
            if confirmar == 'si':
                atracciones_usadas = atracciones_usadas + 1
                costo = parque.calcular_precio('carrusel', atracciones_usadas)
                costo_total = costo_total + costo
                print('Usted se subio al carrusel y se divirtio.')
        else:
            print('Usted aun no ha nacido.')

if atracciones_usadas > 0:
    ver_el_resumen = input('Desea ver su resumen? (si/no): ')
    if ver_el_resumen == 'si':
        parque.mostrar_resumen(resumen_actual)