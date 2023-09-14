""" a = 1 
b = 2
nombre = "Luis"
nombre = "Gabriel"
print(nombre) """

""" nombre = "Luis"
bienvenida = f"Hola {nombre} ¿Como estas?"#f Strings (lo que hace es tomar un dato y cambiarlo a texto)
del bienvenida #se utiliza para borrar esta variable
print (bienvenida) """

nombre = "Luis"
bienvenida = f"Hola {nombre} ¿Como estas?"#f Strings (lo que hace es tomar un dato y cambiarlo a texto)

print ("Hola" in bienvenida)

nombre = "Lucas"
#concatenar con +
bienvenida = "Hola" + '¿Como estas?'
#concatenar con f-strings
bienvenida = f"Hola {nombre} ¿Como estas?"
#operadores de pertenencia (in / not in)
print("Lucas" in bienvenida) #true
print ("Lucas" not in bienvenida) #false
