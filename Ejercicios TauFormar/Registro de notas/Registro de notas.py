direccion_archivo = "Ejercicios TauFormar/Registro de notas/notas.txt"
lista_notas_nombres = []

def lectura_inicial():
    with open(direccion_archivo) as file:
        for linea in file:
            nombre, nota = linea.strip().split(";") 
            lista_notas_nombres.append({"nombre": nombre, "nota": nota})

def menu():
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
    for item in lista_notas_nombres:
        print(f"Nombre: {item['nombre']}, Nota: {item['nota']}")

def añadir_estudiante():
    nombre = input("Introduce el nombre del estudiante: ")
    for item in lista_notas_nombres:
        if item["nombre"].lower() == nombre:
            print("El estudiante ya existe.")
            return
    nota = input("Introduce la nota del estudiante: ")
    lista_notas_nombres.append({"nombre": nombre.title(), "nota": nota})
    print("Estudiante añadido correctamente.")

def modificar_nota():
    nombre = input("Introduce el nombre del estudiante cuya nota quieres modificar: ")
    for item in lista_notas_nombres:
        if item["nombre"].lower() == nombre:
            nueva_nota = float(input("Introduce la nueva nota: "))
            item["nota"] = nueva_nota
            print("Nota modificada correctamente.")
            return
    print("Estudiante no encontrado.")

def consulta_aprobados():
    print("=== Estudiantes Aprobados ===")
    for item in lista_notas_nombres:
        if float(item["nota"]) >= 5.0:
            print(f"Nombre: {item['nombre']}, Nota: {item['nota']}")

def media_curso():
    if not lista_notas_nombres:
        print("No hay estudiantes registrados.")
        return
    suma = 0
    for item in lista_notas_nombres:
        suma += float(item["nota"])
    media = suma / len(lista_notas_nombres)
    print(f"Media del curso: {media:.2f}")

def guardar_cambios():
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