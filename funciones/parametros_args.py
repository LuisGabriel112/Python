#forma no optima de sumar valores
""" def suma(lista):
    numero_sumados = 0
    for numeros in lista:
        numero_sumados = numero_sumados + numeros
    return numero_sumados
resultado = suma([5,3,9,10])
print(resultado) """

 # * significa que se puede pasar cualquier cantidad de argumentos a la función. y lo convierte a una lista
def suma (*numeros):
    return sum(numeros)
    
resultado = suma (1,2,3,4,5,7,7,8)
print (resultado)
