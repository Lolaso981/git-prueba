print("-----------------------------------------")
print("Bienvenido al sistema de gestion de inventario")
print("-----------------------------------------")

name = input("Por favor, ingresa tu nombre: ")
while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")

def agregar_producto():
    print("-----------------------------------------")
    producto = input("Ingresa el nombre del producto a agregar: ")
    while True:
        if producto.replace(" ", "").isalpha():
            break
        else:
            print ("El nombre del producto no debe contener numeros. Intenta de nuevo.")
            producto = input("Ingresa el nombre del producto a aggar: ")

    print("-----------------------------------------")
    precio = input("Ingresa el precio del producto: ")
    while True:
        try:
            precio = float(precio)
            if precio <= 0:
                print("El precio debe ser un numero positivo. Intenta de nuevo.")
                precio = input("Ingresa el precio del producto: ")
                continue
            break
        except ValueError:
            print("Entrada invalida. Por favor, ingresa un numero valido para el precio.")
            precio = input("Ingresa el precio del procto: ")

    print("-----------------------------------------")
    cantidad = input("Ingresa la cantidad del producto: ")
    while True:
        try:
            cantidad = int(cantidad)
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intenta de nuevo.")
                cantidad = input("Ingresa la cantidad del producto: ")
                continue
            break
        except ValueError:
            print("Entrada invalida. Por favor, ingresa un numero valido para la cantidad.")
            cantidad = input("Ingresa la cantidad del procto: ")

    inventario.append({
    "producto": producto, 
    "precio": float(precio), 
    "cantidad": int(cantidad)
    })

    print("-----------------------------------------")
    print(f"Producto {producto} agregado al inventario.")

def mostrar_inventario():
    print("-----------------------------------------")
    if not inventario:
        print("El inventario esta vacio.")
    else:
        print("Inventario actual:")
        inventario.sort()
        for item in inventario:
            print(f"Producto: {item['producto']} | Precio: {item['precio']} | Cantidad: {item['cantidad']} | Valor Total: {item['precio'] * item['cantidad']}")


def calcular_estadisticas():
    print("-----------------------------------------")
    if not inventario:
        print("El inventario esta vacio. No se pueden calcular estadisticas.")
    else:
        valor_total_valor = sum(item['precio'] * item['cantidad'] for item in inventario)
        valor_total_productos = sum(item['cantidad'] for item in inventario)

    print(f"Valor total del inventario: {valor_total_valor}")
    print(f"Cantidad total de productos: {valor_total_productos}")

def salir_sistema():
    print(f"Gracias por usar el sistema de gestion de inventario, {name}. ¡Hasta luego!")
    exit()

inventario = []

while True:
    try:
        print("-----------------------------------------")
        print(f"Hola {name}, a continuacion podras ver las opciones a realizar")
        print("1. Agregar producto")
        print("2. Mostrar inventario")
        print("3. calcular estadisticas")
        print("4. Salir")

        opcion = int(input("Selecciona una opcion (1-4): "))

        if opcion == 1:
            agregar_producto()

        elif opcion == 2:
            mostrar_inventario()

        elif opcion == 3:
            calcular_estadisticas()

        elif opcion == 4:
            salir_sistema()

        else:
            print("Opcion invalida. Por favor, selecciona una opcion entre 1 y 4.")
    except ValueError:
        print("Entrada invalida. Por favor, ingresa un numero valido para la opcion.")