import tkinter as tk
from tkinter import messagebox

# --- Variables Globales ---
precios = []

# --- Paleta de Colores y Fuentes ---
COLOR_FONDO = "#2C3E50"
COLOR_TEXTO = "#ECF0F1"
COLOR_INPUT_FONDO = "#34495E"
COLOR_BOTON = "#3498DB"
COLOR_BOTON_TEXTO = "#FFFFFF"
COLOR_ETIQUETA_RESULTADO = "#2ECC71"
COLOR_MENSAJE_ERROR = "#E74C3C"

FONT_NORMAL = ("consolas", 12)
FONT_BOLD = ("consolas", 12, "bold")
FONT_RESULTADO = ("consolas", 16, "bold")


# --- Funciones ---

def anadir_precio():
    """
    Toma el precio del cuadro de texto, lo valida y lo añade a la lista de precios.
    """
    precio_str = entrada_precio.get()
    try:
        precio_float = float(precio_str)
        if precio_float >= 0:
            precios.append(precio_float)
            actualizar_mensaje(f"Precio añadido: {precio_float:.2f} €", COLOR_ETIQUETA_RESULTADO)
            # Limpia la caja de texto después de añadir
            entrada_precio.delete(0, tk.END)
        else:
            actualizar_mensaje("El precio no puede ser negativo.", COLOR_MENSAJE_ERROR)

    except ValueError:
        actualizar_mensaje("Error: Introduce un número válido.", COLOR_MENSAJE_ERROR)

def calcular_total():
    """
    Calcula la suma total de los precios en la lista y la muestra en la etiqueta de resultados.
    """
    if not precios:
        actualizar_mensaje("No hay precios para calcular el total.", COLOR_MENSAJE_ERROR)
        return
        
    total = sum(precios)
    etiqueta_resultado.config(text=f"Total: {total:.2f} €")
    actualizar_mensaje("Cálculo del total realizado.", COLOR_TEXTO)


def calcular_promedio():
    """
    Calcula el promedio de los precios y lo muestra en la etiqueta de resultados.
    """
    if not precios:
        actualizar_mensaje("No hay precios para calcular el promedio.", COLOR_MENSAJE_ERROR)
        etiqueta_resultado.config(text="Promedio: N/A")
        return
    
    promedio = sum(precios) / len(precios)
    etiqueta_resultado.config(text=f"Promedio: {promedio:.2f} €")
    actualizar_mensaje("Cálculo del promedio realizado.", COLOR_TEXTO)

def guardar_historial():
    """
    Guarda todos los precios introducidos en el archivo 'historial.txt'.
    """
    if not precios:
        actualizar_mensaje("No hay precios para guardar en el historial.", COLOR_MENSAJE_ERROR)
        return

    try:
        with open("historial.txt", "w") as f:
            for precio in precios:
                f.write(f"{precio:.2f}\n")
        actualizar_mensaje("Historial guardado en 'historial.txt'", COLOR_ETIQUETA_RESULTADO)
    except IOError as e:
        actualizar_mensaje(f"Error al guardar el historial: {e}", COLOR_MENSAJE_ERROR)


def guardar_estadisticas():
    """
    Guarda el total y el promedio en el archivo 'estadisticas.txt'.
    """
    if not precios:
        actualizar_mensaje("No hay datos para guardar estadísticas.", COLOR_MENSAJE_ERROR)
        return

    total = sum(precios)
    promedio = total / len(precios)
    
    try:
        with open("estadisticas.txt", "w") as f:
            f.write(f"Total de Ventas: {total:.2f} €\n")
            f.write(f"Promedio de Venta: {promedio:.2f} €\n")
        actualizar_mensaje("Estadísticas guardadas en 'estadisticas.txt'", COLOR_ETIQUETA_RESULTADO)
    except IOError as e:
        actualizar_mensaje(f"Error al guardar estadísticas: {e}", COLOR_MENSAJE_ERROR)


def actualizar_mensaje(texto, color):
    """
    Actualiza el texto y color de la etiqueta de mensajes/feedback.
    """
    etiqueta_mensaje.config(text=texto, fg=color)


# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Gestor de Pedidos - Tienda de Repuestos")
ventana.geometry("400x450")
ventana.resizable(False, False)
ventana.configure(bg=COLOR_FONDO)

# --- Creación y Posicionamiento de Widgets ---

# Etiqueta para el campo de entrada
etiqueta_info = tk.Label(
    ventana,
    text="Precio del Producto (€):",
    font=FONT_NORMAL,
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
)
etiqueta_info.place(x=50, y=40)

# Campo de entrada para el precio
entrada_precio = tk.Entry(
    ventana,
    font=FONT_NORMAL,
    width=20,
    bg=COLOR_INPUT_FONDO,
    fg=COLOR_TEXTO,
    insertbackground=COLOR_TEXTO, # Color del cursor
    borderwidth=2,
    relief="groove"
)
entrada_precio.place(x=50, y=70)

# Botón para añadir precio
boton_anadir = tk.Button(
    ventana,
    text="Añadir",
    command=anadir_precio,
    font=FONT_BOLD,
    bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    width=10,
    relief="raised",
    borderwidth=2
)
boton_anadir.place(x=250, y=68)

# Botones de acciones
boton_total = tk.Button(ventana, text="Total", command=calcular_total, font=FONT_BOLD, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, width=15)
boton_total.place(x=50, y=140)

boton_promedio = tk.Button(ventana, text="Promedio", command=calcular_promedio, font=FONT_BOLD, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, width=15)
boton_promedio.place(x=200, y=140)

# Etiqueta para mostrar el resultado (total o promedio)
etiqueta_resultado = tk.Label(
    ventana,
    text="Total: 0.00 €",
    font=FONT_RESULTADO,
    bg=COLOR_FONDO,
    fg=COLOR_ETIQUETA_RESULTADO,
    width=25,
    anchor="w"
)
etiqueta_resultado.place(x=50, y=220)

# Etiqueta para mensajes de feedback
etiqueta_mensaje = tk.Label(
    ventana,
    text="Introduce un precio para empezar.",
    font=FONT_NORMAL,
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    wraplength=300
)
etiqueta_mensaje.place(x=50, y=280)

# Botones para guardar en archivos
boton_guardar_historial = tk.Button(ventana, text="Guardar Historial", command=guardar_historial, font=FONT_BOLD, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, width=15)
boton_guardar_historial.place(x=50, y=350)

boton_guardar_estadisticas = tk.Button(ventana, text="Guardar Estadísticas", command=guardar_estadisticas, font=FONT_BOLD, bg=COLOR_BOTON, fg=COLOR_BOTON_TEXTO, width=15)
boton_guardar_estadisticas.place(x=200, y=350)


# --- Bucle Principal de la Aplicación ---
ventana.mainloop()