def verificar_acceso(edad):
    if edad >= 18:
        return True
    else:
        return False
    
su_edad = int(input('Ingrese su edad: '))
resultado = verificar_acceso(su_edad)
if resultado:
    print('Usted es mayor de edad.')
else:
    print('Usted es menor de edad.')