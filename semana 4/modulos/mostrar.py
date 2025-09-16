def mostrar_catalogo(titulos, ejemplares):
    for i in range(len(titulos)):
        if titulos[i] != '':
            print(f'Slot {i+1}: {titulos[i]}. \t({ejemplares[i]} ejemplares)')

def consultar_disponibilidad(titulos, ejemplares):
    encontrado = False
    encontrar = input('Ingrese el titulo que desea encontrar: ')
    for i in range(len(titulos)):
        if titulos[i].lower() == encontrar.lower():
            if ejemplares[i] > 0:
                print(f"El titulo '{titulos[i]}' tiene {ejemplares[i]} ejemplares disponibles.")
            else:
                print(f"El titulo {titulos[i]} se encuentra en el catalogo, pero no cuenta con ejemplares disponibles.")
            encontrado = True
            break
    if not encontrado:
        print(f"El titulo {encontrar} no se encuentra en el catalogo.")

def titulos_agotados(titulos, ejemplares):
    vacios = [False] * 20
    for i in range(len(titulos)):
        if titulos[i] != '':
            if ejemplares[i] < 1:
                vacios[i] = True
    print(f"Los articulos agotados son: ")
    for i in range(len(vacios)):
        if vacios[i]:
            print(f"'{titulos[i]}'. \t(Slot {i+1})")