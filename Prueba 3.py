import csv

def agregar_producto():
    # Abre el archivo 'inventario.csv' en modo append para agregar productos sin sobrescribir
    with open('inventario.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        # Solicita al usuario que ingrese los datos del producto
        id_producto = input("Ingrese el ID del producto: ")
        nombre = input("Ingrese el nombre del producto: ")
        categoria = input("Ingrese la categoría del producto (Electrónica, Textil, Calzado): ")
        precio = input("Ingrese el precio del producto: ")
        # Escribe los datos del producto en el archivo CSV
        writer.writerow([id_producto, nombre, categoria, precio])
        print("Producto agregado exitosamente.")

def leer_inventario():
    # Abre el archivo 'inventario.csv' en modo lectura
    with open('inventario.csv', mode='r') as file:
        reader = csv.reader(file)
        # Itera sobre cada fila en el archivo y la imprime
        for row in reader:
            print(row)

def clasificar_y_exportar_productos():
    # Inicializa un diccionario para clasificar los productos por categoría
    clasificacion = {'Electrónica': [], 'Textil': [], 'Calzado': []}
    # Abre el archivo 'inventario.csv' en modo lectura
    with open('inventario.csv', mode='r') as file:
        reader = csv.reader(file)
        # Itera sobre cada fila y la añade a la lista correspondiente en el diccionario
        for row in reader:
            clasificacion[row[2]].append(row)
    # Abre (o crea) el archivo 'clasificacion_productos.txt' en modo escritura
    with open('clasificacion_productos.txt', mode='w') as file:
        # Itera sobre cada categoría y sus productos, escribiéndolos en el archivo de texto
        for categoria, productos en clasificacion.items():
            file.write(f"{categoria}:\n")
            for producto in productos:
                file.write(f"{producto}\n")
            file.write("\n")
    print("Productos clasificados y exportados exitosamente.")

def menu():
    while True:
        # Imprime el menú principal
        print("\nMenú Principal")
        print("1. Agregar Producto al Inventario")
        print("2. Leer el Inventario")
        print("3. Clasificar y Exportar Productos")
        print("4. Salir")
        # Solicita al usuario que seleccione una opción del menú
        opcion = input("Seleccione una opción: ")
        # Ejecuta la función correspondiente según la opción seleccionada
        if opcion == '1':
            agregar_producto()
        elif opcion == '2':
            leer_inventario()
        elif opcion == '3':
            clasificar_y_exportar_productos()
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    # Ejecuta la función del menú principal si el script es ejecutado directamente
    menu()
