numeros = [1,3,5,1,1234,124]

#encontramos el numero mayor de la lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontramos el numero menor de la lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.23525, 2)

print(numero)

#retorna false si le pasamos = 0 , False, vacio, ninguno
resultado_bool = bool(1)

print(resultado_bool)

#retorna true si todos los valores son verdaderos
resultados_all = all([0,"true"])
print (resultados_all)

#suma todos los valores de un iterable 
suma_total = sum(numeros)

print(suma_total)