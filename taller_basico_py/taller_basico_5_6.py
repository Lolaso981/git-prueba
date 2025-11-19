print("----------------------------------------")
print("Bienvenido a la agenda de contactos")
print("(lista de diccionarios)")
print("----------------------------------------")

name = input("Por favor, ingresa tu nombre: ")
while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")

contacts = []

def agregar_contacto(nombre, telefono):
    contacto = {"nombre": nombre, "telefono": telefono}
    contacts.append(contacto)

def mostrar_contactos():
    if not contacts:
        print("No hay contactos en la agenda.")
    else:
        print("Contactos en la agenda:")
        for contacto in contacts:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")

def eliminar_contacto(nombre):
    for contacto in contacts:
        if contacto['nombre'].lower() == nombre.lower():
            contacts.remove(contacto)
            print(f"Contacto {nombre} eliminado.")
            return
    print(f"Contacto {nombre} no encontrado.")

def buscar_contacto(nombre):
    for contacto in contacts:
        if contacto['nombre'].lower() == nombre.lower():
            print(f"Contacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
            return
    print(f"Contacto {nombre} no encontrado.")

def salir():
    print(f"Gracias por usar la agenda de contactos, {name}. ¡Hasta luego!")
    exit()

while True:
    try:
        print("----------------------------------------")
        print(f"Hola {name}, a continuacion podras ver las opciones a realizar")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Eliminar contacto")
        print("4. Buscar contacto")
        print("5. Salir")

        opcion = int(input("Selecciona una opcion (1-5): "))
        if opcion == 1:
            nombre = input("Ingresa el nombre del contacto: ")
            telefono = input("Ingresa el teléfono del contacto: ")
            agregar_contacto(nombre, telefono)
            print(f"Contacto {nombre} agregado.")

        elif opcion == 2:
            mostrar_contactos()

        elif opcion == 3:
            nombre = input("Ingresa el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)

        elif opcion == 4:
            nombre = input("Ingresa el nombre del contacto a buscar: ")
            buscar_contacto(nombre)

        elif opcion == 5:
            salir()
        else:
            print("Opcion invalida. Por favor, selecciona una opcion del 1 al 5.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")