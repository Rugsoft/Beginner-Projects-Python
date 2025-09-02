# Importa la librería para usar emojis
import emoji
# Importa la función choice para selección aleatoria
from random import choice

# Lista de opciones posibles para la máquina (l=papel, p=piedra, t=tijera)
mano_maquina = ["l", "p", "t"]
# Diccionario que mapea las opciones con sus emojis correspondientes
emojis = {"l": "📄", "p": "🪨", "t": "✂️"}
# Diccionario para almacenar el conteo de resultados del juego
resultados_juego = {"Has ganado": 0, "Has perdido": 0, "Empate": 0}
# Contador de victorias del jugador en la serie actual (mejor de 3)
win_condition_human = 0
# Contador de victorias de la máquina en la serie actual (mejor de 3)
win_condition_machine = 0

def juego():
    # Función principal del juego
    global win_condition_human
    global win_condition_machine
    while True:
        print("=== Bienvenido al juego de Piedra, papel o tijera ===")
        humano = input("\nIntroduce: 'l'= Papel 📄 - 'p'= Piedra 🪨 - 't'= Tijera ✂️ : ")  # Obtiene la elección del jugador
        maquina = choice(mano_maquina)  # Obtiene una elección aleatoria para la máquina
        resultado = logica_juego(humano, maquina)  # Determina el resultado de la partida
        print(f"Tu has sacado {emojis[humano]}  y el ordenador ha sacado {emojis[maquina]}. {resultado}")  # Muestra el resultado con emojis
        condicion_ganadora(resultado)  # Actualiza los contadores de la serie actual
        # Verifica si el jugador ha ganado la serie (2 de 3)
        if win_condition_human == 2:
            print("Has ganado 2 de 3 rondas!")
            win_condition_human = 0  # Reinicia los contadores para la siguiente serie
            win_condition_machine = 0
        # Verifica si la máquina ha ganado la serie (2 de 3)
        elif win_condition_machine == 2:
            print("Ha ganado la maquina 2 de 3 rondas!")
            win_condition_human = 0  # Reinicia los contadores para la siguiente serie
            win_condition_machine = 0
        print("\n== Resultados globales ==")
        print(f"""
              Has ganado: {resultados_juego["Has ganado"]}
              Has perdido: {resultados_juego["Has perdido"]}
              Empate: {resultados_juego["Empate"]}
              """)
        respuesta = input("Quieres continuar (s/n): ")  # Pregunta si quiere jugar otra vez
        if respuesta.lower() == "n":
            print("Vale, hasta otra!!")
            break

def condicion_ganadora(resul):
    # Actualiza el contador de rondas ganadas por el humano o la máquina
    global win_condition_machine
    global win_condition_human
    if resul == "Has ganado":
        win_condition_human += 1
    elif resul == "Has perdido":
        win_condition_machine += 1
    # No se actualiza nada en caso de empate

def logica_juego(p, m):
    # Determina el ganador según las reglas del juego
    # p: elección del jugador, m: elección de la máquina
    # Retorna: True si gana el jugador, False si pierde, "empate" si empatan
    if p == m:
        # Si ambos eligen lo mismo, es empate
        resultados_juego["Empate"] += 1
        return "Empate"  # Si ambos eligen lo mismo
    elif ((p == "l" and m == "p") or  # Papel gana a Piedra
          (p == "p" and m == "r") or  # Piedra gana a Tijera
          (p == "t" and m == "l")):   # Tijera gana a Papel
        # El jugador gana la ronda
        resultados_juego["Has ganado"] += 1
        return "Has ganado"
    else:
        # El jugador pierde la ronda
        resultados_juego["Has perdido"] += 1
        return "Has perdido"
    # No hay más casos posibles
if __name__ == "__main__":
    # Ejecuta el juego si el archivo se ejecuta directamente
    juego()