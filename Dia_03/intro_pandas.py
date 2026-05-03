import pandas as pd

#Crear un DataFrame desde un diccionario
datos = {
    'nombre': ['Ana', 'Luis', 'Marta', 'Carlos'],
    'edad': [28, 34, 22, 45],
    'ciudad': ['Madrid', 'Barcelona', 'Madrid', 'Sevilla'],
    'salario': [32000, 48000, 27000, 61000]
}

df = pd.DataFrame(datos)
print(df)

print(df.head(2))      #primeras 2 filas
print(df.tail(1))      #última fila
print(df.shape)        # (filas, columnas)
print(df.columns)      # nombres de las columnas

#Cargar el dataset del Titanic directamente desde internet
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic = pd.read_csv(url)

print(titanic.shape)
print(titanic.head())
