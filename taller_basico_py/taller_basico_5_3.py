print("-------------------------------")
print("Bienvenido al cajero automático")
print("-------------------------------")

name = input("Por favor, ingresa tu nombre: ")
while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")

balance = [0.0]

while True:
    try:
        print("-------------------------------")
        print(f"Hola {name}, a continuacion podras ver las opciones a realizar")
        print("1. Depositar dinero")
        print("2. Retirar dinero")
        print("3. Ver saldo")
        print("4. Salir")

        opcion = int(input("Selecciona una opcion (1-4): "))

        if opcion == 1:
            while True:
                try:
                    deposit_amount = float(input("Ingresa la cantidad a depositar: "))
                    if deposit_amount <= 0:
                        print("La cantidad a depositar debe ser un numero positivo. Intenta de nuevo.")
                        continue

                    balance[0] += deposit_amount
                    print("-------------------------------")
                    print(f"Has depositado: {deposit_amount:.2f}. Nuevo saldo: {balance[0]:.2f}")
                    break

                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número válido para el depósito.")

        elif opcion == 2:
            while True:
                try:
                    withdraw_amount = float(input("Ingresa la cantidad a retirar: "))
                    if withdraw_amount <= 0:
                        print("La cantidad a retirar debe ser un numero positivo. Intenta de nuevo.")
                        continue

                    if withdraw_amount > balance[0]:
                        print("-------------------------------")
                        print("Fondos insuficientes. Intenta de nuevo.")
                        break

                    balance[0] -= withdraw_amount
                    print("-------------------------------")
                    print(f"Has retirado: {withdraw_amount:.2f}. Nuevo saldo: {balance[0]:.2f}")
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número válido para el retiro.")
        
        elif opcion == 3:
            print("-------------------------------")
            print(f"Tu saldo actual es: {balance[0]:.2f}")
            continue

        elif opcion == 4:
            print("-------------------------------")
            print("Gracias por usar el cajero automático. ¡Hasta luego!")
            print("-------------------------------")
            break

        else:
            print("Opción inválida. Por favor, selecciona una opción entre 1 y 4.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

        