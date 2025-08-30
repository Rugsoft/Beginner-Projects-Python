import random  # Importa el módulo random para generar números aleatorios

def roll_dice():
    # Lanza dos dados de seis caras y retorna sus valores
    d1 = random.randint(1, 6)  # Primer dado
    d2 = random.randint(1, 6)  # Segundo dado
    return d1, d2

def main():
    # Función principal que controla el flujo del juego
    while True:
        choice = input("Quieres tirar los dados? S/N: ")  # Pregunta al usuario si quiere lanzar los dados
        if choice.lower() == "s":
            d1, d2 = roll_dice()  # Llama a la función para lanzar los dados
            print(f"{d1}, {d2}")  # Muestra el resultado de los dados
        elif choice.lower() == "n":
            print("Saliendo del dado...")  # Mensaje de salida
            break
        else:
            print("Opción incorrecta")  # Mensaje si la opción no es válida
            
if __name__ == "__main__":
    # Punto de entrada del programa
    main()

