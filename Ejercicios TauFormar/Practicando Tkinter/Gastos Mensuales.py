import tkinter as tk
from tkinter import messagebox

gastos = {}

# --- Paleta de Colores y Fuentes ---
COLOR_FONDO = "#2C3E50"
COLOR_TEXTO = "#ECF0F1"
COLOR_INPUT_FONDO = "#34495E"
COLOR_BOTON = "#3498DB"
COLOR_BOTON_TEXTO = "#FFFFFF"
COLOR_ETIQUETA_RESULTADO = "#2ECC71"
COLOR_MENSAJE_ERROR = "#E74C3C"

FONT_NORMAL = ("Consolas", 12)
FONT_BOLD = ("Consolas", 12, "bold")
FONT_RESULTADO = ("onsolas", 16, "bold")

def guardar_datos():
    
    concepto = entrada_concepto.get()
    gasto = float(entrada_gasto.get())
    gastos[concepto] = gasto
    with open("gastos.txt", "a") as f:
        f.write(f"{concepto},{gasto}\n")
    entrada_gasto.delete(0, tk.END)
    entrada_concepto.delete(0, tk.END)
    actualizar_mensaje(f"Guardado {concepto}: {gasto:.2f} €", COLOR_ETIQUETA_RESULTADO)

def actualizar_mensaje(texto, color):
    """
    Actualiza el texto y color de la etiqueta de mensajes/feedback.
    """
    etiqueta_mensaje.config(text=texto, fg=color)

def calcular_total():
    total = sum(gastos.values())
    messagebox.showinfo("Calculo realizado")
    actualizar_mensaje(f"Total: {total:.2f} €", COLOR_ETIQUETA_RESULTADO)
    

def main():
    pass
    


if __name__=="__main__":
        # --- Configuración de la Ventana Principal ---
    ventana = tk.Tk()
    ventana.title("Calculadora - Gastos Mensuales")
    ventana.geometry("400x300")
    ventana.configure(bg=COLOR_FONDO)
    
    etiqueta_info = tk.Label(
    ventana,
    text="Introduce concepto y gasto:",
    font=FONT_NORMAL,
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO
    )
    etiqueta_info.place(x=50, y=40)

    entrada_concepto = tk.Entry(
    ventana,
    font=FONT_NORMAL,
    width=20,
    bg=COLOR_INPUT_FONDO,
    fg=COLOR_TEXTO,
    insertbackground=COLOR_TEXTO, # Color del cursor
    borderwidth=2,
    relief="groove"
    )
    entrada_concepto.place(x=50, y=70)
    
    entrada_gasto = tk.Entry(
    ventana,
    font=FONT_NORMAL,
    width=20,
    bg=COLOR_INPUT_FONDO,
    fg=COLOR_TEXTO,
    insertbackground=COLOR_TEXTO, # Color del cursor
    borderwidth=2,
    relief="groove"
    )
    entrada_gasto.place(x=50, y=105)
    
    boton_añadir = tk.Button(
    ventana,
    text="Añadir",
    command=guardar_datos,
    font=FONT_BOLD,
    bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    width=10,
    relief="raised",
    borderwidth=2
    )
    boton_añadir.place(x=250, y=85)
    
    boton_calcular = tk.Button(
    ventana,
    text="Calcular Total",
    command=calcular_total,
    font=FONT_BOLD,
    bg=COLOR_BOTON,
    fg=COLOR_BOTON_TEXTO,
    width=15,
    relief="raised",
    borderwidth=2
    )
    boton_calcular.place(x=125, y=225)
    
    etiqueta_mensaje = tk.Label(
    ventana,
    text="Introduce un concepto y un gasto para empezar.",
    font=FONT_NORMAL,
    bg=COLOR_FONDO,
    fg=COLOR_TEXTO,
    wraplength=300
    )
    etiqueta_mensaje.place(x=50, y=160)
    
    ventana.mainloop()