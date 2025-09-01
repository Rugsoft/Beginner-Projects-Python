# Registro de notas de estudiantes

## Descripción del caso práctico

### Un profesor quiere un programa para gestionar las notas de sus estudiantes. La información de los estudiantes se guarda en un archivo de texto llamado “notas.txt”. Cada línea del archivo contiene el nombre del estudiante y su nota, separados por punto y coma. El programa debe permitir al profesor añadir nuevos estudiantes, modificar la nota de uno existente y ver un listado de todos los estudiantes.

## Pasos a seguir

1. Crear el archivo: Crea un archivo “notas.txt” con algunos datos de ejemplo, por ejemplo: 
Juan Pérez;8.5 María López;7.0 Pedro Gomez;7.1

2. Leer el archivo y convertir los datos: Lee el archivo línea por línea, por cada línea, separa el nombre y la nota usando el delimitador punto y coma (“;”), y guarda los datos en una lista de diccionarios: [{“nombre”: “Juan Pérez”, “nota”: 8.5}, …].

3. Mostrar un menú con las siguientes operaciones:

    + 1. Ver estudiantes
    + 2. Añadir estudiante
    + 3. Modificar nota
    + 4. Consulta de aprobados
    + 5. Media del curso
    + 0. Salir

4. Implementar la lógica:

    + Ver listado: Muestra el nombre y la nota de cada estudiante de la lista.
    + Añadir estudiante: Pide el nombre y la nota del nuevo estudiante. Asegúrate de validar si el estudiante ya existe antes de añadirlo.
    + Modificar nota: Pide un nombre y actualiza la nueva nota. Busca el estudiante y actualiza su nota. (Convierte la nota a un tipo numérico (float) al     actualizarla.)
    + Consulta de aprobados: saber el número de alumnos que han sacado 5.0 o más en su calificación.
    + Media del curso: Mostrar la media del curso = la media aritmética

5. Guardar los cambios: Al finalizar, guarda la lista de diccionarios actualizada de nuevo en el archivo “notas.txt”, manteniendo el formato de punto y coma.
