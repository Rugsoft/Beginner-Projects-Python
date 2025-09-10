# Importa la biblioteca tkinter para crear la interfaz gráfica de usuario (GUI).
# 'as tk' es un alias común para simplificar el código.
import tkinter as tk
# Importa el módulo messagebox de tkinter para mostrar ventanas emergentes (diálogos).
from tkinter import messagebox


# Define la ruta al archivo de entrada que contiene las estadísticas.
path_estadisticas = "DAT/estadisticas.txt"
# Define la ruta al archivo de salida donde se guardará el análisis.
path_analisis = "DAT/analisis.txt"

# Inicializa listas globales para almacenar los puntos y rebotes de cada partido.
# Estas listas se llenarán al leer el archivo de estadísticas.
puntos_partido = []
rebotes_partido = []
#######################Funciones###############################################

# Define la función principal que se ejecuta al presionar el botón "Analizar".
def leer_y_analizar():
    fecha = entrada_fecha.get()
    # Verifica si el campo de fecha está vacío.
    if not fecha:
        # Si está vacío, muestra una advertencia y detiene la ejecución de la función.
        messagebox.showwarning("Sin Datos", "No has introducido nada")
        return
    #Limpiamos las listas, para que cada vez que le demos al boton de analizar, no se acumulen datos
    puntos_partido.clear()
    rebotes_partido.clear()
    # Intenta abrir y leer el archivo de estadísticas.
    try:
        with open(path_estadisticas) as file:
            for line in file:
                partes = line.strip().split()
                if len(partes) == 3:
                    puntos_partido.append(int(partes[1]))
                    rebotes_partido.append(int(partes[2]))
            messagebox.showinfo("Éxito", "El documento ha sido leído y procesado correctamente.")
    # Si el archivo no se encuentra, captura la excepción FileNotFoundError.
    except FileNotFoundError:
        # Muestra un mensaje de error indicando que el archivo no existe.
        messagebox.showerror("Error", "No se encontró el archivo 'estadisticas.txt'. Asegúrate de crearlo primero.")
        return # Detiene la función si no se encuentra el archivo.

    promedio_puntos = sum(puntos_partido) / len(puntos_partido)
    # Calcula el promedio de rebotes.
    promedio_rebotes = sum(rebotes_partido) / len(rebotes_partido)
    # Crea la cadena de texto que se guardará en el archivo de análisis.
    # Usa un f-string para formatear el texto con los promedios calculados (con 2 decimales).
    salida_archivo = f"A fecha {fecha} - La media de puntos es: {promedio_puntos:.2f} y la media de rebotes: {promedio_rebotes:.2f}"
    # Intenta abrir y escribir en el archivo de análisis.
    try:
            # Abre el archivo en modo escritura ("w"), lo que sobrescribirá su contenido si ya existe.
            with open(path_analisis, "w") as file:
                file.write(salida_archivo)
            # Muestra un mensaje de éxito indicando que los datos se guardaron.
            messagebox.showinfo("Guardado", f"Analisis guardados en '{path_analisis}'")
    # Si ocurre un error de entrada/salida (ej: permisos de escritura denegados).
    except IOError as e:
        # Muestra un mensaje de error con los detalles de la excepción.
        messagebox.showerror("Error", f"No se pudo guardar el archivo de analisis: {e}")

########################GUI####################################################

# Crea la ventana principal de la aplicación.
ventana = tk.Tk()
# Establece el título de la ventana.
ventana.title("Análisis de Puntos y rebotes")
# Establece el tamaño inicial de la ventana (ancho x alto).
ventana.geometry("400x200")

# Crea una etiqueta (Label) para el título principal.
titulo = tk.Label(ventana, text="Introduce una fecha", font=("Helvetica", 16, "bold"))
# Empaqueta la etiqueta en la ventana, con un relleno vertical (pady) de 15 píxeles.
titulo.pack(pady=15)

# Crea un campo de entrada de texto (Entry).
entrada_fecha = tk.Entry(ventana, font=("Helvetica", 16, "bold"))
entrada_fecha.pack(pady=15)

# Crea un botón (Button).
# 'command=leer_y_analizar' asigna la función que se ejecutará al hacer clic.
boton_analizar = tk.Button(ventana, text="Analizar", command=leer_y_analizar, width=25, height=2, bg="lightblue")
boton_analizar.pack(pady=5)

# Inicia el bucle principal de eventos de la GUI.
# Esto mantiene la ventana abierta y receptiva a las acciones del usuario.
ventana.mainloop()