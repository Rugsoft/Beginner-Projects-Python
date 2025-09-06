import os
import tkinter as tk
from tkinter import messagebox

# Es una buena práctica definir la ruta del archivo en una variable.
path_archivo = "temperaturas.txt"
path_salida = "promedios.txt"

# Las listas globales para almacenar los datos.
temperaturas_maximas = []
temperaturas_minimas = []

def crear_documento():
    """Crea el archivo de texto inicial si no existe."""
    temperaturas_str = "30 15,29 12,32 16,30 14,28 10"
    
    if os.path.exists(path_archivo):
        messagebox.showinfo("Información", f"El archivo '{path_archivo}' ya existe. No se creará uno nuevo.")
        return

    try:
        with open(path_archivo, "w") as archivo:
            contenido = temperaturas_str.replace(",", "\n")
            archivo.write(contenido)
        messagebox.showinfo("Éxito", f"Archivo '{path_archivo}' creado con éxito.")
    except IOError as e:
        messagebox.showerror("Error", f"Error al crear el archivo: {e}")

def leer_documento():
    """Lee el documento y carga las temperaturas en las listas globales."""
    temperaturas_maximas.clear()
    temperaturas_minimas.clear()
    etiqueta_promedios.config(text="") # Limpia el resultado anterior
    
    try:
        with open(path_archivo) as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                if len(partes) == 2:
                    # Usamos float para ser más flexibles, aunque los datos de ejemplo son int
                    temperaturas_maximas.append(float(partes[0]))
                    temperaturas_minimas.append(float(partes[1]))
        
        # Actualizar la GUI para mostrar los datos leídos
        texto_max = "Máximas: " + ", ".join(map(str, temperaturas_maximas))
        texto_min = "Mínimas: " + ", ".join(map(str, temperaturas_minimas))
        etiqueta_datos_leidos.config(text=f"{texto_max}\n{texto_min}")
        messagebox.showinfo("Éxito", "Documento leído y procesado correctamente.")

    except FileNotFoundError:
        messagebox.showerror("Error", f"No se encontró el archivo '{path_archivo}'. Ejecuta 'Crear Documento' primero.")
        etiqueta_datos_leidos.config(text="Error al leer. El archivo no existe.")
    except ValueError:
        messagebox.showerror("Error", "El archivo contiene valores que no son números. Revisa el formato.")
        etiqueta_datos_leidos.config(text="Error de formato en el archivo.")

def calcular_promedios():
    """Calcula y muestra el promedio de las temperaturas máximas y mínimas."""
    if not temperaturas_maximas or not temperaturas_minimas:
        messagebox.showwarning("Sin Datos", "No hay datos para calcular promedios. Lee el documento primero.")
        return

    promedio_max = sum(temperaturas_maximas) / len(temperaturas_maximas)
    promedio_min = sum(temperaturas_minimas) / len(temperaturas_minimas)
    
    resultado_gui = f"Promedio Máximas: {promedio_max:.2f} °C\nPromedio Mínimas: {promedio_min:.2f} °C"
    etiqueta_promedios.config(text=resultado_gui)
    
    # Guardar en archivo
    salida_archivo = f"Promedio de máximas: {promedio_max:.2f} °C, Promedio de mínimas: {promedio_min:.2f} °C"
    try:
        with open(path_salida, "w") as archivo:
            archivo.write(salida_archivo)
        messagebox.showinfo("Guardado", f"Promedios guardados en '{path_salida}'")
    except IOError as e:
        messagebox.showerror("Error", f"No se pudo guardar el archivo de promedios: {e}")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Análisis de Temperaturas")
ventana.geometry("400x400")
ventana.resizable(False, False)

# --- Creación y Posicionamiento de Widgets ---

titulo = tk.Label(ventana, text="Analizador de Temperaturas", font=("Helvetica", 16, "bold"))
titulo.pack(pady=15)

boton_crear = tk.Button(ventana, text="1. Crear Documento", command=crear_documento, width=25, height=2)
boton_crear.pack(pady=5)

boton_leer = tk.Button(ventana, text="2. Leer Documento", command=leer_documento, width=25, height=2)
boton_leer.pack(pady=5)

etiqueta_datos_leidos = tk.Label(ventana, text="Datos leídos aparecerán aquí...", justify=tk.LEFT, wraplength=380)
etiqueta_datos_leidos.pack(pady=10)

boton_calcular = tk.Button(ventana, text="3. Calcular Promedios", command=calcular_promedios, width=25, height=2)
boton_calcular.pack(pady=5)

etiqueta_promedios = tk.Label(ventana, text="", font=("Consolas", 12, "bold"), justify=tk.LEFT)
etiqueta_promedios.pack(pady=10)

# --- Bucle Principal de la Aplicación ---
ventana.mainloop()