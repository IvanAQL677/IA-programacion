def es_par(num):
    if num % 2 == 0:
        return True
    else:
        return False

numero = int(input('Ingrese un numero: '))
par_o_no = es_par(numero)

if par_o_no:
    print(f'El numero {numero} es par.')
else:
    print(f'El numero {numero} es impar.')