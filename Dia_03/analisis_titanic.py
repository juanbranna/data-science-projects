import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
df = pd.read_csv(url)

#print(df.info())
#print(df.describe())
#print(df['Sex'].value_counts())
#print(df['Pclass'].value_counts())

# Una sola columna
#print(df["Age"])

# Varias columnas a la vez
#print(df[['Name', 'Sex', 'Survived']])

# Sólo los pasajeros que sobrevivieron
supervivientes = df[df['Survived'] == 1]
print(supervivientes.shape)

# Sólo las mujeres
mujeres = df[df['Sex'] == 'female']
print(mujeres.shape)

# Pasajeros mayores de 60 años
mayores = df[df['Age'] > 60]
print(mayores.shape)

# Mujeres que sobrevivieron
mujeres_vivas = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]
print(mujeres_vivas.shape)

# Hombres que sobrevivieron
hombres_vivos = df[(df['Sex'] == 'male') & (df['Survived'] == 1)]
print(hombres_vivos.shape)