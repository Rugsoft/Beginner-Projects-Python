import qrcode
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk # NUEVO: Importamos el módulo para widgets modernos

# --- Variables Globales ---
carpeta = ""

# --- Diccionario de Colores Disponibles ---
# NUEVO: (Nombre amigable: código hexadecimal)
colores_disponibles = {
    "Negro": "#000000",
    "Blanco": "#FFFFFF",
    "Azul Marino": "#000080",
    "Verde Oscuro": "#006400",
    "Rojo Oscuro": "#8B0000",
    "Gris": "#808080",
    "Amarillo": "#FFFF00",
    "Cian": "#00FFFF",
}

# --- Funciones ---
def seleccionar_carpeta():
    global carpeta
    ruta_seleccionada = filedialog.askdirectory()
    if ruta_seleccionada:
        carpeta = ruta_seleccionada
        actualizar_mensaje(f"Carpeta seleccionada: {carpeta}", "#0000ff")
    else:
        actualizar_mensaje("No se seleccionó ninguna carpeta.", "#ff0000")

def generar_qr():
    if not carpeta:
        actualizar_mensaje("Error: ¡Primero debes seleccionar una carpeta!", "#ff0000")
        return

    data = entrada_datos.get()
    
    if not data:
        actualizar_mensaje("Error: ¡Debes introducir texto o una URL!", "#ff0000")
        return
        
    # NUEVO: Obtenemos los colores seleccionados de los desplegables
    nombre_color_qr = variable_color_qr.get()
    nombre_color_fondo = variable_color_fondo.get()
    color_qr = colores_disponibles[nombre_color_qr]
    color_fondo = colores_disponibles[nombre_color_fondo]

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # NUEVO: Usamos las variables con los códigos de color
    img = qr.make_image(fill_color=color_qr, back_color=color_fondo)

    try:
        ruta_guardado = f"{carpeta}/qr_personalizado.png"
        img.save(ruta_guardado)
        actualizar_mensaje(f"QR guardado en: {ruta_guardado}", "#008000")
    except Exception as e:
        actualizar_mensaje(f"Error al guardar: {e}", "#ff0000")
    
def actualizar_mensaje(texto, color):
    etiqueta_mensaje.config(text=texto, fg=color)

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Generador de QR's Personalizado")
ventana.geometry("450x400") # Aumentamos la altura para los nuevos widgets
ventana.configure(bg="#f0f0f0")

etiqueta_info = tk.Label(ventana, text="Introduce la frase o URL para generar el QR:", bg="#f0f0f0")
etiqueta_info.pack(pady=10)

entrada_datos = tk.Entry(ventana, width=50)
entrada_datos.pack(pady=5)

# NUEVO: Desplegables para seleccionar colores
etiqueta_color_qr = tk.Label(ventana, text="Color del QR:", bg="#f0f0f0")
etiqueta_color_qr.pack(pady=(10,0))
variable_color_qr = tk.StringVar(value="Negro")
desplegable_color_qr = ttk.Combobox(
    ventana, textvariable=variable_color_qr,
    values=list(colores_disponibles.keys()), state="readonly"
)
desplegable_color_qr.pack(pady=2)

etiqueta_color_fondo = tk.Label(ventana, text="Color del Fondo:", bg="#f0f0f0")
etiqueta_color_fondo.pack(pady=(10,0))
variable_color_fondo = tk.StringVar(value="Blanco")
desplegable_color_fondo = ttk.Combobox(
    ventana, textvariable=variable_color_fondo,
    values=list(colores_disponibles.keys()), state="readonly"
)
desplegable_color_fondo.pack(pady=10)

boton_seleccionar = tk.Button(ventana, text="1. Seleccionar Carpeta de Destino", command=seleccionar_carpeta)
boton_seleccionar.pack(pady=5)

boton_generar = tk.Button(ventana, text="2. Generar QR", command=generar_qr)
boton_generar.pack(pady=10)

etiqueta_mensaje = tk.Label(ventana, text="Bienvenido. Selecciona una carpeta para empezar.", bg="#f0f0f0", wraplength=400)
etiqueta_mensaje.pack(pady=10)

ventana.mainloop()
