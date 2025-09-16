def cargar_titulos(titulos, ejemplares):
    print('Esta en modo carga. Cargue 20 items o ingrese "Salir" para finalizar antes de tiempo. Deje un slot vacio para no modificarlo.')
    for i in range(len(titulos)):
        titulo = input(f'Ingrese titulo #{i+1}: ')
        if titulo.lower() == 'salir':
            print('Carga finalizada antes de tiempo')
            return titulos, ejemplares
        if titulo == '':
            titulos[i] = titulos[i]
            ejemplares[i] = ejemplares[i]
            continue
        ejemplar = int(input('Ingrese numero de ejemplares: '))
        titulos[i] = titulo
        ejemplares[i] = ejemplar

def agregar_uno(titulos, ejemplares):
    espacio_libre = 0
    bandera_libre = False
    for i in range(len(titulos)):
        if titulos[i] == '':
            espacio_libre = i
            bandera_libre = True
            break
    if bandera_libre:
        nuevo_titulo = input('Ingrese el nuevo titulo a agregar: ')
        nuevo_ejemplar = int(input('Ingrese la cantidad de ejemplares para agregar: '))
        titulos[espacio_libre] = nuevo_titulo
        ejemplares[espacio_libre] = nuevo_ejemplar
        return titulos, ejemplares
    else:
        print('Error: Maximo de titulos en el catalogo alcanzado.')

def actualizar_ejemplares(titulos, ejemplares):
    titulo = input('Ingrese el titulo que desea modificar: ')
    objectivo = -1
    for i in range(len(titulos)):
        if titulos[i] == titulo:
            objectivo = i
    if objectivo < 0:
        print('Titulo no encontrado.')
    else:
        ejemplares_nuevo = int(input(f"Ingrese la nueva cantidad de ejemplares para '{titulos[objectivo]}': "))
        ejemplares[objectivo] = ejemplares_nuevo
        return ejemplares