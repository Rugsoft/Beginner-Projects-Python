from random import randint  # Importa la función randint para generar números aleatorios
contador = 0

def random_number():
    num1, num2 = rango_de_numeros()
    intentos = limite_intentos(num1, num2)
    return randint(num1, num2), intentos

def rango_de_numeros():
    while True:
        n1 = input("Introduce el numero del rango de abajo: ")
        n2 = input("Introduce el numero del rango alto: ")
        if n1.isdigit() and n2.isdigit():
            return int(n1), int(n2)
        else:
            print("Alguno de los dos valores introducidos no es numerico, try again!")

def contador_de_intentos():
    global contador
    contador += 1

def limite_intentos(n1, n2):
    diferencia = n2 - n1
    if diferencia <= 50:
        intentos_max = 10
    elif diferencia > 50 and diferencia <= 100:
        intentos_max = 15
    elif diferencia > 100 and diferencia <= 150:
        intentos_max = 20
    elif diferencia > 150 and diferencia <= 200:
        intentos_max = 25
    else:
        intentos_max = 30
    return intentos_max
    
def adivinar_numero():
    numero_oculto, intentos = random_number()  
    print(f"Tienes {intentos} intentos para adivinar el numero\n")
    while contador < intentos:
        numero_usuario = input("Introduce un número, a ver si lo adivinas!: ") 
        contador_de_intentos()
        if numero_usuario.isdigit():
            if int(numero_usuario) > numero_oculto:
                print("El número secreto es más pequeño")
                print(f"Llevas {contador} intento/s, te quedan {intentos - contador}")
            elif int(numero_usuario) < numero_oculto:
                print("El números secreto es más grande")
                print(f"Llevas {contador} intento/s, te quedan {intentos - contador}")
            else:
                print(f"Correcto, el número era: {numero_oculto}")
                print(f"Lo ha adivinado en {contador} intento/s")
                break
        else:
            print("Introduce un número, listillo!")
        # Comprobación de límite de intentos dentro del bucle
        if contador >= intentos:
            print(f"Has llegado al limite de intentos {intentos}, el numero era {numero_oculto}")
            break
    
def main():
    # Función principal que inicia el juego
    print("\n=== Juego de adivinar un numero en un rango elegido por el usuario ===\n")
    adivinar_numero()
    
if __name__ == "__main__":
    # Punto de entrada del programa
    main()