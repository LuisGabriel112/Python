import random


def inicio ():
    nombre = input('Hola!, ¿Cual es tu nombre? ')
    bienvenida = print(f"Bienvenido al juego de piedra papel tijeras {nombre} ")
    return bienvenida

def Juego ():
    elecciones = ['Piedra','Papel','Tijera',]
    
    eleccionU = input('Selecciona una opcion \n[1] Piedra \n[2] Papel \n[3] Tijera\n')
    
    #eleccion de la maquina 
    eleccion = random.choice(elecciones)
    
    if eleccionU == 'Piedra' or 'piedra' and eleccion == 'Piedra' or 'piedra':
        print("Empate")
    elif eleccionU == 'Piedra' or 'piedra' and eleccion == 'papel' or 'Papel':
        print ("Perdiste")
    elif eleccionU == 'Piedra' or 'piedra' and eleccion == 'Tijera' or 'tijera':
        print ("Ganaste!!!")
    elif eleccionU == 'Papel' or 'papel' and eleccion == 'Piedra' or 'piedra':
        print("Ganaste")
    elif eleccionU == 'Papel' or 'papel' and eleccion == 'papel' or 'Papel':
        print ("Empate")
    elif eleccionU == 'Papel' or 'papel' and eleccion == 'Tijera' or 'tijera':
        print ("Perdiste")
    elif eleccionU == 'Tijera' or 'tijera' and eleccion == 'Piedra' or 'piedra':
        print("Perdiste")
    elif eleccionU == 'Tijera' or 'tijera' and eleccion == 'papel' or 'Papel':
        print ("Ganaste")
    elif eleccionU == 'Tijera' or 'tijera' and eleccion == 'Tijera' or 'tijera':
        print ("Empate")
        
        
    return eleccion

    
inicio()
Juego()