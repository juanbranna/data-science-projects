import numpy as np
notas = np.array([6, 8, 4, 9, 7, 5, 10, 3])
print(notas)
print(type(notas))

#print(f'Media: {np.mean(notas):.2f}')
print(f'Desviación estándar: {np.std(notas):.2f}')
print(f'Mínimo: {np.min(notas)}')
print(f'Máximo: {np.max(notas)}')

notas_normalizadas = (notas - np.mean(notas)) / np.std(notas)
print(f'Notas normalizadas: {notas_normalizadas.round(2)}')

