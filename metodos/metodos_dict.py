diccionario = {
    "nombre": 'luis',
    "Apellido": 'Venegas',
    "subs": 6
}

#Devuelve las claves de los diccionarios
claves = diccionario.keys()

#Devuelve el valor de la clave que consultemos
tomar = diccionario.get("nombre") 

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
#diccionario.pop("nombre")

#obteniendo un elemento dict_items iterable
dict_iterable = diccionario.items()

print(dict_iterable)