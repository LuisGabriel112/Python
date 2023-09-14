#Creando una lista con list
lista = list([5,1,34,1245])

#Nos devuelve la cantidad de elementos en una lista
cantidad_de_elementos = len(lista)

#agrega un elemento a la lista
lista.append("JAJAJAJ")

#agregando un elemento a la lista con un indice especifico
lista.insert(2,"xd")

#agregando varios elementos a la lista
lista.extend([False,2])

#eliminando un elemento de la lista por el indice
lista.pop(0) #si pones -1 se elemina el ultimo elemento de la lista

#Removiendo un elemnto de la lista por su valor
lista.remove("xd")

#ordenando la lista (si usamos el valor reverse=True lo ordena en reversa)
#lista.sort(reverse=True)

#invierte los elementos de una lista
lista.reverse()

#eliminando todos los elemntos de la lista
lista.clear()
print(lista)