def convertir_minutos(minutos):
    horas = minutos // 60
    sobrante = minutos % 60
    return horas, sobrante

minutos = int(input('Ingrese una cantdidad de minutos: '))
horas_totales, minutos_sobrantes = convertir_minutos(minutos)
print(f'{minutos} minutos es igual a {horas_totales} horas y {minutos_sobrantes} minutos.')