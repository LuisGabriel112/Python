import random
from colorama import Fore,init

init()

X = ['*','*','*','*',]
intentos = 4

def bienvenida():
   print(Fore.GREEN+'''
          ******************************
         * || BIENVENIDO AL AHORCADO || *
          ******************************
         ''')

def hangman():
   palabras = ['agua','palo','casa']
   Hw = random.choice(palabras)
   Hw.lower
   print(Hw)
   ahorcado = prests()
   letra = input(Fore.LIGHTRED_EX+"Introduce una letra (a-z): ")
   for letras in X:
      busqueda = Hw.find(letra)
      if busqueda != -1:
         letra
         print("Encontraste una letra")
         X.pop(busqueda)
         X.insert(busqueda,letra)
         print(X)
      else:
         intentosN = intentos - 1
         print("Sigue intentando")
         print(ahorcado[0])


def prests():
   ahorcado0 =Fore.YELLOW+ '''
~~~~~~~~~~~|~~~~~~~~~
           I
                   
                   
          '''

   ahorcado1 =Fore.YELLOW+  '''
~~~~~~~~~~~|~~~~~~~~
           I
           o   
               
        _ _ _ _             
          '''

   ahorcado2 =Fore.YELLOW+  '''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
           |  
                   
        _ _ _ _
          '''

   ahorcado3 =Fore.YELLOW+  '''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
           |\
  
               
        _ _ _ _    
          '''

   ahorcado4 =Fore.YELLOW+  '''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
          /|\   
        _ _ _ _   
          '''

   ahorcado5 =Fore.YELLOW+  '''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
          /|\
            \   
                
        _ _ _ _   
          '''

   ahorcado6 =Fore.YELLOW+  f'''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
          /|\
          / \   
      
        _ _ _ _  
          '''
   return [ahorcado0, ahorcado1, ahorcado2, ahorcado3, ahorcado4, ahorcado5, ahorcado6]

   

   

    

#bienvenida()
hangman()