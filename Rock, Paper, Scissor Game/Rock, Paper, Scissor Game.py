# Importa la librería para usar emojis
import emoji
# Importa la función choice para selección aleatoria
from random import choice

# Lista de opciones posibles para la máquina (l=papel, p=piedra, t=tijera)
mano_maquina = ["l", "p", "t"]
# Diccionario que mapea las opciones con sus emojis correspondientes
emojis = {"l": "📄", "p": "🪨", "t": "✂️"}

def juego():
    # Función principal del juego
    while True:
        print("=== Bienvenido al juego de Piedra, papel o tijera ===")
        humano = input("\nIntroduce: 'l'= Papel 📄 - 'p'= Piedra 🪨 - 't'= Tijera ✂️ : ")  # Obtiene la elección del jugador
        maquina = choice(mano_maquina)  # Obtiene una elección aleatoria para la máquina
        resultado = logica_juego(humano, maquina)  # Determina el resultado de la partida
        print(f"Tu has sacado {emojis[humano]}  y el ordenador ha sacado {emojis[maquina]}. {resultado}")  # Muestra el resultado con emojis
        respuesta = input("Quieres continuar (s/n): ")  # Pregunta si quiere jugar otra vez
        if respuesta.lower() == "n":
            print("Vale, hasta otra!!")
            break
    

def logica_juego(p, m):
    # Determina el ganador según las reglas del juego
    # p: elección del jugador, m: elección de la máquina
    # Retorna: True si gana el jugador, False si pierde, "empate" si empatan
    if p == m:
        return "Empate"  # Si ambos eligen lo mismo
    elif ((p == "l" and m == "p") or  # Papel gana a Piedra
          (p == "p" and m == "r") or  # Piedra gana a Tijera
          (p == "t" and m == "l")):   # Tijera gana a Papel
        return "Has ganado"
    else:
        return "Has perdido"
    
if __name__ == "__main__":
    # Punto de entrada del programa
    juego()