
# Importar las funciones del módulo utilidades
from utilidades import (
    validar_codigo,
    validar_tipo_entrega,
    registrar_entrega,
    mostrar_entregas,
    buscar_entrega
)


# Menú principal del programa
def menu():

    while True:

        print("\n===== REGISTRO DE ENTREGAS KFC7 =====")
        print("1. Registrar entrega")
        print("2. Mostrar entregas")
        print("3. Buscar entrega")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        # Registrar entrega
        if opcion == "1":

            codigo = input("Código del estudiante: ").strip()

            if not validar_codigo(codigo):
                print("Código inválido. Debe tener 6 caracteres como mínimo.")
                continue

            nombre = input("Nombre del estudiante: ").strip()

            if nombre == "":
                print("El nombre no puede estar vacío.")
                continue

            tipo = input(
                "Tipo de entrega (tarea, trabajo, proyecto, practica, otro): "
            ).strip()

            if not validar_tipo_entrega(tipo):
                print("Tipo de entrega inválido.")
                continue

            descripcion = input("Descripción de la entrega: ").strip()

            if descripcion == "":
                print("La descripción no puede estar vacía.")
                continue

            registrar_entrega(
                codigo, nombre, tipo, descripcion
            )

            print("Entrega registrada correctamente.")

        # Mostrar entregas
        elif opcion == "2":

            mostrar_entregas()

        # Buscar entrega
        elif opcion == "3":

            codigo = input("Ingrese el código del estudiante: ").strip()

            buscar_entrega(codigo)

        # Salir del programa
        elif opcion == "4":

            print("Programa finalizado.")
            break

        else:

            print("Opción incorrecta. Intente nuevamente.")


# Ejecutar el programa
menu()