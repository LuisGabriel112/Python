#creando un conjunto con set
conjunto = set(["dato1","dato2"])

#metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset(["dato1","dato2"])
conjunto2 = {conjunto1,"dato3"}

#print (conjunto2)

#Teoria de conjuntos
conjunto1 = {1,2,3,4,20}
conjunto2 = {1,3,2}

#verificamos si es un subconjunto 
Resultado = conjunto2.issubset(conjunto1)
#otra forma de verificar
Resultado = conjunto2 <= conjunto1


#verificamos si es un superconjunto 
Resultado2 = conjunto2.issuperset(conjunto1)
#otra forma de verificar
Resultado2 = conjunto2 < conjunto1


#verifica si hay algun numero en comun
Resultado = conjunto2.isdisjoint(conjunto1)
print(Resultado2)