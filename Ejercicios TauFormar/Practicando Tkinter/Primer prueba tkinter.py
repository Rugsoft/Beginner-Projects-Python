# Importamos la biblioteca tkinter con el alias tk para facilitar su uso
import tkinter as tk

# Función que cambia el texto del Label a español
def saludar():
    saludo.config(text="Buenos Dias")

# Función que cambia el texto del Label a inglés
def greet():
    saludo.config(text="Good Morning")

# Función que se ejecuta cuando presionamos Enter en el Entry
# El parámetro x es el evento que genera la tecla Enter
def mostrar(x):
    valor = respuesta.get()  # Obtiene el texto del Entry
    saludo.config(text="Hola "+valor)  # Actualiza el Label con el texto

# Función similar a mostrar() pero se ejecuta al hacer clic en el botón
def mostrar_boton():
    valor = respuesta.get()  # Obtiene el texto del Entry
    saludo.config(text="Hola "+valor)  # Actualiza el Label con el texto

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Primera ventana en Python")  # Establecemos el título de la ventana

# Creamos una etiqueta (Label) para mostrar texto
saludo = tk.Label(ventana, text="Bon dia")
saludo.pack()  # Coloca el widget en la ventana

# Creamos un campo de entrada (Entry) para que el usuario escriba
respuesta = tk.Entry(ventana)
respuesta.pack()  # Coloca el Entry en la ventana
respuesta.bind("<Return>", mostrar)  # Vincula la tecla Enter con la función mostrar

# Creamos tres botones con diferentes funciones
boton1 = tk.Button(ventana, text="Español", command=saludar)  # Botón para texto en español
boton1.pack()
boton2 = tk.Button(ventana, text="English", command=greet)    # Botón para texto en inglés
boton2.pack()
boton3 = tk.Button(ventana, text="Coger", command=mostrar_boton)  # Botón para mostrar texto del Entry
boton3.pack()

# Iniciamos el bucle principal de la aplicación
# Este bucle mantiene la ventana abierta y responde a las interacciones del usuario
ventana.mainloop()
