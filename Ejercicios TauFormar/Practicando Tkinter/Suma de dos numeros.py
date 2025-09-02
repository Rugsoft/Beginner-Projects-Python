# Importamos la biblioteca tkinter con el alias tk para facilitar su uso
import tkinter as tk

# Función que realiza la suma de los números ingresados
def sumar():
    n1 = num1.get()  # Obtiene el valor del primer Entry
    n2 = num2.get()  # Obtiene el valor del segundo Entry
    suma = int(n1) + int(n2)  # Convierte los valores a enteros y los suma
    resultado.config(text=f"Resultado: {suma}")  # Muestra el resultado en el Label

# Creamos la ventana principal
ventana = tk.Tk()
# Configuramos el título y tamaño de la ventana
ventana.title("Suma de dos valores")  # Establece el título de la ventana
ventana.geometry("500x300")  # Establece el tamaño de la ventana (ancho x alto)

# Creamos y configuramos los widgets para el primer número
num1Label = tk.Label(ventana, text="Numero 1:")  # Etiqueta para el primer número
num1Label.pack()  # Coloca la etiqueta en la ventana
num1 = tk.Entry(ventana)  # Campo de entrada para el primer número
num1.pack()  # Coloca el campo de entrada en la ventana

# Creamos y configuramos los widgets para el segundo número
num2Label = tk.Label(ventana, text="Numero 2:")  # Etiqueta para el segundo número
num2Label.pack()  # Coloca la etiqueta en la ventana
num2 = tk.Entry(ventana)  # Campo de entrada para el segundo número
num2.pack()  # Coloca el campo de entrada en la ventana

# Creamos la etiqueta donde se mostrará el resultado
resultado = tk.Label(ventana, text="Resultado:")  # Etiqueta para mostrar el resultado
resultado.pack()  # Coloca la etiqueta de resultado en la ventana

# Creamos el botón que ejecutará la suma
boton = tk.Button(ventana, text="Sumar", command=sumar)  # Botón que llama a la función sumar
boton.pack()  # Coloca el botón en la ventana

# Iniciamos el bucle principal de la aplicación
ventana.mainloop()  # Mantiene la ventana abierta y responde a las interacciones