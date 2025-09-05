# === Importación de Librerías ===
# Se importan las librerías necesarias para el funcionamiento del programa.
import requests  # Para realizar peticiones a la API a través de internet.
import json      # Para "traducir" la respuesta de la API (en formato JSON) a un diccionario de Python.
import random    # Para barajar las opciones de respuesta de forma aleatoria.
import html      # Para decodificar caracteres especiales de HTML (ej: &quot; por ") que puedan venir en las preguntas.

# === Datos Estáticos ===
# Un diccionario que mapea el número de categoría de la API a un nombre legible por humanos.
# Facilita que el usuario elija una categoría sin tener que saber su número de identificación.
categorias = {
    9: "General Knowledge",
    10: "Books",
    11: "Film",
    12: "Music",
    13: "Musicals & Theatres",
    14: "Television",
    15: "Video Games",
    16: "Board Games",
    17: "Science & Nature",
    18: "Computers",
    19: "Mathematics",
    20: "Mythology",
    21: "Sports",
    22: "Geography",
    23: "History",
    24: "Politics",
    25: "Art",
    26: "Celebrities",
    27: "Animals",
    28: "Vehicles",
    29: "Comics",
    30: "Gadgets",
    31: "Anime & Manga",
    32: "Cartoons"
}

# === Definición de Funciones ===

def solicitar_preguntas(cantidad, categoria, dificultad):
    """
    Se conecta a la API de OpenTriviaDB para obtener las preguntas.
    
    Argumentos:
        cantidad (int): El número de preguntas a solicitar.
        categoria (int): El ID de la categoría de las preguntas.
        dificultad (str): La dificultad de las preguntas ('easy', 'medium', 'hard').
        
    Returns:
            list: Una lista de diccionarios, donde cada diccionario es una pregunta.
              Retorna None si hay un error de conexión.
    """
    # Se construye la URL de la API usando un f-string para insertar los parámetros del usuario.
    url = f"https://opentdb.com/api.php?amount={cantidad}&category={categoria}&difficulty={dificultad}&type=multiple"
    
    # Se usa un bloque try/except para manejar posibles errores de red de forma segura.
    try:
        # Se realiza la petición GET a la URL.
        respuesta_API = requests.get(url)
        # Se comprueba si la petición fue exitosa (códigos 2xx). Si no, lanza un error.
        respuesta_API.raise_for_status()
        # Se convierte el texto de la respuesta (en formato JSON) a una estructura de Python (diccionarios y listas).
        datos_preguntas = json.loads(respuesta_API.text)
        # La API devuelve un diccionario principal; las preguntas están dentro de la clave "results".
        return datos_preguntas["results"]
    
    # Si ocurre cualquier error durante la petición (mala conexión, URL incorrecta, etc.), se captura aquí.
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

def solicitar_datos():
    """
    Interactúa con el usuario para obtener la configuración del juego (cantidad, categoría, dificultad).
    Valida que los datos introducidos sean correctos.
    
    Returns:
        tuple: Una tupla conteniendo la cantidad, categoría y dificultad elegidas.
    """
    # Un bucle infinito que solo se romperá cuando el usuario introduzca datos válidos.
    while True:
        # Bloque try/except para capturar errores si el usuario no introduce un número.
        try:
            question_amount = int(input("Introduce el numero de preguntas que quieres constestar: "))
            
            print("\nElige una de las siguientes categorias")
            print("=" * 30)
            # Se itera sobre el diccionario de categorías para mostrarlas de forma amigable.
            for num, categoria in categorias.items():
                print(f"{num}: {categoria}")
            print("=" * 30)
            
            question_category = int(input("Elige escribiendo el numero: "))
            dificulty = input("Elige una dificultad (easy, medium, hard): ").lower() # .lower() para aceptar mayúsculas
            
            # Si todas las entradas son correctas, se devuelven los valores y se rompe el bucle.
            return question_amount, question_category, dificulty
        
        # Si el usuario introduce texto donde se espera un número, se captura el ValueError.
        except ValueError:
            print("\nValores incorrectos, vuelve a rellenarlo. Recuerda usar números para la cantidad y categoría.\n")

def quiz_game(datos):
    """
    Función principal que ejecuta la lógica del juego de preguntas.
    
    Args:
        datos (list): La lista de preguntas obtenida de la API.
    """
    # Se inicializa la puntuación del jugador a 0.
    puntuacion = 0
    
    # Se itera sobre la lista de preguntas. 'enumerate' nos da tanto el índice (i) como el elemento (dato).
    for i, dato in enumerate(datos):
        # Se decodifican los textos para mostrarlos correctamente.
        pregunta = html.unescape(dato["question"])
        respuesta_correcta = html.unescape(dato["correct_answer"])
        respuestas_incorrectas = [html.unescape(r) for r in dato["incorrect_answers"]]
        
        # Se crea una lista única con todas las opciones (correcta e incorrectas).
        opciones = respuestas_incorrectas + [respuesta_correcta]
        # Se baraja la lista para que la respuesta correcta no esté siempre en la misma posición.
        random.shuffle(opciones)
        
        # Se muestra la pregunta al usuario. El `i+1` es para empezar a contar desde 1.
        print(f"\n{i+1}- {pregunta}")
        # Se muestran todas las opciones numeradas.
        for n, opcion in enumerate(opciones):
            print(f"    {n+1}. {opcion}")
        
        # Bucle de validación para la respuesta del usuario.
        while True:
            try:
                # Se solicita al usuario el número de la respuesta.
                respuesta_usuario_num = int(input("Introduce el numero de la respuesta: "))
                # Se comprueba si el número está dentro del rango de opciones válidas (1 a 4).
                if respuesta_usuario_num >= 1 and respuesta_usuario_num <= len(opciones):
                    break  # Si es válido, se rompe el bucle.
                else:
                    print("Introduce un numero válido!")
            except ValueError:
                print("Introduce un numero!")
        
        # Se convierte el NÚMERO elegido por el usuario al TEXTO de la respuesta correspondiente.
        # Se resta 1 porque las listas empiezan en el índice 0.
        respuesta_usuario_texto = opciones[respuesta_usuario_num - 1]
        
        # Se compara el texto de la respuesta del usuario con el texto de la respuesta correcta.
        if respuesta_usuario_texto == respuesta_correcta:
            puntuacion += 1  # Si acierta, se incrementa la puntuación.
            print("Respuesta correcta")
        else:
            print(f"Respuesta incorrecta, la correcta era: {respuesta_correcta}")
    
    # Al final del juego, se muestra la puntuación final.
    print(f"\nJuego Finalizado!! Has sacado un {puntuacion}/{len(datos)}")
    
  
def main():
    """
    Función principal que orquesta la ejecución del programa.
    """
    print("\n                        =====  QUIZ GAME  =====")
    # 1. Se piden los datos de configuración al usuario.
    cantidad, categoria, dificultad = solicitar_datos()
    # 2. Se solicitan las preguntas a la API con esa configuración.
    preguntas = solicitar_preguntas(cantidad, categoria, dificultad)
    # 3. Se comprueba si se recibieron las preguntas antes de iniciar el juego.
    if preguntas:
        quiz_game(preguntas)
    else:
        print("No se pudo iniciar el juego porque no se obtuvieron preguntas.")


# === Punto de Entrada del Programa ===
# Esta construcción estándar de Python asegura que la función main() solo se ejecute
# cuando el script es corrido directamente (y no cuando es importado por otro script).
if __name__ == "__main__":
    main()