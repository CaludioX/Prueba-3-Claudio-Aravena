import csv

def agregar_producto():
    with open('inventario.csv', 'a', newline='') as csvfile:
        fieldnames = ['ID', 'Nombre', 'Categoría', 'Precio']
        # Usamos delimiter para especificar un espacio en blanco como separador
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=' ')
        
        # Pedir datos al usuario
        id_producto = input("Ingrese ID del producto: ")
        nombre = input("Ingrese nombre del producto: ")
        categoria = input("Ingrese categoría del producto (Electrónica, Textil, Calzado): ")
        precio = input("Ingrese precio del producto: ")
        
        # Escribir datos en el archivo CSV
        writer.writerow({'ID': id_producto, 'Nombre': nombre, 'Categoría': categoria, 'Precio': precio})
        print("Producto agregado exitosamente.")

def leer_inventario():
    try:
        with open('inventario.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=' ')
            print("Inventario actual:")
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No se encontró el archivo inventario.csv. Asegúrese de haber agregado productos primero.")

def clasificar_y_exportar_productos():
    categorias = {'Electrónica': [], 'Textil': [], 'Calzado': []}
    
    try:
        with open('inventario.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=' ')
            for row in reader:
                categoria = row.get('Categoría', None)  # Usamos .get() para manejar claves faltantes
                if categoria in categorias:
                    categorias[categoria].append(row)
        
        with open('clasificacion_productos.txt', 'w') as txtfile:
            for categoria, productos in categorias.items():
                txtfile.write(f"Categoría: {categoria}\n")
                for producto in productos:
                    txtfile.write(f"  ID: {producto['ID']}, Nombre: {producto['Nombre']}, Precio: {producto['Precio']}\n")
        
        print("Productos clasificados y exportados exitosamente.")
    except FileNotFoundError:
        print("No se encontró el archivo inventario.csv. Asegúrese de haber agregado productos primero.")

def menu():
    while True:
        print("\n--- Menú de Gestión de Inventario ---")
        print("1. Agregar Productos al Inventario")
        print("2. Leer el Inventario")
        print("3. Clasificar y Exportar Productos")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
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
            print("Opción no válida. Por favor, seleccione una opción del 1 al 4.")

# Llamada a la función principal del menú
if __name__ == "__main__":
    menu()