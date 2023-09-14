import random
from colorama import Fore, init

init()

X = ['*', '*', '*', '*']

intentos = 6
prst = 1

def bienvenida():
   print(Fore.GREEN+'''
          ******************************
         * || BIENVENIDO AL AHORCADO || *
          ******************************
         ''')

def hangman():
   global intentos
   global prst
   palabras = ['agua', 'palo', 'casa']
   Hw = random.choice(palabras).lower()
   print(Hw)
   ahorcado = prests()
   letras_adivinadas = ['_'] * len(Hw)
   while intentos > 0 and '_' in letras_adivinadas:
      letra = input(Fore.LIGHTRED_EX + "Introduce una letra (a-z): ").lower()
      
      if len(letra) == 1 and letra.isalpha():
         encontrada = False
         for i, letra_palabra in enumerate(Hw):
            if letra == letra_palabra:
               letras_adivinadas[i] = letra
               encontrada = True

         if encontrada:
            print("Encontraste una letra")
            print(' '.join(letras_adivinadas))
         else:
            intentos -= 1
            print("Sigue intentando")
            print(ahorcado[prst])
            prst += 1
      else:
         print("Por favor, introduce una sola letra válida.")

   if '_' not in letras_adivinadas:
      print("¡Felicidades! Has adivinado la palabra:", Hw)
   else:
      print("¡Lo siento, has agotado tus intentos! La palabra era:", Hw)

def prests():
   ahorcado0 =Fore.YELLOW+'''
~~~~~~~~~~~|~~~~~~~~~
           I
                   
                   
          '''

   ahorcado1 =Fore.YELLOW+'''
~~~~~~~~~~~|~~~~~~~~
           I
           o   
               
          '''

   ahorcado2 =Fore.YELLOW+'''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
           |  
                   
          '''

   ahorcado3 =Fore.YELLOW+'''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
           |\
  
               
          '''

   ahorcado4 =Fore.YELLOW+'''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
          /|\   
          '''

   ahorcado5 =Fore.YELLOW+'''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
          /|\
            \   
                
          '''

   ahorcado6 =Fore.YELLOW+'''
~~~~~~~~~~~|~~~~~~~~~
           I
           o
          /|\
          / \   
      
          '''
   return [ahorcado0, ahorcado1, ahorcado2, ahorcado3, ahorcado4, ahorcado5, ahorcado6]

bienvenida()
hangman()