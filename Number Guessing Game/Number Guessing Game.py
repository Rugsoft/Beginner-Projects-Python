from random import randint  # Importa la función randint para generar números aleatorios

def random_number():
    # Genera un número aleatorio entre 1 y 100
    return randint(1, 100)

def adivinar_numero():
    # Lógica principal del juego de adivinar el número
    numero_oculto = random_number()  # Número que el usuario debe adivinar
    while True:
        numero_usuario = input("Introduce un número, a ver si lo adivinas!: ")  # Solicita un número al usuario
        if numero_usuario.isdigit():  # Verifica que la entrada sea un número
            if int(numero_usuario) > numero_oculto:
                print("El número secreto es más pequeño")  # El número es menor
            elif int(numero_usuario) < numero_oculto:
                print("El números secreto es más grande")  # El número es mayor
            else:
                print("Correcto, el número era,", numero_oculto)  # Adivinó el número
                break
        else:
            print("Introduce un número, listillo!")  # Mensaje si la entrada no es un número

def main():
    # Función principal que inicia el juego
    print("\n=== Juego de adivinar un numero entre 1 y 100 ===")
    adivinar_numero()
if __name__ == "__main__":
    # Punto de entrada del programa
    main()