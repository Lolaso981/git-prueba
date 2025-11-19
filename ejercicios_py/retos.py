# 1. Par o impar
# Pide al usuario un número e indica si es par o impar sin usar ningún módulo especial.

print("Bienvenido, este algoritmo te ayudara a saber si el número que ingreses es Par o Impar")
num = int(input("Por favor, digita un número => "))

if num % 2 == 0:
    print(f"El número {num} es Par")
else:
    print(f"El número {num} es Impar")

# 2. Calculadora simple
# Pide dos números y una operación (+, -, *, /) y realiza la operación.

print("Bienvenido a la Calculadora")
num_1 = int(input("Ingresa el primer digito => "))
num_2 = int(input("Ingresa el segundo digito => "))

print("Ahora, escoge que operación deseas realizar, digita el número de la operación")

print("1. +")
print("2. -")
print("3. *")
print("4. /")

caso = int(input())

if caso == 1:
    print(f"La suma de {num_1} y {num_2} es igual a {num_1 + num_2}")
elif caso == 2:
    print(f"La resta de {num_1} y {num_2} es igual a {num_1 - num_2}")
elif caso == 3:
    print(f"La multiplicación de {num_1} y {num_2} es igual a {num_1 * num_2}")
elif caso == 4:
    print(f"La división de {num_1} y {num_2} es igual a {num_1 / num_2}")
else:
    print("Ingresaste un dato erroneo")