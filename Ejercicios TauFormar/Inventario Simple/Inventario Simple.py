direccion_archivo = "Inventario Simple/inventario.txt"  # Variable con la ruta del archivo donde se guarda el inventario
listas_productos = []  # Lista global que almacena los productos y sus cantidades



def inventario_inicial():
    # Lee el archivo de inventario y carga los productos en la lista global
    with open(direccion_archivo) as file:
        for linea in file:
            producto, cantidad = linea.strip().split(",")  # Separa producto y cantidad
            listas_productos.append([producto, int(cantidad)])  # Añade a la lista como [producto, cantidad]
            
def menu():
    # Muestra el menú principal y solicita una opción al usuario
    print("=== Menu Principal ===")
    print("1. Ver inventario")
    print("2. Añadir Producto")
    print("3. Actualizar cantidad")
    print("4. Eliminar Producto")
    print("0. Salir")
    opcion = input("Introduce una opción (0-4): ")
    return opcion

def ver_inventario():
    # Muestra todos los productos y cantidades en el inventario
    for lista in listas_productos:
        print(f"Producto: {lista[0]} - Cantidad: {lista[1]}")

def añadir_producto():
    # Añade un nuevo producto al inventario si no existe
    producto = input("Introduce el producto a incluir al inventario: ")
    for item in listas_productos:
        if item[0] == producto:
            print("El producto ya se encuentra en el inventario")
            return
    cantidad = int(input("Introduce la cantidad del producto: "))
    listas_productos.append([producto, cantidad])        
    print("Producto añadido correctamente")
        
def actualizar_cantidad():
    # Actualiza la cantidad de un producto existente
    producto = input("Introduce el producto a modificar su cantidad: ")
    for item in listas_productos:
        if item[0] == producto:
            cantidad = int(input("Introduce la nueva cantidad: "))
            item[1] = cantidad
            print("Producto actualizado correctamente")
            return
    print("Producto no encontrado")       

def eliminar_producto():
    # Elimina un producto del inventario si existe
    producto = input("Introduce el producto a eliminar: ")
    for i, item in enumerate(listas_productos):
        if item[0] == producto:
            del(listas_productos[i])
            print("Producto eliminado correctamente")
            return
    print("Producto no encontrado")

def guardar_cambios():
    # Guarda el inventario actualizado en el archivo
    with open(direccion_archivo, "w") as file:
        for lista in listas_productos:
            file.write(f"{lista[0]},{str(lista[1])}\n") 
                

def main():
    # Bucle principal del programa que gestiona el menú y las opciones
    finW = True
    while finW:
        opcion = menu()
        match opcion:
            case "1":
                ver_inventario()
            case "2":
                añadir_producto()
            case "3":
                actualizar_cantidad()
            case "4":
                eliminar_producto()
            case "0":
                print("Saliendo del programa...")
                guardar_cambios()
                finW = False
            case _:
                print("Opción no válida")
                 
if __name__ == "__main__":
    # Punto de entrada del programa
    inventario_inicial()
    main()
    
    
    
        