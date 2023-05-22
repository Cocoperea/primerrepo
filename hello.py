def mostrar_menu():
    print("---- Menú Principal ----")
    print("1. Mostrar agenda")
    print("2. Agregar contacto")
    print("3. Modificar contacto")
    print("4. Eliminar contacto")
    print("5. Buscar contacto por nombre")
    print("6. Buscar contacto por número telefónico")
    print("7. Salir")

def mostrar_agenda():
    with open('agenda.txt', 'r') as file:
         print("Agenda:")
         for line in file:
            contact_data = line.strip().split(',')
            nombre = contact_data[0]
            telefono = contact_data[1]
            datos_adicionales = contact_data[2:]
            print(f"Nombre: {nombre}, Teléfono: {telefono}, Datos adicionales: {', '.join(datos_adicionales)}")
    

def agregar_contacto(nombre, telefono, datos_adicionales):
    with open('agenda.txt', 'r') as file:
        for line in file:
            contact_data = line.strip().split(',')
            if contact_data[1] == telefono:
                    print("El número de teléfono ya existe en la agenda. No se puede agregar el contacto.")
                    return
    with open ('agenda.txt', 'a') as file:
            file.write(f"{nombre},{telefono},{datos_adicionales}\n")       
    print("Contacto agregado con éxito.")


def modificar_contacto(nombre, nuevo_telefono, datos_adicionales):
    with open('agenda.txt', 'r') as file:
        lines = file.readlines()
    with open('agenda.txt', 'w') as file:
        contact_found = False
        for line in lines:
            contact_data = line.strip().split(',')
            line_nombre = contact_data[0]
            if line_nombre == nombre:
                line = f"{nombre},{nuevo_telefono},{datos_adicionales}\n"
                contact_found = True
            file.write(line)
        if contact_found:
            print("Contacto modificado con éxito.")
        else:
            print("El contacto no existe en la agenda.")

def eliminar_contacto(nombre):
    with open('agenda.txt', 'r') as file:
        lines = file.readlines()
    with open('agenda.txt', 'w') as file:
        contact_found = False
        for line in lines:
            contact_data = line.strip().split(',')
            line_nombre = contact_data[0]
            if line_nombre == nombre:
                contact_found = True
            else:
                file.write(line)
        if contact_found:
            print("Contacto eliminado con éxito.")
        else:
            print("El contacto no existe en la agenda.")

def buscar_contacto_por_nombre(nombre):
    with open('agenda.txt', 'r') as file:
        contactos_encontrados = []
        for line in file:
            line_nombre, telefono, datos_adicionales = line.strip().split(',')
            if nombre.lower() in line_nombre.lower():
                    contactos_encontrados.append((line_nombre, telefono, datos_adicionales))
        if contactos_encontrados:
            print("Contactos encontrados:")
            for contacto in contactos_encontrados:
                print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Datos adicionales: {contacto[2]}")
        else:
            print("No se encontraron contactos en la agenda con ese nombre.")

def buscar_contacto_por_telefono(telefono):
    with open('agenda.txt', 'r') as file:
        contactos_encontrados = []
        for line in file:
            nombre, line_telefono, datos_adicionales = line.strip().split(',')
            if telefono in line_telefono:
                    contactos_encontrados.append((nombre, line_telefono, datos_adicionales))
        if contactos_encontrados:
            print("Contactos encontrados:")
            for contacto in contactos_encontrados:
                print(f"Nombre: {contacto[0]}, Teléfono: {contacto[1]}, Datos adicionales: {contacto[2]}")
        else:
            print("No se encontraron contactos en la agenda con ese número telefónico.")
    
def menu_principal():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            mostrar_agenda()
        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono: ")
            datos_adicionales = input("Ingrese los datos adicionales separados por comas (Ejemplo: correo,dirección): ")
            agregar_contacto(nombre, telefono, datos_adicionales)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto a modificar: ")
            nuevo_telefono = input("Ingrese el nuevo número de teléfono: ")
            datos_adicionales = input("Ingrese los nuevos datos adicionales separados por comas (Ejemplo: correo,dirección): ")
            modificar_contacto(nombre, nuevo_telefono, datos_adicionales)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif opcion == "5":
            nombre = input("Ingrese el nombre del contacto a buscar: ")
            buscar_contacto_por_nombre(nombre)
        elif opcion == "6":
            telefono = input("Ingrese el número de teléfono a buscar: ")
            buscar_contacto_por_telefono(telefono)
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
             print("Opción inválida. Por favor, ingrese una opción válida.")

menu_principal()