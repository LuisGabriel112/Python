#leer un archivo y codificar
archivo = open ("archivos\\texto.txt",encoding="UTF-8")
#una vez que ya se leyo no se puede volver a leer

#leer linea por linea
lineas = archivo.readlines()

#cerrando el archivo
close = archivo.close()
print(lineas)
