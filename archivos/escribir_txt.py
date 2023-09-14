

with open ('archivos\\texto.txt','w', encoding='UTF-8') as archivo:
    #sobre escribiendo el archivo 'archivo.write("xd2")'
    for x in range (3):
        archivo.writelines('hola \n')
    