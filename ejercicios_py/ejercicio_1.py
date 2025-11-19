# print("Hola mundo")

# name = input("¿Cual es tu nombre? ")
# age = int(input("¿Cuantos años tienes? "))

# if age < 18:
#     print(f"Hola {name}, eres menor de edad, tienes {age} años.")
# else:
#     print(f"Hola {name}, eres mayor de edad, tienes {age} años.")
# print("Fin del programa.")

print("Ahora vamos a realizar una sumatoria de números de 1 hasta n (n ingresado por el usuario)")

n = int(input("Ingresa un número entero positivo n => "))
suma_total = 0

i = 1
while i <= n:
    suma_total += i
    print(f" {i} + {suma_total-i} = {suma_total}")
    i += 1

print(f"La suma total de los números de 1 hasta {n} es {suma_total}")

print("--------------------------------------------------------------")

print("Ahora vamos a hacer una tabla de multiplicar de un número n las veces que necesites(n ingresado por el usuario)")

n = int(input("Ingresa el numero entero positivo que deseas mutiplicar => "))
veces = int(input("Ingresa cuantas veces deseas multiplicar el número => "))

i = 1
while i <= veces:
    resultado = n * i
    print(f"{n} x {i} = {resultado}")
    i += 1

print("--------------------------------------------------------------")

print("Ahora vamos a hacer un contador regresivo desde un número n hasta 0 (n ingresado por el usuario)")

n = int(input("Ingresa un número entero positivo n => "))
while n >= 0:
    print(n)
    n -= 1

print("--------------------------------------------------------------")

print("Ahora vamos a adivinar un número entre 1 y 10")
import random
numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adivina el número entre 1 y 10 => "))
    intentos += 1
    if intento < numero_secreto:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > numero_secreto:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
        break

print("-------------------------------------------------------------")

print("Ahora vamos a sumar números hasta que el usuario decida parar (ingresando 0)")

suma_total = 0
while True:
    numero = int(input("Ingresa un número para sumar (0 para parar) => "))
    if numero == 0:
        break
    suma_total += numero
    print(f"Suma parcial: {suma_total}")