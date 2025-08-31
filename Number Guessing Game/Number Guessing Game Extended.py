from random import randint  # Importa la función randint para generar números aleatorios
contador = 0  # Variable global para contar los intentos
direccion_archivo = "Number Guessing Game/intentos.txt"

def random_number():
    # Genera un número aleatorio dentro del rango elegido y calcula los intentos máximos
    num1, num2 = rango_de_numeros()
    intentos = limite_intentos(num1, num2)
    return randint(num1, num2), intentos

def rango_de_numeros():
    # Solicita al usuario el rango de números para adivinar
    while True:
        n1 = input("Introduce el numero del rango de abajo: ")
        n2 = input("Introduce el numero del rango alto: ")
        if n1.isdigit() and n2.isdigit():
            return int(n1), int(n2)
        else:
            print("Alguno de los dos valores introducidos no es numerico, try again!")

def contador_de_intentos():
    # Incrementa el contador global de intentos
    global contador
    contador += 1

def limite_intentos(n1, n2):
    # Calcula el número máximo de intentos según el tamaño del rango
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

def guardar_resultado(intentos):
    # Guarda el número de intentos en el archivo especificado
    with open(direccion_archivo, "a") as file:
        file.write(str(intentos) + "\n")  # Escribe el número de intentos en una nueva línea

def mejor_intento():
    # Lee todos los intentos guardados y muestra el menor número de intentos logrado
    lista_intentos = []  # Lista para almacenar los intentos guardados
    with open(direccion_archivo) as file:
        for line in file:
            lista_intentos.append(int(line))  # Convierte cada línea a entero y la agrega a la lista
    minimo_intento = min(lista_intentos)  # Obtiene el menor valor de la lista
    print("Tu menor numero de intentos es:", minimo_intento)
            

def adivinar_numero():
    # Lógica principal del juego de adivinar el número
    numero_oculto, intentos = random_number()  # Número a adivinar y número máximo de intentos
    print(f"Tienes {intentos} intentos para adivinar el numero\n")
    while contador < intentos:
        numero_usuario = input("Introduce un número, a ver si lo adivinas!: ")  # Solicita un número al usuario
        contador_de_intentos()  # Incrementa el contador de intentos
        if numero_usuario.isdigit():  # Verifica que la entrada sea un número
            if int(numero_usuario) > numero_oculto:
                print("El número secreto es más pequeño")  # El número es menor
                print(f"Llevas {contador} intento/s, te quedan {intentos - contador}")
            elif int(numero_usuario) < numero_oculto:
                print("El números secreto es más grande")  # El número es mayor
                print(f"Llevas {contador} intento/s, te quedan {intentos - contador}")
            else:
                print(f"Correcto, el número era: {numero_oculto}")  # Adivinó el número
                print(f"Lo ha adivinado en {contador} intento/s")
                guardar_resultado(contador)
                mejor_intento()
                break
        else:
            print("Introduce un número, listillo!")  # Mensaje si la entrada no es un número
        # Comprobación de límite de intentos dentro del bucle
        if contador >= intentos:
            print(f"Has llegado al limite de intentos {intentos}, el numero era {numero_oculto}")  # Mensaje de fin de intentos
            break
    
def main():
    # Función principal que inicia el juego
    print("\n=== Juego de adivinar un numero en un rango elegido por el usuario ===\n")
    adivinar_numero()
if __name__ == "__main__":
    # Punto de entrada del programa
    main()