#pedir nombre y edad de los compañeros y ordenar los datos de mayor a menor
#el mayor de la clase es el profesor y el menor el asistente
profesor = ""
Alumno_asistente = ""
alumnos = {}
edadadesyalumnos = []
cantidad_alumnos = 0
for i in range(3):
    edad = int(input("Dame tu edad "))
    nombre = input("Dime tu nombre ")
    i = edad
    alumnos[i] = nombre
dic_it =alumnos.items()
for o in dic_it:
    edadadesyalumnos.append(o)
edadadesyalumnos.sort(reverse=True)
print(edadadesyalumnos)
profesor = edadadesyalumnos[0]
Alumno_asistente = edadadesyalumnos[-1]
print(f"El profesor es {profesor} el asistente es {Alumno_asistente}")