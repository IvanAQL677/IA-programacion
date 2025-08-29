def mostrar_atracciones():
    print('1) Montaña rusa ($1500)\n2) Casa del terror ($1200)\n3) Carrusel ($800)')

def puede_subir(edad, atraccion):
    if atraccion == 'carrusel':
        edad_minima = 0
    elif atraccion == 'casa del terror':
        edad_minima = 6
    elif atraccion == 'montaña rusa':
        edad_minima = 13
    
    if edad >= edad_minima:
        return True
    else:
        return False

def calcular_precio(atraccion, atracciones_usadas):
    if atraccion == 'carrusel':
        precio = 800
    elif atraccion == 'casa del terror':
        precio = 1200
    elif atraccion == 'montaña rusa':
        precio = 1500

    if atracciones_usadas >= 3:
        precio = precio - (precio * 0.10)
        print(f'Costos de esta visita: ${precio} (10% de descuento!)')
    else:
        print(f'Costos de esta visita: ${precio}.')
    
    return precio

def registrar_visita(nombre, edad, atracciones, costo):
    resumen_actual = f'Nombre: {nombre} \nEdad: {edad} \nAtracciones a las que se subio: {atracciones} \nCosto total de su visita: {costo}'
    return resumen_actual

def mostrar_resumen(resumen):
    print(resumen)
