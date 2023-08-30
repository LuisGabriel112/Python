#AND
#and nos devuelve true si ambas se cumplen
Resultado = True & True #Devolver True
Resultado2= False & True #Devolver Falso
Resultad3 = True & False #Devolver Falso
Resultad4 = False & False #Devolver Falso

#OR
#or nos devuelve falso solo si las dos condiciones no se cumplen
Resultado5 = True | True #Devolver True
Resultado6 = False | True #Devolver True
Resultad7 = True | False #Devolver True
Resultado8 = False | False #Devolver Falso

#NOT
#si le damos un valor true lo convierte en false y viceversa 
Resultado9 = not True #Devolver Falso
Resultado10 = not False #Devolver True
print(Resultado2)
