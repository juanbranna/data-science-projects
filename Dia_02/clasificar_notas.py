def clasificar_nota(nota):
    if nota >= 9:
        return 'Sobresaliente'
    elif nota >= 7:
        return 'Notable'
    elif nota>= 5:
        return 'Aprobado'
    else:
        return 'Suspenso'
print(clasificar_nota(7))
notas = [6, 8, 4, 9, 7, 5, 10, 3]

clasificaciones = [clasificar_nota(n) for n in notas]

#print(clasificaciones)

for i, calificacion in enumerate(clasificaciones):
    print(f'Alumno {i+1}: {calificacion}')
#clasificaciones = [clasificar_nota(n) for n in notas]
#print(clasificaciones)