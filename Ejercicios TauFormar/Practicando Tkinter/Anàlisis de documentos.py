import tkinter as tk
from tkinter import messagebox

texto = "Zombie ipsum reversus ab viral inferno, nam rick grimes malum cerebro. De carne lumbering animata corpora quaeritis. Summus brains sit, morbo vel maleficia? De apocalypsi gorger omero undead survivor dictum mauris. Hi mindless mortuis soulless creaturas, imo evil stalking monstra adventus resi dentevil vultus comedat cerebella viventium. Qui animated corpse, cricket bat max brucks terribilem incessu zomby. The voodoo sacerdos flesh eater, suscitat mortuos comedere carnem virus. Zonbi tattered for solum oculi eorum defunctis go lum cerebro. Nescio brains an Undead zombies. Sicut malus putrid voodoo horror. Nigh tofth eliv ingdead."
lista_palabras = []

def crear_documento():
    """Crea el archivo de texto inicial."""
    with open("documento.txt", "w", encoding="utf-8") as archivo:
        archivo.write(texto)

def leer_documento():
    """Lee el documento y carga las palabras en una lista global."""
    global lista_palabras
    try:
        with open("documento.txt", "r", encoding="utf-8") as archivo:
            contenido_completo = archivo.read()
            # Primero dividimos el texto en una lista de palabras
            lista_palabras = contenido_completo.split()
            # Luego, eliminamos los caracteres no alfabéticos de cada palabra
            lista_palabras = [palabra.strip("\n, .,?") for palabra in lista_palabras]
            messagebox.showinfo("Éxito", "El documento ha sido leído y procesado correctamente.")
    except FileNotFoundError:
        messagebox.showerror("Error", "No se encontró el archivo 'documento.txt'. Asegúrate de crearlo primero.")


def analizar_documento():
    """Analiza la lista de palabras y devuelve los contadores."""
    global lista_palabras
    if not lista_palabras:
        messagebox.showwarning("Advertencia", "La lista de palabras está vacía. Por favor, lee el documento primero.")
        return None, None, None

    # Contar todas las palabras
    palabras_totales = len(lista_palabras)
    # Contador de letras
    letras = [len(palabra) for palabra in lista_palabras]
    letras_totales = sum(letras)
    # Contador de vocales
    vocales = "aeiouAEIOU" # Incluimos mayúsculas
    total_vocales = 0
    for palabra in lista_palabras:
        for letra in palabra:
            if letra in vocales:
                total_vocales += 1
    
    # Mostramos el resultado en una ventana emergente
    resultado = f"Palabras totales: {palabras_totales}\nLetras totales: {letras_totales}\nVocales totales: {total_vocales}"
    messagebox.showinfo("Análisis Completado", resultado)

    return palabras_totales, letras_totales, total_vocales

def guardar_analisis():
    """Guarda los resultados del análisis en un nuevo archivo."""
    # Primero nos aseguramos de que haya algo que analizar
    if not lista_palabras:
        messagebox.showwarning("Advertencia", "No hay nada que analizar. Por favor, lee el documento primero.")
        return

    pt, lt, tv = analizar_documento()
    # Si el análisis no devuelve nada (porque la lista estaba vacía), no continuamos.
    if pt is None:
        return
        
    cadena = f"Palabras totales: {pt} - Letras totales: {lt} - Vocales totales: {tv}"
    with open("resultadoanalisis.txt", "w", encoding="utf-8") as archivo:
        archivo.write(cadena)
    messagebox.showinfo("Guardado", "El análisis se ha guardado en 'resultadoanalisis.txt'.")


def main():
    # Aseguramos que el documento base exista al iniciar
    crear_documento()

    # --- Configuración de la ventana principal ---
    ventana = tk.Tk()
    ventana.title("Analizador de Texto")
    ventana.geometry("300x250")
    ventana.resizable(False, False)

    # --- Creación de los widgets (botones) ---
    titulo = tk.Label(ventana, text="Analizador de Archivos", font=("Helvetica", 16))
    
    # El comando de cada botón llama a la función correspondiente
    boton_leer = tk.Button(ventana, text="1. Leer Texto", command=leer_documento, width=20, height=2)
    boton_analizar = tk.Button(ventana, text="2. Analizar Texto", command=analizar_documento, width=20, height=2)
    boton_guardar = tk.Button(ventana, text="3. Guardar Resultados", command=guardar_analisis, width=20, height=2)

    # --- Posicionamiento de los widgets en la ventana ---
    titulo.pack(pady=15)
    boton_leer.pack(pady=5)
    boton_analizar.pack(pady=5)
    boton_guardar.pack(pady=5)

    # --- Bucle principal de la aplicación ---
    # Esto mantiene la ventana abierta y a la espera de interacciones del usuario
    ventana.mainloop()


if __name__ == "__main__":
    main()