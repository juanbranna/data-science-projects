import numpy as np

def clasificar_nota(nota):
    if nota >= 5:
        return 'Aprobado'
    else:
        return 'Suspenso'

def analisis_completo(notas):
    print(f'Media: {np.mean(notas):.2f}')
    print(f'Desviación estándar: {np.std(notas):.2f}')
    
    notas_aprobadas = [n for n in notas if n>= 5]
    numero_aprobados = len(notas_aprobadas)
    numero_suspensos = len(notas) - len(notas_aprobadas)
    print(f'Aprobados: {numero_aprobados}')
    print(f'Suspensos: {numero_suspensos}')
    clasificaciones = [clasificar_nota(n) for n in notas]
    print(f'Clasificaciones: {clasificaciones}')
notas = [6, 3, 5, 5, 7, 8, 3, 5, 8, 10, 10, 4]
analisis_completo(notas)

#clasificar_nota(notas)