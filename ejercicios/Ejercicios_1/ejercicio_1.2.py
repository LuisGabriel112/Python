#cantidad de palabras x segundo que las personas hablan
personaPromedio = 2.0
Dalto = 2.6

palabra = input("dime cualquier texto: ")

palabra= palabra.split(" ")

cantidadDePalabras = len(palabra)

tiempo = cantidadDePalabras / personaPromedio

tiempoDalto = cantidadDePalabras / Dalto

print("=======================================")
print(f"dijiste {cantidadDePalabras} palabras ")
print("=======================================")
if tiempo > 60.0:
    print("Tampoco me cuentes tu vida crack")
else:
     print (f"El tiempo que te tomaria en decir esa frase es de {tiempo} segundos")
     print (f"Dalto se tardaria {tiempoDalto} segundos")