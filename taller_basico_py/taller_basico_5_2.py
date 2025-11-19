print("-------------------------------")
print("Bienvenido al carrito de compras")
print("-------------------------------")
name = input("Por favor, ingresa tu nombre: ")
while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")

product_price = 0.0
cart = []

while True:
    try:
        print("-------------------------------")
        print(f"Hola {name}, a continuacion podras ver las opciones a realizar")
        print("1. Agregar un producto")
        print("2. Ver el total de la compra")
        print("3. Salir")

        option = int(input("Selecciona una opcion (1-3): "))

        if option == 1:
            product_name = input("Ingresa el nombre del producto: ")
            product_price = 0.0

            while True:
                try:
                    product_price = float(input(f"Ingresa el precio de {product_name}: "))
                    if product_price < 0:
                        print("El precio no puede ser negativo. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número válido para el precio.")
                
                cantity = 0
            while True:
                try:
                    cantity = int(input(f"Ingresa la cantidad de {product_name}: "))
                    if cantity <= 0:
                        print("La cantidad debe ser un numero positivo. Intenta de nuevo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número entero válido para la cantidad.")
                    
            item_total = product_price * cantity

            new_product = {
                "name": product_name,
                "price": product_price,
                "quantity": cantity,
                "item_total": item_total    
            }
            cart.append(new_product)

            print(f"Producto {product_name} agregado al carrito: {cantity} unidad(es) a {product_price:.2f} cada una. Total: {item_total:.2f}")
            continue

        elif option == 2:
            if not cart:
                print("-------------------------------")
                print("El carrito está vacío.")
            else:
                final_total = 0.0
                print("\n--- Productos en el carrito ---")

                for item in cart:
                    print(f"{item['quantity']} x {item['name']} a {item['price']:.2f} cada una - Total: {item['item_total']:.2f}")
                    final_total += item['item_total']

                print("-------------------------------")
                print(f"\nTotal de la compra: {final_total:.2f}\n")
        elif option == 3:
            print("Gracias por usar el carrito de compras. ¡Hasta luego!")
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero entre 1 y 3.")