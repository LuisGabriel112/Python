#promedio de duracion
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudos
crudo_promedio = 5
crudo_dalto = 3.5


#Diferencias de duracion

diferenciasConMin = 100 - dalto_curso / otros_cursos_min * 100
diferenciasConMax = 100 - dalto_curso *1000 // otros_cursos_max / 10
diferenciasPromedio = 100 - dalto_curso / otros_cursos_promedio * 100

#calculando el porcentaje de tiempo vacio
tiempoVacioPromedio = 100 - otros_cursos_promedio *1000/ crudo_promedio / 10
tiempoVacioDalto = 100 - dalto_curso *1000 // crudo_dalto / 10

#mostrando la diferencia de duracion(A)
print("------------------------------")
print(f"El curso de dalto dura un {diferenciasConMin}% menos que el mas  rapido")
print(f"El curso de dalto dura un {diferenciasConMax}% menos que el mas  lento")
print(f"El curso de dalto dura un {diferenciasPromedio}% menos que el promedio")
print("------------------------------")
#Mostrando la diferencia de duracion (B)
print(f"este curso promedio elimina un {tiempoVacioPromedio}% del tiempo vacio")
print(f"este curso elimino un {tiempoVacioDalto}% del tiempo vacio")
print("------------------------------")
#Mostrando diferencias si los cursos duraran 10hrs
print("------------------------------")
print(f'ver 10 horas de este curso equivale a ver {otros_cursos_promedio *100 // dalto_curso /10} horas de otros cursos ')
print(f'ver 10 horas de otros cursos equivale a ver {dalto_curso *100 // otros_cursos_promedio /10} horas de otros cursos ')
print("------------------------------")