# Importar funciones del módulo utilidades
from utilidades import (
    validar_guia,
    validar_texto,
    validar_cantidad,
    registrar_recepcion,
    mostrar_recepciones,
    buscar_recepcion
)


# Menú principal
def menu():

    while True:

        print("\n===== CONTROL DE RECEPCIÓN DE PRODUCTOS KFC =====")
        print("1. Registrar recepción")
        print("2. Mostrar recepciones")
        print("3. Buscar recepción por guía")
        print("4. Salir")

        opcion = input("Seleccione una opción: ").strip()

        # Registrar una recepción
        if opcion == "1":

            guia = input("Número de guía: ").strip()

            if not validar_guia(guia):
                print("Número de guía inválido.")
                continue

            proveedor = input("Nombre del proveedor: ").strip()

            if not validar_texto(proveedor):
                print("El proveedor no puede estar vacío ni contener |.")
                continue

            producto = input("Nombre del producto: ").strip()

            if not validar_texto(producto):
                print("El producto no puede estar vacío ni contener |.")
                continue

            presentacion = input("Presentación del producto: ").strip()

            if not validar_texto(presentacion):
                print("La presentación no puede estar vacía ni contener |.")
                continue

            solicitadas = input("Cantidad solicitada: ").strip()

            if not validar_cantidad(solicitadas):
                print("La cantidad solicitada debe ser mayor que cero.")
                continue

            recibidas = input("Cantidad recibida: ").strip()

            if not validar_cantidad(recibidas, permitir_cero=True):
                print("La cantidad recibida no puede ser negativa.")
                continue

            registrar_recepcion(
                guia,
                proveedor,
                producto,
                presentacion,
                int(solicitadas),
                int(recibidas)
            )

            print("Recepción registrada correctamente.")

        # Mostrar las recepciones
        elif opcion == "2":

            mostrar_recepciones()

        # Buscar una recepción
        elif opcion == "3":

            guia = input("Ingrese el número de guía: ").strip()
            buscar_recepcion(guia)

        # Salir del programa
        elif opcion == "4":

            print("Programa finalizado.")
            break

        else:

            print("Opción incorrecta. Intente nuevamente.")


# Ejecutar el programa
menu()
