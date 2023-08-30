

change = 0
while change != 1:
    print("""Hola bienvenido a la calculadora
      Selecciona una opcion
      Sum - sumar
      Res - restar
      Mul - multiplicar
      Div - Dividir
      E   - Salir""")
    Eleccion = input()
    if Eleccion == "Sum":
        a = int(input("Dame el primer operador "))
        b = int(input("Dame el primer operador "))
        print(a + b)
    elif Eleccion == 'Res':
        a = int(input("Dame el primer operador "))
        b = int(input("Dame el primer operador "))
        print (a-b )
    elif Eleccion == "Mul":
        a = int(input("Dame el primer operador "))
        b = int(input("Dame el primer operador "))
        print(a*b)
    elif Eleccion == "Div":
        a = int(input("Dame el primer operador "))
        b = int(input("Dame el primer operador "))
        print (a/b)
    elif Eleccion == "E":
        print("Saliendo...")
        change = 1      
