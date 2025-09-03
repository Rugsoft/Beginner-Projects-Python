# Importamos tkinter para crear la interfaz gráfica
import tkinter as tk

# Variables globales para almacenar la lista de números y contar repeticiones
lista_numeros = []  # Lista para guardar los números ingresados
contador = 0        # Contador para números repetidos consecutivos

def añadir_numero():
    """
    Función que se ejecuta al hacer clic en el botón 'Añadir'.
    Obtiene el número del campo de entrada y lo añade a la lista.
    También maneja el contador de repeticiones consecutivas.
    """
    global contador  # Indicamos que usaremos la variable global contador
    try:
        num = int(entry_numeros.get())  # Convertimos la entrada a número entero
    except ValueError:
        ventana_error_flag()

    if not lista_numeros:  # Si la lista está vacía
        añadido_label.config(text=f"Número {num} añadido")
        lista_numeros.append(num)
    elif num == lista_numeros[-1]:  # Si el número es igual al último añadido
        contador += 1  # Incrementamos el contador de repeticiones
        añadido_label.config(text=f"Número {num} añadido x{contador+1}")
        lista_numeros.append(num)   
    else:  # Si el número es diferente al último
        añadido_label.config(text=f"Número {num} añadido")
        lista_numeros.append(num)
        contador = 0  # Reiniciamos el contador de repeticiones

def sumar_lista():
    """
    Función que se ejecuta al hacer clic en el botón 'Sumar lista'.
    Calcula la suma de todos los números en la lista y limpia la lista.
    """
    global contador
    total = sum(lista_numeros)  # Calculamos la suma de todos los números
    suma_label.config(text=f"La suma total es: {total}")
    lista_numeros.clear()  # Vaciamos la lista
    contador = 0  # Reiniciamos el contador

def ventana_error_flag():
    # Creamos una nueva ventana para mostrar el error
    ventana_error = tk.Tk()
    ventana_error.title("Error de ValueError")  # Título de la ventana de error
    ventana_error.geometry("150x75")  # Tamaño de la ventana de error
    # Etiqueta que muestra el mensaje de error
    error_label = tk.Label(ventana_error, text="Introduce un número!")
    error_label.pack()
    # Botón para cerrar solo la ventana de error
    boton_error = tk.Button(ventana_error, text="Cerrar", command=lambda: ventana_error.destroy())
    boton_error.pack()

    
    
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de lista de valores")  # Título de la ventana
ventana.geometry("200x150")  # Tamaño inicial de la ventana


# Crear y configurar el campo de entrada
entry_label = tk.Label(ventana, text="Entrada de numeros:")  # Etiqueta para el campo de entrada
entry_label.pack()  # Colocar la etiqueta en la ventana
entry_numeros = tk.Entry(ventana)  # Campo de entrada para los números
entry_numeros.pack()  # Colocar el campo de entrada en la ventana

# Crear y configurar el botón de añadir y su etiqueta de estado
boton_add = tk.Button(ventana, text="Añadir", command=añadir_numero)  # Botón para añadir números
boton_add.pack()  # Colocar el botón en la ventana
añadido_label = tk.Label(ventana, text="")  # Etiqueta para mostrar el estado de la adición
añadido_label.pack()  # Colocar la etiqueta de estado en la ventana

# Crear y configurar el botón de sumar y su etiqueta de resultado
boton_suma = tk.Button(ventana, text="Sumar lista", command=sumar_lista)  # Botón para sumar la lista
boton_suma.pack()  # Colocar el botón en la ventana
suma_label = tk.Label(ventana, text="")  # Etiqueta para mostrar el resultado de la suma
suma_label.pack()  # Colocar la etiqueta de resultado en la ventana

# Iniciar el bucle principal de la aplicación (mantiene la ventana abierta y responde a eventos)
ventana.mainloop()  # Bucle principal de Tkinter