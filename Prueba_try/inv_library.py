from inv_library_functions import Add_book, Show_book, Update_book, Delete_book, Add_Sale, Show_sales, T3_sellers, Author_sales_report, Sales_income_report
name = input("Por favor, digite su nombre: ")

while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")

print("-----------------------------------------------------")
print(f"{name} bievenido al sistema de gestion de libros.")
print("------------------------------------------------------")
print("A continuación podras ver las opciones que podras realizar.")

#Cycle that allows us to remain in the code without exiting due to any error, except if we want to exit.
while True:
    try:
        print("\n1. Gestión de Inventario.")
        print("2. Gestión de Ventas.")
        print("3. Salir")
        opt_inv_main = int(input("\nDigite la opción que deseas realizar: "))
        if opt_inv_main < 1 or opt_inv_main > 3:
            print("Error, solo se permite números del 1 al 3")

        if opt_inv_main == 1:
            while True:
                print("\nGestión de inventario.")
                print("1. Agregar libro.")
                print("2. Mostrar libros.")
                print("3. Actualizar libro.")
                print("4. Eliminar libro.")
                print("5. Salir")
                opt_gestor_inv = int(input("Digita la opción que deseas realizar: \n"))
                if opt_gestor_inv < 1 or opt_gestor_inv > 5:
                    print("Error, solo se permite números del 1 al 5.")
                if opt_gestor_inv == 1:
                    Add_book()
                if opt_gestor_inv == 2:
                    Show_book()
                if opt_gestor_inv == 3:
                    Update_book()
                if opt_gestor_inv == 4:
                    Delete_book()
                if opt_gestor_inv == 5:
                    break

        if opt_inv_main == 2:
            while True:
                print("\nGestión de Ventas.")
                print("1. Registrar una venta.")
                print("2. Ver historial de ventas.")
                print("3. Ver Top 3 productos mas vendidos.")
                print("4. Reportes de ventas por autor.")
                print("5. Reporte de ingresos brutos y netos.")
                print("6. Salir")
                opt_gestor_sale = int(input("Digita la opción que deseas realizar: \n"))
                if opt_gestor_sale < 1 or opt_gestor_sale > 6:
                    print("Error, solo se permiten númmeros del 1 al 6")
                if opt_gestor_sale == 1:
                    Add_Sale()
                if opt_gestor_sale == 2:
                    Show_sales()
                if opt_gestor_sale == 3:
                    T3_sellers()
                if opt_gestor_sale == 4:
                    Author_sales_report()
                if opt_gestor_sale == 5:
                    Sales_income_report()
                if opt_gestor_sale == 6:
                    break
        
        if opt_inv_main == 3:
            print("Gracias por usar el sistema de inventario, espero verte pronto!")
            break

    except ValueError:
        print("Ingresaste un dato erroneo. Intenta de nuevo.")