from random import randint  # Importa la función randint para generar números aleatorios entre dos valores

def roll_dice(dice):
    # Lanza la cantidad de dados especificada y retorna una lista con los resultados
    dice_list = []  # Lista para almacenar los resultados de cada dado
    for d in range(dice):
        dice_list.append(randint(1, 6))  # Agrega el resultado de un dado (1 a 6)
    return dice_list
    
def numero_de_dados():
    # Solicita al usuario la cantidad de dados a lanzar y valida que sea un número
    while True:
        dice = input("¿Cuantos D6 quieres lanzar?: ")  # Pide al usuario la cantidad de dados
        if dice.isdigit():
            return int(dice)  # Retorna el número de dados si la entrada es válida
        else:
            print("No es un numero, vuelve a intentarlo")  # Mensaje de error si no es número
    
def main():
    # Función principal que controla el flujo del juego
    while True:
        choice = input("Quieres lanzar los dados? S/N: ")  # Pregunta al usuario si quiere lanzar los dados
        if choice.lower() == "s":
            dice = numero_de_dados()  # Obtiene la cantidad de dados a lanzar
            dice_list = roll_dice(dice)  # Lanza los dados y obtiene los resultados
            for i, d in enumerate(dice_list):
                print(f"Dado {i+1} = {d}")  # Muestra el resultado de cada dado
        elif choice.lower() == "n":
            print("Saliendo del dado...")  # Mensaje de salida
            break
        else:
            print("Opción incorrecta")  # Mensaje si la opción no es válida
            
if __name__ == "__main__":
    # Punto de entrada del programa
    main()

