import modulos.cargas as carga
import modulos.mostrar as mostrar
titulos = [''] * 20
ejemplares = [0] * 20

ayuda = '1) Cargar titulares y ejemplares \n2) Mostrar catalogo completo \n3) Consultar disponibilidad \n4) Listar titulos agotados \n5) Agregar un titulo nuevo \n6) Actualizar ejemplares \n7) Salir'

while True:
    opcion = input('Elija una opcion (H para ayuda): ')
    if opcion == '1':
        titulos, ejemplares = carga.cargar_titulos(titulos, ejemplares)
    elif opcion == '2':
        mostrar.mostrar_catalogo(titulos, ejemplares)
    elif opcion == '3':
        mostrar.consultar_disponibilidad(titulos, ejemplares)
    elif opcion == '4':
        mostrar.titulos_agotados(titulos, ejemplares)
    elif opcion == '5':
        titulos, ejemplares = carga.agregar_uno(titulos, ejemplares)
    elif opcion == '6':
        ejemplares = carga.actualizar_ejemplares(titulos, ejemplares)
    elif opcion == '7':
        break
    elif opcion.lower() == 'h':
        print(ayuda)