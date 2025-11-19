print("--------------------------------------")
print("Bienvenido a la calculadora avanzada")
print("(Con soporte para operaciones básicas)")
print("--------------------------------------")

name = input("Por favor, ingresa tu nombre: ")
while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")

def calcular(operacion, num1, num2):
    if operacion == 1:
        return num1 + num2
    elif operacion == 2:
        return num1 - num2
    elif operacion == 3:
        return num1 * num2
    elif operacion == 4:
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: División por cero no permitida."

while True:
    try:
        print("--------------------------------------")
        print(f"Hola {name}, a continuacion podras ver las opciones a realizar")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = int(input("Selecciona una opcion (1-5): "))
        if opcion in [1, 2, 3, 4]:
            num1 = float(input("Ingresa el primer numero: "))
            num2 = float(input("Ingresa el segundo numero: "))

            resultado = calcular(opcion, num1, num2)
            print("--------------------------------------")
            print(f"El resultado es: {resultado}")

        elif opcion == 5:
            print("--------------------------------------")
            print(f"Gracias por usar la calculadora, {name}. ¡Hasta luego!")
            break
        else:
            print("Opcion invalida. Por favor, selecciona una opcion del 1 al 5.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido.")