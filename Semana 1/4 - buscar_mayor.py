def buscar_mayor(num1, num2, num3):
        if num1 > num2 and num1 > num3:
                if num2 > num3:
                        return num1, num2, num3
                else:
                        return num1, num3, num2
        
        elif num2 > num1 and num2 > num3:
                if num1 > num3:
                        return num2, num1, num3
                else:
                        return num2, num3, num1
        elif num3 > num1 and num3 > num2:
                if num1 > num2:
                        return num3, num1, num2
                else:
                        return num3, num2, num1

numero_1 = int(input('Ingrese el primer numero: '))
numero_2 = int(input('Ingrese el segundo numero: '))
numero_3 = int(input('Ingrese el tercer numero: '))

menor_1, menor_2, mayor = buscar_mayor(numero_1, numero_2, numero_3)
print(f'De menor a mayor, los numeros son {menor_1}, {menor_2} y {mayor}.')