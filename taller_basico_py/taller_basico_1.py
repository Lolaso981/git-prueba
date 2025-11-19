# Taller Básico de Python Parte 1
# Fundamentos de programación en Python y Variables

print ("Hola usuario")
name = input("Por favor, ingresa tu nombre: ")
while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")
        
age = input("Cuantos años tienes? => ")
while True:
    if age.isdigit() and int(age) > 0 and int(age) < 100:
        break
    else:
        print("La edad debe ser un número positivo. Intenta de nuevo.")
        age = input("Cuantos años tienes? => ")
print (f"Mucho gusto {name}, veo que tienes {age} años")
print ("-------------------------------------------------------------")

while True:
    try:
        print("A continuacion podras escoger a que nivel ingresar")
        print("1. Nivel 1 — Fundamentos y Variables")
        print("2. Nivel 2 — Condicionales (Decisiones)")
        print("3. Nivel 3 — Bucles y Repetición")
        print("4. Nivel 4 — Listas y Colecciones")
        print("5. Salir")

        opcion = int(input("Digita el la opción en la cual decidas ingresar(1 - 5): "))
        print ("-------------------------------------------------------------")

        if opcion == 1:
            while True:
                try:
                    print("Ahora que opciones hacer dentro del nivel 1")
                    print("1. Suma de dos números")
                    print("2. Área de un triángulo")
                    print("3. Conversión de Celsius a Fahrenheit")
                    print("4. Edad dentro de 10 años")
                    print("5. Salir del nivel 1")
                    opcion_nivel1 = int(input("Selecciona una opción (1-5): "))
                    print ("-------------------------------------------------------------")

                    if opcion_nivel1 == 1:
                        print("Ahora vamos a hacer una suma de dos números")
                        num1 = int(input("Ingresa el primer número => "))
                        num2 = int(input("Ingresa el segundo número => "))
                        suma = num1 + num2
                        print(f"La suma de {num1} y {num2} es igual a {suma}")
                        print ("-------------------------------------------------------------")

                    elif opcion_nivel1 == 2:
                        print("Ahora vamos a conocer el Área de un triángulo")
                        base = float(input("Ingresa la base del triángulo => "))
                        altura = float(input("Ingresa la altura del triángulo => "))
                        area = (base * altura) / 2
                        print(f"El área del triángulo con base {base} y altura {altura} es igual a {area}")
                        print ("-------------------------------------------------------------")

                    elif opcion_nivel1 == 3:
                        print ("Ahora vamos a pasar de grados Celsius a Fahrenheit")
                        celsius = float(input("Ingresa la temperatura en grados Celsius => "))
                        fahrenheit = (celsius * 9/5) + 32
                        print(f"{celsius}° Celsius son iguales a {fahrenheit}° Fahrenheit")
                        print ("-------------------------------------------------------------")

                    elif opcion_nivel1 == 4:
                        print("Ahora vamos a conocer tu edad dentro de 10 años más")
                        edad_futura = int(age) + 10
                        print(f"{name}, dentro de 10 años tendrás {edad_futura} años")
                        print ("-------------------------------------------------------------")
                    
                    elif opcion_nivel1 == 5:
                        print("Saliendo del nivel 1. ¡Hasta luego!")
                        break
                except ValueError:
                    print("Ingresaste un dato erroneo, intenta de nuevo")

# Inicio del Taller Básico de Python Parte 2
# Condicionales

        if opcion == 2:
            while True:
                try:
                    print("Ahora que opciones hacer dentro del nivel 2")
                    print("1. Mayor o menor de edad")
                    print("2. Número positivo, negativo o cero")
                    print("3. Número par o impar")
                    print("4. Calculadora básica")
                    print("5. Clasificador de notas")
                    print("6. comparar tres números")
                    print("7. Salir del nivel 2")
                    opcion_nivel2 = int(input("Selecciona una opción (1-7): "))
                    print ("-------------------------------------------------------------")

                    if opcion_nivel2 == 1:
                        print("Ahora vamos a saber si eres mayor de edad")
                        if int(age) >= 18:
                            print(f"{name}, eres mayor de edad. Tienes {age} años.")
                        else:
                            print(f"{name}, eres menor de edad. Tienes {age} años.")
                        print ("-------------------------------------------------------------")

                    elif opcion_nivel2 == 2:
                        print("Ahora vamos a saber si un número es positivo, negativo o cero")
                        numero = float(input("Ingresa un número => "))
                        if numero > 0:
                            print(f"El número {numero} es positivo.")
                        elif numero < 0:
                            print(f"El número {numero} es negativo.")
                        else:
                            print("El número es cero.")
                        print ("-------------------------------------------------------------")
                    
                    elif opcion_nivel2 == 3:
                        print("Ahora vamos a saber si un número es par o impar")
                        numero_par_impar = int(input("Ingresa un número entero => "))
                        if numero_par_impar % 2 == 0:
                            print(f"El número {numero_par_impar} es par.")
                        else:
                            print(f"El número {numero_par_impar} es impar.")
                        print ("-------------------------------------------------------------")

                    elif opcion_nivel2 == 4:
                        print("Ahora vamos a hacer una calculadora básica")
                        print("Seleccione una operación:")
                        print("1. Suma")
                        print("2. Resta")
                        print("3. Multiplicación")
                        print("4. División")
                        print("5. Salir")
                        opcion = int(input("Ingrese el número de la operación deseada: "))

                        if opcion == 1:
                            num1 = float(input("Ingrese el primer número: "))
                            num2 = float(input("Ingrese el segundo número: "))
                            resultado = num1 + num2
                            operacion = "suma"
                            print(f"El resultado de la {operacion} entre {num1} y {num2} es {resultado}")

                        elif opcion == 2:
                            num1 = float(input("Ingrese el primer número: "))
                            num2 = float(input("Ingrese el segundo número: "))
                            resultado = num1 - num2
                            operacion = "resta"
                            print(f"El resultado de la {operacion} entre {num1} y {num2} es {resultado}")

                        elif opcion == 3:
                            num1 = float(input("Ingrese el primer número: "))
                            num2 = float(input("Ingrese el segundo número: "))
                            resultado = num1 * num2
                            operacion = "multiplicación"
                            print(f"El resultado de la {operacion} entre {num1} y {num2} es {resultado}")

                        elif opcion == 4:
                            num1 = float(input("Ingrese el primer número: "))
                            num2 = float(input("Ingrese el segundo número: "))
                            operacion = "división"
                            if num2 != 0:
                                resultado = num1 / num2
                                print(f"El resultado de la {operacion} entre {num1} y {num2} es {resultado}")
                            else:
                                print("Error: No se puede dividir por cero.")

                        elif opcion == 5:
                            print("Saliendo de la calculadora. ¡Hasta luego!")

                        else:
                            print("Opción no válida. Por favor, intente de nuevo.")
                        print("-------------------------------------------------------------")

                    elif opcion_nivel2 == 5:
                        print("Ahora vamos a realizar un clasificador de notas")
                        nota = float(input("Ingresa tu nota (0 - 100) => "))
                        if 90 <= nota <= 100:
                            print("Tu calificación es Excelente")
                        elif 70 <= nota < 90:
                            print("Tu calificación es Aprobado")
                        elif 0 <= nota < 70:
                            print("Tu calificación es Reprobado")
                        else:
                            print("Nota inválida. Por favor ingresa una nota entre 0 y 100.")
                        print("-------------------------------------------------------------")

                    elif opcion_nivel2 == 6:
                        print("Ahora vamos a conocer el mayor de 3 números")
                        num_a = float(input("Ingresa el primer número => "))
                        num_b = float(input("Ingresa el segundo número => "))
                        num_c = float(input("Ingresa el tercer número => "))

                        if num_a >= num_b and num_a >= num_c:
                            mayor = num_a
                        elif num_b >= num_a and num_b >= num_c:
                            mayor = num_b
                        else:
                            mayor = num_c

                        print(f"El mayor de los tres números es {mayor}")
                        print ("-------------------------------------------------------------")

                    elif opcion_nivel2 == 7:
                        print("Saliendo del nivel 2. ¡Hasta luego!")
                        break
                except ValueError:
                    print("Ingresaste un dato erroneo, intenta de nuevo")

# Inicio del Taller Básico de Python Parte 3
# Bucles

        if opcion == 3:
            while True:
                try:
                    print("Ahora que opciones hacer dentro del nivel 3")
                    print("1. Contar del 1 al 10")
                    print("2. Sumatoria de números hasta n")
                    print("3. Tabla de multiplicar")
                    print("4. Contador regresivo")
                    print("5. Adivinar un número")
                    print("6. Sumar números hasta parar")
                    print("7. Salir del nivel 3")
                    opcion_nivel3 = int(input("Selecciona una opción (1-7): "))
                    print ("-------------------------------------------------------------")

                    if opcion_nivel3 == 1:
                        print("Ahora vamos a contar del 1 al 10 usando un bucle while")
                        contador = 1
                        while contador <= 10:
                            print(contador)
                            contador += 1
                        print("-------------------------------------------------------------")

                    if opcion_nivel3 == 2:
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

                    if opcion_nivel3 == 3:
                        print("Ahora vamos a hacer una tabla de multiplicar de un número n las veces que necesites(n ingresado por el usuario)")
                        n = int(input("Ingresa el numero entero positivo que deseas mutiplicar => "))
                        veces = int(input("Ingresa cuantas veces deseas multiplicar el número => "))

                        i = 1
                        while i <= veces:
                            resultado = n * i
                            print(f"{n} x {i} = {resultado}")
                            i += 1
                        print("--------------------------------------------------------------")

                    if opcion_nivel3 == 4:
                        print("Ahora vamos a hacer un contador regresivo desde un número n hasta 0 (n ingresado por el usuario)")
                        n = int(input("Ingresa un número entero positivo n => "))
                        while n >= 0:
                            print(n)
                            n -= 1
                        print("--------------------------------------------------------------")

                    if opcion_nivel3 == 5:
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

                    if opcion_nivel3 == 6:
                        print("Ahora vamos a sumar números hasta que el usuario decida parar (ingresando 0)")
                        suma_total = 0
                        while True:
                            numero = int(input("Ingresa un número para sumar (0 para parar) => "))
                            if numero == 0:
                                break
                            suma_total += numero
                            print(f"Suma parcial: {suma_total}")
                            print ("--------------------------------------------------------------")

                    if opcion_nivel3 == 7:
                        print("Saliendo del nivel 3. ¡Hasta luego!")
                        break
                except ValueError:
                    print("Ingresaste un dato erroneo, intenta de nuevo")

# Inicio del Taller Básico de Python Parte 4
# Listas y Diccionarios

        if opcion == 4:
            while True:
                try:
                    print("Ahora que opciones hacer dentro del nivel 4")
                    print("1. Lista de frutas")
                    print("2. Eliminar fruta de la lista")
                    print("3. Buscar fruta en la lista")
                    print("4. Promedio de una lista de números")
                    print("5. Números pares de una lista")
                    print("6. Eliminar duplicados de una lista")
                    print("7. Salir del nivel 4")
                    opcion_nivel4 = int(input("Selecciona una opción (1-7): "))
                    print ("-------------------------------------------------------------")

                    if opcion_nivel4 == 1:
                        print("Ahora vamos a crear una lista de frutas y agregar frutas hasta que el usuario decida parar (ingresando 'salir')")
                        frutas = []
                        while True:
                            fruta = input("Ingresa el nombre de una fruta (o 'salir' para terminar) => ")
                            if fruta.lower() == 'salir':
                                break
                            frutas.append(fruta)

                        print("Las frutas en tu lista son:")
                        for fruta in frutas:
                            print(f"- {fruta}")
                        print("--------------------------------------------------------------")
                    
                    if opcion_nivel4 == 2:
                        print("Ahora vamos a eliminar una fruta de la lista si existe")
                        fruta_a_eliminar = input("Ingresa el nombre de la fruta que deseas eliminar => ")
                        if fruta_a_eliminar in frutas:
                            frutas.remove(fruta_a_eliminar)
                            print(f"{fruta_a_eliminar} ha sido eliminada de la lista.")

                        print("Las frutas en tu lista actualizada son:")
                        for fruta in frutas:
                            print(f"- {fruta}")
                        print("--------------------------------------------------------------")

                    if opcion_nivel4 == 3:
                        print("Ahora vamos a buscar alguna fruta en la lista")
                        fruta_a_buscar = input("Ingresa el nombre de la fruta que deseas buscar => ")
                        if fruta_a_buscar in frutas:
                            print(f"{fruta_a_buscar} si está en la lista.")
                        else:
                            print(f"{fruta_a_buscar} no está en la lista.")
                        print("--------------------------------------------------------------")

                    if opcion_nivel4 == 4:
                        print("Ahora vamos a hacer una lista de números y vamos a calcular su promedio")
                        numeros = []
                        while True:
                            entrada = input("Ingresa un número para agregar a la lista (o 'salir' para terminar) => ")
                            if entrada.lower() == 'salir':
                                break
                            numero = float(entrada)
                            numeros.append(numero)

                        if len(numeros) > 0:
                            promedio = sum(numeros) / len(numeros)
                            print(f"El promedio de los números en la lista es {promedio}")
                        else:
                            print("No se ingresaron números para calcular el promedio.")
                        print("--------------------------------------------------------------")

                    if opcion_nivel4 == 5:
                        print("Ahora vamos a ingresar números en una lista y dejar solo los números pares")

                        numeros = []
                        while True:
                            entrada = input("Ingresa un número para agregar a la lista (o 'salir' para terminar) => ")
                            if entrada.lower() == 'salir':
                                break
                            numero = int(entrada)
                            numeros.append(numero)

                        numeros_pares = [] 
                        for num in numeros:
                            if num % 2 == 0:
                                numeros_pares.append(num)

                        print("Los números pares en la lista son:")
                        for num in numeros_pares:
                            print(f"- {num}")
                        print("--------------------------------------------------------------")

                    if opcion_nivel4 == 6:
                        print("Ahora vamos a eliminar los números duplicados de una lista")

                        numeros = []
                        while True:
                            entrada = input("Ingresa un número para agregar a la lista (o 'salir' para terminar) => ")
                            if entrada.lower() == 'salir':
                                break
                            numero = int(entrada)
                            numeros.append(numero)

                        numeros_sin_duplicados = set(numeros)
                        print("La lista sin números duplicados es:")
                        for num in numeros_sin_duplicados:
                            print(f"- {num}")
                        print("--------------------------------------------------------------")

                    if opcion_nivel4 == 7:
                        print("Saliendo del nivel 4. ¡Hasta luego!")
                        break
                except ValueError:
                    print("Ingresaste un dato erroneo, intenta de nuevo")

        if opcion == 5:
            print(f"Gracias por utilizar el codigo, espero verte pronto {name}!")
            break

    except ValueError:
        print("Ingresaste un dato erroneo, intenta de nuevo")
        print("--------------------------------------------------------------")