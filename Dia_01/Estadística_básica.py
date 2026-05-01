datos = [4,8,15,17,37,38,29,19,39,34,25,36,49,78,6,5,56,78,76,74]
def calcular_media(lista):
    return sum(lista) / len(lista)

media = calcular_media(datos)
#print('Media =', media)

def calcular_std(juan):
    media = calcular_media(juan)
    varianza = sum((x - media) ** 2 for x in juan) / len(juan)
    return varianza ** 0.5

std = calcular_std(datos)
#print('Desviación estándar =', std)

def resumen_estadistico(maca):
    media = calcular_media(maca)
    std = calcular_std(maca)
    print(f'Datos = {maca}')
    print(f'Media = {media:.2f}')
    print(f'Desviación estándar: {std:.2f}')

resumen_estadistico(datos)