# Gestión de un inventario simple

## Descripción del caso práctico

### Una pequeña tienda de barrio necesita un sistema sencillo para gestionar su inventario. El inventario se guarda en un archivo de texto llamado “inventario.txt”, donde cada línea representa un producto con su nombre y cantidad, separados por una coma. El programa debe permitir al usuario ver el inventario, añadir un nuevo producto, actualizar la cantidad de un producto existente, y eliminar un producto.

## Pasos a seguir:

1. Crear el archivo: Si no existe, crea un archivo llamado “inventario.txt” y añade algunos  productos de ejemplo, por ejemplo:
[ “manzanas,100”, “leche,50”, “pan,20” ]

2. Leer o cargar datos: al iniciar el programa, lee el contenido de “inventario.txt”. Por cada línea, divide el texto por la coma, limpia los espacios en blanco con strip() y guarda el nombre del producto y la cantidad en una lista de listas. Por ejemplo, [[“manzanas”, 100], [“leche”, 50], [“pan”, 20]]

3. Mostrar el menú: Presenta un menú en la consola con las siguientes opciones:
    + 1. Ver inventario
    + 2. Añadir producto
    + 3. Actualizar cantidad
    + 4. Eliminar producto
    + 5. Salir

4. Implementar la lógica:

    + Ver inventario: Itera sobre la lista cargada y muestra cada producto con su cantidad.

    + Añadir producto: Pide el nombre y la cantidad del nuevo producto al usuario. Valida que el producto no exista ya en la lista, si no existe, añádelo a la lista.

    + Actualizar cantidad: Pide el nombre del producto a actualizar. Busca el producto en la lista y, si se encuentra, actualiza su cantidad.

    + Eliminar producto: Pide el nombre del producto a eliminar. Busca el producto en la lista y, si se encuentra, elimínalo.

5. Guardar cambios: Antes de que el programa termine (cuando el usuario elija la opción Salir del menú), sobrescribe el archivo actual con el archivo “inventario.txt”
Cada línea del archivo se formateo sea el mismo (nombre, cantidad).
