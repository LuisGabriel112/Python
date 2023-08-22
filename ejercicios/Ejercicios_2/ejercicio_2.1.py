#pedir nombre y edad de los compañeros y ordenar los datos de mayor a menor

#el mayor de la clase es el profesor y el menor el asistente

profesor = ""
Alumno_asistente = ""

my_dict = {}


for i in range(10):
    nombre = input("Dime tu nombre ")
    edad = int(input("dime tu edad "))
    i = nombre 
    my_dict[i] = edad


print(my_dict)