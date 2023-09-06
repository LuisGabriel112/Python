import pandas as pd
#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")

#Obteniendo los datos de la columna nombre
nombres = df["Edad"]

#Slicing

"""cadena = '0123456789'
Del lado izquierdo de los dos puntos tenemos que señalar el valor por 
donde empieza a tomarse el slice, del lado derecho es donde termina 
Si lo dejamos vacio recorre todo
print(cadena[:])"""

#ordenando el dataframe por la edad

df_ordenado = df.sort_values("Edad")

#ordenando de forma descendente
df_desordenado = df.sort_values("Edad",ascending=False)

#concatenando los df
df_concatenado = pd.concat([df,df2])

#Accediendo a la primer fila con head()

primer_fila = df.head(1)

#accediendo a las ultimas filas con tail()
ultimas_filas = df.tail(2)

#accediendo a la cantidad de filas y columnas con shape

filas_totales, columnas_totales = df.shape

#obteniendo data estadistica del dataFrame

df_info = df.describe()

#accediendo a un elemento especifico del dataframe con loc

elemento_especifico = df.loc[0,"Nombre"]

#accediendo a un elemento especifico del dataframe con iloc
elemento_especifico = df.iloc[0,1]

#accediendo a todas las filas de una columna
edades = df.iloc[:,1]

#accediendo a las filas con edad mayor a 10
edades_mayor = df.loc[df['Edad']>10,:]
print(edades_mayor)