expedientes = []
contador = 1


def mostrar_menu():
    print("==================================================")
    print("           MESA DE PARTES DIGITAL")
    print('        IESTP "MANUEL AREVALO CACERES"')
    print("             LOS OLIVOS - LIMA")
    print("==================================================")
    print()
    print("1. Registrar expediente")
    print("2. Buscar expediente por codigo")
    print("3. Mostrar todos los expedientes")
    print("4. Ordenar expedientes por codigo")
    print("5. Guardar expedientes")
    print("6. Salir")
    print()


def registrar_expediente():
    global contador

    print("\n--- REGISTRO DE EXPEDIENTE ---")

    dni = input("Ingrese DNI del ciudadano: ")

    if len(dni) != 8 or not dni.isdigit():
        print("Error: el DNI debe tener 8 digitos numericos.")
        return

    nombre = input("Ingrese nombres y apellidos: ").strip()

    if nombre == "":
        print("Error: el nombre no puede estar vacio.")
        return

    tipo_documento = input("Ingrese tipo de documento: ").strip()

    if tipo_documento == "":
        print("Error: debe ingresar el tipo de documento.")
        return

    asunto = input("Ingrese el asunto del expediente: ").strip()

    if asunto == "":
        print("Error: debe ingresar el asunto.")
        return

    expediente = {
        "codigo": contador,
        "dni": dni,
        "nombre": nombre,
        "tipo_documento": tipo_documento,
        "asunto": asunto
    }

    expedientes.append(expediente)
    contador += 1

    print("\nExpediente registrado correctamente.")
    print("Codigo:", expediente["codigo"])
    print("DNI:", dni)
    print("Ciudadano:", nombre)
    print("Tipo de documento:", tipo_documento)
    print("Asunto:", asunto)


def buscar_expediente():
    print("\n--- BUSCAR EXPEDIENTE ---")

    codigo = input("Ingrese el codigo del expediente: ")

    if not codigo.isdigit():
        print("Error: el codigo debe ser numerico.")
        return

    codigo = int(codigo)

    for expediente in expedientes:
        if expediente["codigo"] == codigo:
            print("\nExpediente encontrado:")
            print("Codigo:", expediente["codigo"])
            print("DNI:", expediente["dni"])
            print("Ciudadano:", expediente["nombre"])
            print("Tipo de documento:", expediente["tipo_documento"])
            print("Asunto:", expediente["asunto"])
            return

    print("No se encontro un expediente con ese codigo.")


def mostrar_expedientes():
    print("\n--- LISTA DE EXPEDIENTES ---")

    if len(expedientes) == 0:
        print("Todavia no hay expedientes registrados.")
        return

    for expediente in expedientes:
        print("------------------------------")
        print("Codigo:", expediente["codigo"])
        print("DNI:", expediente["dni"])
        print("Ciudadano:", expediente["nombre"])
        print("Tipo de documento:", expediente["tipo_documento"])
        print("Asunto:", expediente["asunto"])

    print("------------------------------")
    print("Total de expedientes:", len(expedientes))


def main():
    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_expediente()

        elif opcion == "2":
            buscar_expediente()

        elif opcion == "3":
            mostrar_expedientes()

        elif opcion == "4":
            print("\nEsta opcion esta pendiente de implementacion.")

        elif opcion == "5":
            print("\nEsta opcion esta pendiente de implementacion.")

        elif opcion == "6":
            print("\nGracias por utilizar la Mesa de Partes Digital.")
            break

        else:
            print("\nOpcion no valida. Intente nuevamente.")

        input("\nPresione ENTER para continuar...")


if __name__ == "__main__":
    main()

