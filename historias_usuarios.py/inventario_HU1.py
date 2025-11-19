while True: # Bucle principal del sistema de inventario
    print("=== Sistema de Inventario ===") # Encabezado del sistema

    print("Seleccione una opción:") # Menú de opciones
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Salir")

    opcion = input("Ingrese el número de la opción deseada: ") # Solicita al usuario que ingrese una opción
    if opcion == "1": # Opción para agregar un producto
        while True: # Bucle para validar el ingreso de datos del producto
            nombre = input("Ingrese el nombre del producto: ") # Solicita el nombre del producto
            if nombre.isalpha(): # Verifica que el nombre contenga solo letras
                while True: # Bucle para validar la cantidad y el precio
                    cantidad = input("Ingrese la cantidad del producto: ") # Solicita la cantidad del producto
                    if cantidad.isdigit(): # Verifica que la cantidad sea un número positivo
                        while True: # Bucle para validar el precio 
                            precio = input("Ingrese el precio del producto: ") # Solicita el precio del producto
                            if precio.isdigit(): # Verifica que el precio sea un número positivo
                                costo_total = int(cantidad) * float(precio) # Calcula el costo total
                                print(f"Producto agregado: {nombre} | Cantidad: {cantidad} | Precio unitario: {precio} | Costo total: {costo_total}") # Muestra la información del producto agregado
                                break                                
                            else:
                                print("El precio debe ser un número positivo y no puede ser un caracter. Intente de nuevo.") 
                    else:
                        print("La cantidad debe ser un número positivo y no puede ser un caracter. Intente de nuevo.")
            else:
                print("El nombre del producto debe contener solo letras. Intente de nuevo.")

    elif opcion == "2": # Opción para ver el inventario
        print("Inventario de productos:")
        # Aquí se mostrarían los productos almacenados en el inventario
        print("Funcionalidad en desarrollo...")
        break

    elif opcion == "3": # Opción para salir del sistema
        print("Saliendo del sistema de inventario. ¡Hasta luego!")
        break

    else: # Manejo de opción inválida
        print("Opción no válida. Por favor, intente de nuevo.")