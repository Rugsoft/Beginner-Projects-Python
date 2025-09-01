# Importa la librería para usar emojis
import emoji
# Importa la función choice para selección aleatoria
from random import choice

# Lista de opciones posibles para la máquina (l=papel, p=piedra, t=tijera)
mano_maquina = ["l", "p", "t"]

def juego():
    # Función principal del juego
    while True:
        print("=== Bienvenido al juego de Piedra, papel o tijera ===")
        humano = input("\nIntroduce: 'l'= Papel 📄 - 'p'= Piedra 🪨 - 't'= Tijera ✂️ : ")  # Obtiene la elección del jugador
        maquina = choice(mano_maquina)  # Obtiene una elección aleatoria para la máquina
        icono_h, icono_m = emoji_convertidor(humano, maquina)  # Convierte las elecciones a emojis
        resultado = logica_juego(humano, maquina)  # Determina el ganador
        if resultado:
            print(f"Sacaste {icono_h}  - La maquina {icono_m}, has ganado!!")
        elif not resultado:
            print(f"Sacaste {icono_h}  - La maquina {icono_m}, has perdido!!")
        else:
            print(f"Sacaste {icono_h}  - La maquina {icono_m}, habeis empatado")
        respuesta = input("Quieres continuar (s/n): ")
        if respuesta.lower() == "n":
            print("Vale, hasta otra!!")
            break
    
    
def emoji_convertidor(p, m):
    # Convierte las elecciones de letra a emoji
    # p: elección del jugador, m: elección de la máquina
    if p == "l":
        p = emoji.emojize("Papel 📄", language="alias")
    elif p == "p":
        p = emoji.emojize("Piedra 🪨", language="alias")
    elif p == "t":
        p = emoji.emojize("Tijera ✂️", language="alias")

    if m == "l":
        m = emoji.emojize("Papel 📄", language="alias")
    elif m == "p":
        m = emoji.emojize("Piedra 🪨", language="alias")
    elif m == "t":
        m = emoji.emojize("Tijera ✂️", language="alias")

    return p, m


def logica_juego(p, m):
    # Determina el ganador según las reglas del juego
    # p: elección del jugador, m: elección de la máquina
    # Retorna: True si gana el jugador, False si pierde, "empate" si empatan
    if (p == "l" and m == "p") or (p == "p" and m == "r") or (p == "t" and m == "l"):
        return True
    elif (p == "l" and m == "t") or (p == "p" and m == "l") or (p == "t" and m == "p"):
        return False
    else:
        return "empate"
    
if __name__ == "__main__":
    # Punto de entrada del programa
    juego()