""" def Saludar():
    print("Hola")

Saludar() """

#crear una funcion que tengan parametros
def saludar(nombre,sexo):
    sexo = sexo.lower()
    if (sexo == "mujer"):
        adjetivo = "y"
    elif (sexo == "hombre"):
        adjetivo = "x"
    print(f"Hola {nombre} que tal {adjetivo}")
    
#saludar("Luis", "muJEr")

#creando una funcion que nos retorne valores
def crear_contraseña_r (num):# creando funcion
    caracteres = "abcdefghij"# creando caracteres aleatorios
    
    num_entero = str(num)#convirtiendo a string el primer numero
    
    num = int(num_entero[0])#pasando el primer dato del string el indice 0
    
    c1 = num-2#dando valor al caracter 1 dependiendo de la posicion de la lista
    c2 = num#dando valor al caracter 1 dependiendo de la posicion de la lista
    c3 = num-5#dando valor al caracter 1 dependiendo de la posicion de la lista
    
    contraseña = f'{caracteres[c1]}{caracteres[c2]}{caracteres[c3]}{num*2}'#Creando la contraseña
    return contraseña

pwd = crear_contraseña_r(4)
frase = f'Tu nueva contraseña es {pwd}'

print(frase)