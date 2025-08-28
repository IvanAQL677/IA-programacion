def area_triangulo(base, altura):
    resultado = (base * altura) / 2
    return resultado

base = int(input('Ingrese el area de un triangulo: '))
altura = int(input('Ingrese la altura de un triangulo: '))
resultado = area_triangulo(base, altura)
print(f'El area de su triangulo es de {resultado}.')