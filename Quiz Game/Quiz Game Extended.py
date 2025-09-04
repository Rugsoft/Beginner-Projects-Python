import requests
import json
import random
import html

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


def solicitar_preguntas(cantidad, categoria, dificultad):
    
    url = f"https://opentdb.com/api.php?amount={cantidad}&category={categoria}&difficulty={dificultad}&type=multiple"
    
    try:
        respuesta_API = requests.get(url)
        respuesta_API.raise_for_status()
        datos_preguntas = json.loads(respuesta_API.text)
        return datos_preguntas["results"]
    
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return None

def solicitar_datos():
    while True:
        try:
            question_amount = int(input("Introduce el numero de preguntas que quieres constestar: "))
            print("Elige una de las siguientes categorias")
            print("=" * 25)
            for num, categoria in categorias.items():
                print(num, categoria)
            question_category = int(input("Elige escribiendo el numero: "))
            dificulty = input("Elige una dificultad (easy, medium, hard): ")
            return question_amount, question_category, dificulty
        except ValueError:
            print("Valores incorrectos, vuelve a rellenarlo")

def quiz_game(datos):
    puntuacion = 0
    
    for i, dato in enumerate(datos):
        pregunta = html.unescape(dato["question"])
        respuesta_correcta = html.unescape(dato["correct_answer"])
        respuestas_incorrectas = [html.unescape(r) for r in dato["incorrect_answers"]]
        
        opciones = respuestas_incorrectas + [respuesta_correcta]
        random.shuffle(opciones)
        
        print(f"\n{i+1}- {pregunta}")
        for n, opcion in enumerate(opciones):
            print(f"    {n+1}. {opcion}")
        
        while True:
            try:
                respuesta_usuario = int(input("Introduce el numero de la respuesta: "))
                if respuesta_usuario >= 1 and respuesta_usuario <= len(opciones):
                    break
                else:
                    print("Introduce un numero válido!")
            except ValueError:
                print("Introduce un numero!")
        
        respuesta_usuario = opciones[respuesta_usuario - 1]
        
        if respuesta_usuario == respuesta_correcta:
            puntuacion += 1
            print("Respuesta correcta")
        else:
            print(f"Respuesta incorrecta, la correcta era: {respuesta_correcta}")
    
    print(f"Juegos Finalizado!! Has sacado un {puntuacion}/{len(datos)}")
    
  
def main():
    print("\n                        =====  QUIZ GAME  =====")
    cantidad, categoria, dificultad = solicitar_datos()
    preguntas = solicitar_preguntas(cantidad, categoria, dificultad)
    quiz_game(preguntas)


if __name__ == "__main__":
    main()