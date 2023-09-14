#Creando una funcion que sume numeros
def sumar_dos():
    #iniciando bucle
    while True:
        #pidiendo numeros
        a = input('numero 1: ')
        b = input('numero 2: ')
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
            #si lanzo una excepcion, pedirle que reingrese los datos
        except:
            print('Dame un numero valido')
        #si todo salio bien terminamos el bucle
        else:
            break
    #mostrando el resultado
    return(resultado)
print(sumar_dos())