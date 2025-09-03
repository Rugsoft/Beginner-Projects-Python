preguntas = [
    {
        "pregunta": "¿Qué es un archivo .BAT?",
        "opciones": "a) Un archivo binario ejecutable b) Un archivo de texto plano con secuencia de comandos para CMD c) Un lenguaje compilado d) Una aplicación gráfica",
        "correcta": "b"
    },
    {
        "pregunta": "¿Cuál es la función del comando @echo off en un script batch?",
        "opciones": "a) Ejecutar los comandos en segundo plano b) Mostrar todos los comandos en pantalla c) Ocultar la muestra de comandos mientras se ejecuta el script d) Detener la ejecución del script",
        "correcta": "c"
    },
    {
        "pregunta": "¿Cómo se declara una variable en un archivo .BAT?",
        "opciones": "a) var = valor b) set var=valor c) declare var valor d) %var = valor%",
        "correcta": "b"
    },
    {
        "pregunta": "¿Cuál de estos comandos se usa para pausar la ejecución y esperar que el usuario pulse una tecla?",
        "opciones": "a) stop b) pause c) wait d) halt",
        "correcta": "b"
    },
    {
        "pregunta": "Para llamar a una sección del script definida con una etiqueta, se utiliza el comando:",
        "opciones": "a) goto etiqueta b) call etiqueta c) exit etiqueta d) start etiqueta",
        "correcta": "a"
    },
    {
        "pregunta": "¿Qué hace el comando xcopy con el modificador /s?",
        "opciones": "a) Copia solo archivos de sistema b) Copia subdirectorios, excepto los vacíos c) Sobrescribe todos los archivos sin confirmación d) Crea un script nuevo automáticamente",
        "correcta": "b"
    },
    {
        "pregunta": "¿Qué comando permite mostrar una lista de procesos en ejecución en Windows desde un script batch?",
        "opciones": "a) proc list b) tasklist c) ps d) processes",
        "correcta": "b"
    },
    {
        "pregunta": "¿Cómo se detiene un servicio de Windows desde un script .BAT?",
        "opciones": "a) service stop NombreServicio b) net stop NombreServicio c) stop service NombreServicio d) shutdown NombreServicio",
        "correcta": "b"
    },
    {
        "pregunta": "Si quieres mostrar un mensaje en pantalla dentro de un archivo batch, se utiliza:",
        "opciones": "a) print b) echo c) show d) message",
        "correcta": "b"
    },
    {
        "pregunta": "¿Qué comando se utiliza para redirigir la salida de un comando a un fichero, sobrescribiendo su contenido?",
        "opciones": "a) > b) < c) >> d) |",
        "correcta": "a"
    } 
]

puntuacion = 0
    
print("¡Bienvenido al Quiz de Programación Básica!")
print("------------------------------------------")

for pregunta in preguntas:
    print(pregunta["pregunta"])
    print(pregunta["opciones"])
    respuesta = input("Selecciona una opción (a/b/c/d): ")
    if respuesta == pregunta["correcta"]:
        print("¡Correcto!")
        puntuacion += 1
    else:
        print("Incorrecto.")
    print()

print(f"Tu puntuación final es: {puntuacion}/{len(preguntas)}")