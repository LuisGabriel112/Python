import tkinter as tk

ventana = tk.Tk()

def saludar():
    label.config(text="hola, "+ nombre.get()+ "!")
    
boton_saludar = tk.Button(ventana, text="saludar", command=saludar)

label = tk.Label(ventana, text="Cual es tu nombre?")

nombre = tk.Entry(ventana)

label.pack
nombre.pack()
boton_saludar.pack()

ventana.mainloop()