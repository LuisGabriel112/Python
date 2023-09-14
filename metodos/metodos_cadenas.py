cadena1 = "Hola,soy,Luis"
cadena2 = "Hola soy xd"
#print(dir(cadena1))#dir: Nos muestra todo lo que podemos hacer con 
#el objeto que le pasamos

Resultado = cadena1.upper()#Pasa todo a mayusculas

ResultadoMinus = cadena1.lower()#Pasa todo a minusculas

ResultadoCap = cadena1.capitalize()#Pasa la primer letra a mayuscula

busqueda_find = cadena1.find("Hola")#devuelve la posicion en la que encuentra
#lo que nosotros le pedimos si no hay resultados devuelve -1

busqueda_find = cadena1.find("Hola")#funciona igual que find es que
#si no encuentra nada lanza una excepcion

#si es numerico, devolvemos true, sino devolvemos false
es_numerico = cadena1. isnumeric()

#si es alfanumèrico devolvemos true, sino devolvemos false
es_alfanumerico = cadena1.isalpha()

#contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad
#de coincidencias
contar_coincidencias = cadena1. count("D")

#contamos la cantidad de caracteres que tiene una cadena
cantidadDeCaracteres = len(cadena1)

#Verificamos si una cadena empieza con otra cadena dada si es asi devuelve true
Empieza_con = cadena1.startswith("Hola")

#Verificamos si una cadena termina con otra cadena dada si es asi devuelve true
Termina_con = cadena1.endswith("s")

#si el valor 1, se encuentra en la cadena original, remplaza el valor 1 de la misma, por el valor 2
CadenaNueva = cadena1.replace("la", "lu")

#Separa cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")

print(cadena_separada)