#Listas
lista = ["Luis Gabriel",True,1.70,"xd"]
lista[3] = "maquinola"
print(lista[3])

#tuplas
#La diferencia con las listas es que no se pueden modificar los
#valores ya establecidos
tupla = ("Luis Gabriel",True,1.70,"xd")
print (tupla[0])
#tupla[3] = "maquinola"

#conjunto (set)
"""
La diferencia con las listas y las tuplas es que no se puede
acceder a un indice en especifico y no te deja repetir elementos

"""
conjunto = {"Luis Gabriel","Hola", True,1.2}
#print(conjunto[3]) -> no puede acceder al elemento

#Diccionario
#creando un diccionario (dict) (la estructura es key : value y separamos con comas)

diccionario = {
    "nombre": "Luis",
    "canal" : "568 crew",
    "Esta emocionado" : True,
    "dato_duplicado" : "Luis"
}

print (diccionario['canal'])