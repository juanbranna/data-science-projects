import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

# ¿Cuántos pasajeros había en total?
print(df.info())

pasajeros_totales = df['PassengerId'].shape[0]
print(pasajeros_totales.shape)

# ¿Cuántos sobrevivieron y cuántos murieron?
print(df.describe())
vivos = df[df['Survived'] == 1]
muertos = df[df['Survived'] == 0]
print(vivos.shape)
print(muertos.shape)

# ¿Cuál era la edad media de los pasajeros?
#print(df.describe())
edad_media_pasajeros = (df['Age'].mean())
print(edad_media_pasajeros)

#¿Cuántos viajaban en cada clase?
viajeros_por_clase = (df['Pclass'].value_counts())
print(viajeros_por_clase)

# ¿Cuál fue la tasa de supervivencia de los niños (menores de 16 años)?
niños_menores_16 = (df['Age'] < 16).sum()
supervivientes_menores_de_16 = ((df['Age'] < 16) & (df['Survived'] == 1)).sum()
print(df['Survived'].value_counts())
porcentaje = (supervivientes_menores_de_16 / niños_menores_16) * 100
print(f'Tasa de supervivencia en niños: {porcentaje:.2f}%')


# ¿Cuál era el precio medio del billete en primera clase vs tercera clase?
precio_medio_primera_clase = df[df['Pclass'] == 1]['Fare'].mean()
precio_medio_tercera_clase = df[(df['Pclass'] == 3)]['Fare'].mean()
print(f'Precio medio tercera clase: {precio_medio_tercera_clase:.2f}')
print(f'Precio medio primera clase: {precio_medio_primera_clase:.2f}')