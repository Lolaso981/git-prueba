edad = int(input("Ingresa tu edad: "))
tiene_documento = input("¿Tienes documento de identidad? (si/no): ").strip().lower() == "si"
puede_entrar = (edad >= 18) and tiene_documento
print(f"¿Puede entrar? {puede_entrar}")