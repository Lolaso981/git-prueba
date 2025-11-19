print("Bienvenido al sistema de calificaciones")
name = input("Por favor, ingresa tu nombre: ")

while True:
    try:
        print(f"Hola {name}, ingresa la cantidad de calificaciones que deseas ingresar, luego calcularemos su promedio:")
        num_grades = input()
        if num_grades.isdigit():
            num_grades = int(num_grades)
            if num_grades <= 0:
                print("Por favor, ingresa un número positivo mayor que cero.")
                continue
        else:
            print("El valor ingresado no es un número entero válido. Intenta de nuevo.")
            continue
        grades = []
        for i in range(num_grades):
            while True:
                try:
                    entrada = input(f"Ingresa la calificación #{i + 1}: ")
                    if not entrada.replace('.', '', 1).isdigit():
                        print("Solo se permiten números (por ejemplo: 85 o 90.5). Intenta de nuevo.")
                        continue
                    grade = float(entrada)
                    if 0 <= grade <= 100:
                        grades.append(grade)
                        break
                    else:
                        print("Por favor, ingresa una calificación entre 0 y 100.")
                except ValueError:
                    print("Entrada inválida. Por favor, ingresa un número válido.")
        average = sum(grades) / num_grades
        print(f"\n{name}, el promedio de tus calificaciones es: {average:.2f}")
        break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")