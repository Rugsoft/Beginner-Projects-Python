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
    pass
    
  
def main():
    print("                        =====  QUIZ GAME  =====")
    cantidad, categoria, dificultad = solicitar_datos()
    preguntas = solicitar_preguntas(cantidad, categoria, dificultad)
    print(preguntas)


if __name__ == "__main__":
    main()