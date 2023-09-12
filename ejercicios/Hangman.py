import random
from colorama import Fore,init

init()


def bienvenida():
   print(Fore.GREEN+'''
          ******************************
         * || BIENVENIDO AL AHORCADO || *
          ******************************
         ''')


def prests():
   ahorcado0 =Fore.YELLOW+ '''
~~~~~~~~~~~|~~~~~~~~~
           I
                   
                   
        _ _ _ _
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

   ahorcado6 =Fore.YELLOW+  '''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
          /|\
          / \   
                 
        _ _ _ _  
          '''
   return [ahorcado0, ahorcado1, ahorcado2, ahorcado3, ahorcado4, ahorcado5, ahorcado6]

   
def hangman():
   palabras = ['agua','palo','casa']
   Hw = random.choice(palabras)
   Hw.lower
   print(Hw)
   ahorcado = prests()
   letra = input(Fore.LIGHTRED_EX+"Introduce una letra (a-z): ")
   busqueda = Hw.find(letra)
   if busqueda == 1:
      print("Encontraste una letra")
   else:
      print("Sigue intentando")
   #if input == Hw:
   

    

#bienvenida()
hangman()