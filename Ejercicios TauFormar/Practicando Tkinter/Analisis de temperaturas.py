temperaturas = "30 15,29 12,32 16,30 14,28 10"
temperaturas_maximas = []
temperaturas_minimas = []

def crear_documento():
    """Crea el archivo de texto inicial."""
    with open("temperaturas.txt", "w") as archivo:
        for letra in temperaturas:
            if letra == ",":
                archivo.write("\n")
            else:
                archivo.write(letra)



if __name__ == "__main__":
    crear_documento()