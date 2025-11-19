datos = ["Ana", "Luis", "María", "Carlos"]

with open("Nombres.txt", "w") as archivo:
    for nombre in datos:
        archivo.write(nombre + "\n")

with open("Nombres.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)