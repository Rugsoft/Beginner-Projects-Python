direccion_archivo = "Ejercicios TauFormar/Registro de notas/notas.txt"  # Ruta del archivo donde se guardan las notas
lista_notas_nombres = []  # Lista global que almacena diccionarios con nombre y nota de cada estudiante



def lectura_inicial():
    # Lee el archivo de notas y carga los datos en la lista global
    with open(direccion_archivo) as file:
        for linea in file:
            nombre, nota = linea.strip().split(";") 
            lista_notas_nombres.append({"nombre": nombre, "nota": nota})

def menu():
    # Muestra el menú principal y solicita una opción al usuario
    print("=== Menu Principal ===")
    print("1. Ver listado de notas")
    print("2. Añadir estudiante")
    print("3. Modificar nota")
    print("4. Consulta de aprobados")
    print("5. Media del curso")
    print("0. Salir")
    opcion = input("Introduce una opción (0-5): ")
    return opcion

def ver_lista_notas():
    # Muestra la lista de estudiantes y sus notas
    for item in lista_notas_nombres:
        print(f"Nombre: {item['nombre']}, Nota: {item['nota']}")

def añadir_estudiante():
    # Añade un nuevo estudiante si no existe ya en la lista
    nombre = input("Introduce el nombre del estudiante: ")with open(direccion_archivo, "w") as file:
        for lista in listas_productos:
    for item in lista_notas_nombres:
        if item["nombre"].lower() == nombre:
            print("El estudiante ya existe.")
            return
    nota = input("Introduce la nota del estudiante: ")
    lista_notas_nombres.append({"nombre": nombre.title(), "nota": nota})
    print("Estudiante añadido correctamente.")

def modificar_nota():
    # Modifica la nota de un estudiante si existe
    nombre = input("Introduce el nombre del estudiante cuya nota quieres modificar: ")
    for item in lista_notas_nombres:
        if item["nombre"].lower() == nombre:
            nueva_nota = float(input("Introduce la nueva nota: "))
            item["nota"] = nueva_nota
            print("Nota modificada correctamente.")
            return
    print("Estudiante no encontrado.")

def consulta_aprobados():
    # Muestra los estudiantes aprobados (nota >= 5.0)
    print("=== Estudiantes Aprobados ===")
    for item in lista_notas_nombres:
        if float(item["nota"]) >= 5.0:
            print(f"Nombre: {item['nombre']}, Nota: {item['nota']}")

def media_curso():
    # Calcula y muestra la media de las notas del curso
    if not lista_notas_nombres:
        print("No hay estudiantes registrados.")
        return
    suma = 0
    for item in lista_notas_nombres:
        suma += float(item["nota"])
    media = suma / len(lista_notas_nombres)
    print(f"Media del curso: {media:.2f}")

def guardar_cambios():
    # Guarda los cambios realizados en la lista en el archivo de notas
    with open(direccion_archivo, "w") as file:
        for item in lista_notas_nombres:
            file.write(f"{item['nombre']};{item['nota']}\n")

def main():
    # Bucle principal del programa que gestiona el menú y las opciones
    finW = True
    while finW:
        opcion = menu()
        match opcion:
            case "1":
                ver_lista_notas()
            case "2":
                añadir_estudiante()
            case "3":
                modificar_nota()
            case "4":
                consulta_aprobados()
            case "5":
                media_curso()
            case "0":
                print("Saliendo del programa...")
                guardar_cambios()
                finW = False
            case _:
                print("Opción no válida")
                 
if __name__ == "__main__":
    # Punto de entrada del programa
    lectura_inicial()
    main()