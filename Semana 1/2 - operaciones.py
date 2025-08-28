def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2
    print(f'{num1} + {num2} = {suma} \n{num1} - {num2} = {resta} \n{num1} * {num2} = {multiplicacion}')

numero_1 = int(input('Por favor ingrese un numero: '))
numero_2 = int(input('Por favor ingrese otro numero: '))
operaciones(numero_1, numero_2)