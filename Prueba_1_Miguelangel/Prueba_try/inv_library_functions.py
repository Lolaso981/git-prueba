#We import the "Datetime" library to use it in the sales part
import datetime

#We create a list with 5 items, each of them is a dictionary, in which the books are stored
Books_Inv = [
    {"Titulo": "Don Quijote De La Mancha", "Autor" : "Miguel De Cervantes", "Categoría" : "Novela", "Precio" : 299000, "Cantidad" : 7} ,
    {"Titulo": "Cien años de soledad", "Autor" : "Gabriel García Márquez", "Categoría" : "Ficción", "Precio" : 79000, "Cantidad" : 22} ,
    {"Titulo": "El principito", "Autor" : "Antoine de Saint-Exupéry", "Categoría" : "Fantasía", "Precio" : 49000, "Cantidad" : 16} ,
    {"Titulo": "La Odisea", "Autor" : "dHomero", "Categoría" : "Epico", "Precio" : 499000, "Cantidad" : 4} ,
    {"Titulo": "Harry Potter", "Autor" : "J. K. Rowling", "Categoría" : "Fantasía", "Precio" : 149000, "Cantidad" : 10} 
]

#We create an empty list to save the sales
Sales_Inv = []

#Function to validate names
def Valide_String(message):
    while True:
        Title = input(message)
        if Title.isdigit():
            print("Error, solo puedes ingresar caracteres. \n")
            continue
        return Title

#Function to validate nums
def Valide_Nums(message):
    while True:
        try:
            price = float(input(message))
            if price < 0:
                print("Error, solo puede ingresar números positivos.\n")
                continue
            return price
        except ValueError:
            print("Error, ingrese un número valido.\n")

#Function to add books to the list "Books_inv"
def Add_book():
    Title_book = Valide_String("Ingrese el título del libro: ")

    for item in Books_Inv:
        if Title_book.lower() == item["Titulo"].lower():
            print("El producto ya existe.\n")
            return
        
    Autor_book = Valide_String("Ingrese el nombre del autor: ")
    Category_book = Valide_String("Ingrese la categoría del libro: ")
    Price_book = Valide_Nums("Ingrese el precio del libro: ")
    Quantity_book = Valide_Nums("Ingrese la cantidad de libros: ")

    Book = {
        "Titulo" : Title_book,
        "Autor" : Autor_book,
        "Categoría" : Category_book,
        "Precio" : Price_book,
        "Cantidad" : Quantity_book
    }

    Books_Inv.append(Book)
    print("Libro agregado con exito!")

#Function to show books in the list "Books_inv"
def Show_book():
    x = 1
    if not Books_Inv:
        print("No hay libros en el inventario.\n")
        return

    print("---------------------------------------------------")
    print("-------------------|Libros|------------------------")
    print("---------------------------------------------------")
    for item in Books_Inv:
        print(f"{x}. Titulo: {item["Titulo"]} | Autor: {item["Autor"]} | Categoría: {item["Categoría"]} | Precio: {item["Precio"]} | Cantidad: {item["Cantidad"]}")
        x += 1

#Function to update books in the list "Books_inv" using the name of each book
def Update_book():
    Title = Valide_String("Ingrese el título del libro que deseas actualizar: ")
    found = False
    for item in Books_Inv:
        if item["Titulo"].lower() == Title.lower():
            item["Titulo"] = Valide_String("Ingrese el nuevo nombre del libro: ")
            item["Autor"] = Valide_String("Ingrese el nuevo autor del libro: ")
            item["Categoría"] = Valide_String("Ingrese la nueva categoría del libro: ")
            item["Precio"] = Valide_Nums("Ingrese el nuevo precio del libro: ", int)
            item["Cantidad"] = Valide_Nums("Ingrese la nueva cantidad de libros: ", int)
            print("El libro ha sido actualizado correctamente!")
            found = True
            break

    if not found:
        print(f"El libro {Title} no ha sido encontrado.")

#Function to delete books in the list "Books_inv" using the name of each book
def Delete_book():
    Title = Valide_String("Ingrese el nombre del libro que desea eliminar: ")
    found = False
    for item in Books_Inv:
        if item["Titulo"].lower() == Title.lower():
            Books_Inv.remove(item)
            print(f"El libro {item['Titulo']} ha sido eliminado correctamente!")
            found = True
            break

    if not found:
        print(f"El libro {Title} no ha sido encontrado.")

#Function to add sales in the list "Sales_inv"
def Add_Sale():
    print("---------------------------------------------------")
    print("------------|Registrar una venta|------------------")
    print("---------------------------------------------------")

    Title = Valide_String("Ingrese el nombre del libro que desea comprar: ")
    found = False

    for item in Books_Inv:
        if item["Titulo"].lower() == Title.lower():
            try:
                Quantity = int(input("Ingrese la cantidad que desea commprar: "))
            except ValueError:
                print("Error, debe ingresar un dato númerico.")

            if Quantity <= 0:
                print("La cantidad debe ser un número mayor a 0.\n")
            if Quantity > item["Cantidad"]:
                print("No hay suficiente en el stock")
                return
            
            User_name = input("Ingrese el nombre del cliente que esta realizando la compra: ")
            User_type = input("Ingrese el tipo de cliente (Normal / Premium): ").lower()

            Discount = 0.2 if User_type == "premium" else 0

            Total_gross = Quantity * item["Precio"]
            Total_net = Total_gross * (1 - Discount)

            item["Cantidad"] -= Quantity

            Save_sale = {
                "Titulo" : item["Titulo"],
                "Cantidad" : Quantity,
                "Bruto total" : Total_gross,
                "Net total" : Total_net,
                "Nombre usuario" : User_name,
                "Tipo usuario" : User_type,
                "Fecha" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Descuento" : Discount
            }

            Sales_Inv.append(Save_sale)

            print("\nVenta registrada con exito!")
            print(f"Titulo: {item['Titulo']} | Cantidad: {item['Cantidad']} | Bruto: {Total_gross} | Descuento: {Discount*100}% | Neto: {Total_net}\n")
            found = True
            break

    if not found:
        print("El libro no ha sido encontrado.")

#Function to show sales in the list "Sales_inv"
def Show_sales():
    if not Sales_Inv:
        print("No hay ventas registradas.\n")

    print("---------------------------------------------------")
    print("------------|Historial de ventas|------------------")
    print("---------------------------------------------------")
    for item in Sales_Inv:
        print(f"Titulo: {item['Titulo']} | Cantidad: {item['Cantidad']} | Cliente: {item['Nombre usuario']} | "
            f"Tipo: {item['Tipo usuario']} | Bruto: {item['Bruto total']} | Neto: {item['Net total']} | "
            f"Descuento: {item['Descuento']*100}% | Fecha: {item['Fecha']} ")

#Function to count how many books each author has sold       
def Sales_author(Sale_history):
    sales_count = {}
    for sale in Sale_history:
        Title = sale["Titulo"]
        Quantity = sale["Cantidad"]
        sales_count[Title] = sales_count.get(Title, 0) + Quantity
    return sales_count

#Function to show top 3 sellers in all time
def T3_sellers():
    if not Sales_Inv:
        print("No hay ventas registradas.")
        return
    
    Sales_count = Sales_author(Sales_Inv)
    Sorted_sales = sorted(Sales_count.items(), key=lambda x: x[1], reverse=True)
    top_3 = Sorted_sales[:3]

    print("---------------------------------------------------")
    print("----------|Top 3 Libros mas vendidos|--------------")
    print("---------------------------------------------------")

    for i, (Title, Quantity) in enumerate(top_3, start=1):
        print(f"{i} | {Title} - {Quantity} unidades")
    print()

#Function to show how many sales each author has
def Author_sales_report():
    if not Sales_Inv:
        print("No hay ventas registradas.\n")
        return
    
    author_sales = {}

    for sale in Sales_Inv:
        Title_name = sale["Titulo"]
        quantity = sale["Cantidad"]
        Autor = None

        for item in Books_Inv:
            if item["Titulo"].lower() == Title_name.lower():
                author = item["Autor"]
                break
        
        if author:
            author_sales[author] = author_sales.get(author, 0) + quantity

    print("---------------------------------------------------")
    print("----------|Informe de ventas por autor|------------")
    print("---------------------------------------------------")
    for Autor, Quantity in author_sales.items():
        print(f"{Autor} : {Quantity} unidades")
    print()

#Function to show the total income for each sale
def Sales_income_report():
    if not Sales_Inv:
        print("No hay ventas registradas.\n")
        return
    
    Total_gross = sum(map(lambda s: s['Bruto total'], Sales_Inv))
    Total_net = sum(map(lambda s: s['Net total'], Sales_Inv))

    print("---------------------------------------------------")
    print("--------|Informe de ingreso por ventas|------------")
    print("---------------------------------------------------")
    print(f"Total bruto: {Total_gross}")
    print(f"Total neto: {Total_net}")