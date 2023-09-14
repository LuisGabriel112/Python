#Abriendo el archivo con with open
with open("archivos\\texto.txt",encoding="UTF-8") as archivo:
    #Leemos el archivo
    contenido = archivo.readlines()
    #mostramos el archivo
    print(contenido)

#No es necesario cerrarlo al usar with open