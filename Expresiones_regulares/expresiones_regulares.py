import re

texto= '''hola,hola por dos
jola xd 2.
adios  tres 312.'''

#haciendo una busqueda simple

resultado = re.findall("jola",texto)

#\d -> busca digitos numeros del 0 - 9
#resultado = re.findall(r"\d",texto)

#\D -> busca TODO menos numeros del 0 - 9
resultado = re.findall(r"\D",texto)

#\w -> busca caracteres alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\w",texto)

#\W -> busca caracteres TODO menos alfanumericos [a-z A-Z 0-9 _]
resultado = re.findall(r"\W",texto)

#\s -> busca espacios en blanco y tabs
resultado = re.findall(r"\s",texto)


#\S -> busca TODO menos espacios en blanco y tabs
resultado = re.findall(r"\S",texto)

#\. -> busca TODO menos saltos en linea
resultado = re.findall(r"\.",texto)

#\n -> busca saltos en linea
resultado = re.findall(r"\n",texto)

#\ -> cancelar caracteres especiales (todos los que no son alfanumericos) cancelando la funcion del punto y buscando puntos
resultado = re.findall(r"\.",texto)

#armando una cadena que busque un numero, seguido de un punto y espacio
resultado = re.findall(f'\d\.\s',texto)

#busca el principio de una linea
#^ -> busca el comienzo de una linea 
resultado = re.findall(f"^hola",texto)

#busca el final de una linea
#$ -> busca el termino de una linea 
resultado = re.findall(r"dos$",texto,flags=re.M)

#{n} -> busca n cantidad de veces el valor de la izquierda (3 numeros juntos esta vez)
resultado = re.findall(r"\d{3}",texto)

#{n,m} -> al menos (n), como maximo (m)
resultado = re.findall(r"\d{1,4}",texto)

print(resultado)