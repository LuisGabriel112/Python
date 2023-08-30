#creando diccionarios con dict() (Podemos crear diccionarios vacios con esta funcion*(funciona igual con listas tuplas y sets))
#diccionario = dict(nombre = "Luis", apellido = "Venegas")

#otra forrma de crear diccionarios
""" {
    nombre : "Luis",
    apellido : "Venegas" 
} """

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Dalto","Rancio"]):"jjasj"}

#creando diccionario con fromkeys() (Nos crea cualquier dato None)
diccionario = dict.fromkeys(["nombre","apellido"])

#creando diccionarios con fromkeys() cambiando el valor a "No se"
diccionario = dict.fromkeys(["nombre","apellido"],"No se")

print(diccionario)