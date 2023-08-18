animales = {"gato","perro","loro","cocodrilo"}
numeros = {1,2,3,4,}


#creando un for
#recorriendo la conjunto animales
#for animal in animales: 
    #print(f'Ahora la variable animal es {animal}')
    
    
#recorriendo la conjunto numero y multiplicando por 2=
#for numero in numeros:
   # numero *=2
    #print(numero)
    
#como iterar 2 conjuntos del mismo tamaño al mismo tiempo(for anidado)
"""

En Python, zip() es una función incorporada 
que se utiliza para combinar elementos de iterables (conjuntos, tuplas, etc.)
en pares ordenados. 
"""
for numero , animal in zip(animales,numeros):
    print(f"Recorriendo conjunto 1 {numero}")
    print(f"Recorriendo conjunto 2 {animal}")
    
#tambien se puede iterara con la funcion range
for num in range(10):
    print(num)
#diferentes usos:
for num in range(10,20):
    print(num)
    
#forma correcta de recorrer una conjunto por su inidice
#nos devuelve el indice y el valor
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f'El indice es {indice} y el valor es {valor}')
    
#usando el else (siempre se van a ejecutar los else en los for incluso si esta vacio el objeto proporcionado)
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino")
    
#todo lo anterior funciona igual para tuplas y listas
