import os

# Es una buena práctica definir la ruta del archivo en una variable.
path_archivo = "temperaturas.txt"

# Las listas globales para almacenar los datos.
temperaturas_maximas = []
temperaturas_minimas = []

def crear_documento():
    
    #Crea el archivo de texto inicial si no existe.

    temperaturas_str = "30 15,29 12,32 16,30 14,28 10"
    
    if os.path.exists(path_archivo):
        print(f"El archivo '{path_archivo}' ya existe. No se creará uno nuevo.")
        return

    try:
        with open(path_archivo, "w") as archivo:
            contenido = temperaturas_str.replace(",", "\n")
            archivo.write(contenido)
        print(f"Archivo '{path_archivo}' creado con éxito.")
    except IOError as e:
        print(f"Error al crear el archivo: {e}")

def leer_documento():
    
    #Lee el documento y carga las temperaturas en las listas globales.

    temperaturas_maximas.clear()
    temperaturas_minimas.clear()
    
    try:
        with open(path_archivo) as archivo:
            for linea in archivo:
                partes = linea.strip().split()
                if len(partes) == 2:
                    temperaturas_maximas.append(int(partes[0]))
                    temperaturas_minimas.append(int(partes[1]))
            print("Documento leído y procesado correctamente.")
            print(f"Temperaturas máximas: {temperaturas_maximas}")
            print(f"Temperaturas mínimas: {temperaturas_minimas}")
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{path_archivo}'. Ejecuta crear_documento() primero.")
    except ValueError:
        print("Error: El archivo contiene valores que no son números. Revisa el formato.")

def calcular_promedios():
    """Calcula y muestra el promedio de las temperaturas máximas y mínimas."""
    if not temperaturas_maximas or not temperaturas_minimas:
        print("No hay datos para calcular promedios. Lee el documento primero.")
        return

    promedio_max = sum(temperaturas_maximas) / len(temperaturas_maximas)
    promedio_min = sum(temperaturas_minimas) / len(temperaturas_minimas)
    
    print("\n--- Promedios de Temperatura ---")
    print(f"Promedio de máximas: {promedio_max:.2f} °C")
    print(f"Promedio de mínimas: {promedio_min:.2f} °C")

if __name__ == "__main__":
    crear_documento()
    print("-" * 20)
    leer_documento()
    print("-" * 20)
    calcular_promedios()