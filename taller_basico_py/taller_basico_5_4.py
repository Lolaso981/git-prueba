print("--------------------------------------")
print("Bienvenido al gestor de estudiantes")
print("--------------------------------------")

name = input("Por favor, ingresa tu nombre: ")
while True:
    if name.isalpha():
        break
    else:
        print("El nombre solo debe contener letras. Intenta de nuevo.")
        name = input("Por favor, ingresa tu nombre: ")

students = []

while True:
    try:
        print("--------------------------------------")
        print(f"Hola {name}, a continuacion podras ver las opciones a realizar")
        print("1. Agregar estudiante")
        print("2. Ver lista de estudiantes")
        print("3. Modificar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")

        opcion = int(input("Selecciona una opcion (1-5): "))
        if opcion == 1:
            student_name = input("Ingresa el nombre del estudiante a agregar: ")

            while True:
                if student_name.isalpha():
                    students.append(student_name)
                    print("--------------------------------------")
                    print(f"Estudiante {student_name} agregado exitosamente.")
                    break
                else:
                    print("El nombre solo debe contener letras. Intenta de nuevo.")
                    student_name = input("Ingresa el nombre del estudiante a agregar: ")

        elif opcion == 2:
            print("--------------------------------------")
            if not students:
                print("No hay estudiantes en la lista.")
            else:
                print("Lista de estudiantes:")
                for idx, student in enumerate(students, start=1):
                    print(f"{idx}. {student}")
            continue

        elif opcion == 3:
            if not students:
                print("--------------------------------------")
                print("No hay estudiantes para modificar.")
                continue

            print("Lista de estudiantes:")
            for idx, student in enumerate(students, start=1):
                print(f"{idx}. {student}")

            try:
                student_index = int(input("Ingresa el numero del estudiante a modificar: ")) - 1
                if 0 <= student_index < len(students):
                    new_name = input("Ingresa el nuevo nombre del estudiante: ")
                    while True:
                        if new_name.isalpha():
                            old_name = students[student_index]
                            students[student_index] = new_name
                            print("--------------------------------------")
                            print(f"Estudiante {old_name} modificado a {new_name} exitosamente.")
                            break
                        else:
                            print("El nombre solo debe contener letras. Intenta de nuevo.")
                            new_name = input("Ingresa el nuevo nombre del estudiante: ")
                else:
                    print("Indice invalido. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número válido.")
            
        elif opcion == 4:
            if not students:
                print("--------------------------------------")
                print("No hay estudiantes para eliminar.")
                continue

            print("Lista de estudiantes:")
            for idx, student in enumerate(students, start=1):
                print(f"{idx}. {student}")

            try:
                student_index = int(input("Ingresa el numero del estudiante a eliminar: ")) - 1
                if 0 <= student_index < len(students):
                    removed_student = students.pop(student_index)
                    print("--------------------------------------")
                    print(f"Estudiante {removed_student} eliminado exitosamente.")
                else:
                    print("Indice invalido. Intenta de nuevo.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número válido.")

        elif opcion == 5:
            print("--------------------------------------")
            print(f"Gracias por usar el gestor de estudiantes, {name}. ¡Hasta luego!")
            break
    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número válido para la opción.")