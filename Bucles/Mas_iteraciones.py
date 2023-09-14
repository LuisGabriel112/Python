cadena = "Hola Luis"
frutas = ["banana", "manzana","ciruela","Pera","Naranja", "Granada","Durazno"]
numero = [2,5,8,10]
#creando condiciones dentro de un for
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"Me estoy comiendo una: {fruta}")
    
#evitar que el bucle se siga ejecutando
for fruta in frutas:
    if fruta == "manzana":
        break
    print(f"Me estoy comiendo una: {fruta}")
    
#recorrer una cadena de texto
for letra in cadena:
    print(letra)

#for en una sola linea
numero_duplicados = [x*2 for x in numero]
print (numero_duplicados)