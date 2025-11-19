from datetime import date

print("¡Hola! Vamos a calcular tu edad.")

nacimiento = int(input("¿En qué año naciste? "))

año_actual = date.today().year
edad = año_actual - nacimiento

print(f"Si naciste en {nacimiento}, entonces tienes {edad} años en {año_actual}.")