# Validar el número de guía
def validar_guia(guia):
    return len(guia.strip()) >= 6


# Validar que los textos no estén vacíos
def validar_texto(texto):
    return texto.strip() != "" and "|" not in texto


# Validar cantidades
def validar_cantidad(cantidad, permitir_cero=False):
    try:
        numero = int(cantidad)

        if permitir_cero:
            return numero >= 0

        return numero > 0

    except ValueError:
        return False


# Registrar una recepción en el archivo
def registrar_recepcion(guia, proveedor, producto, presentacion,
                        solicitadas, recibidas):

    diferencia = solicitadas - recibidas

    with open("recepciones.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{guia}|{proveedor}|{producto}|{presentacion}|"
            f"{solicitadas}|{recibidas}|{diferencia}\n"
        )

    if diferencia > 0:
        print(f"Recepción incompleta: faltan {diferencia} unidades.")
    elif diferencia < 0:
        print(f"Se recibieron {abs(diferencia)} unidades adicionales.")
    else:
        print("Recepción conforme: las cantidades coinciden.")


# Cargar las recepciones en una lista
def cargar_recepciones():
    recepciones = []

    try:
        with open("recepciones.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.strip().split("|")

                if len(datos) == 7:
                    recepciones.append(datos)

    except FileNotFoundError:
        pass

    return recepciones


# Mostrar todas las recepciones
def mostrar_recepciones():

    recepciones = cargar_recepciones()

    if not recepciones:
        print("No hay recepciones registradas.")
        return

    print("\n===== RECEPCIONES REGISTRADAS =====")

    for datos in recepciones:

        print("\nNúmero de guía:", datos[0])
        print("Proveedor:", datos[1])
        print("Producto:", datos[2])
        print("Presentación:", datos[3])
        print("Cantidad solicitada:", datos[4])
        print("Cantidad recibida:", datos[5])

        diferencia = int(datos[6])

        if diferencia > 0:
            print("Faltantes:", diferencia)
        elif diferencia < 0:
            print("Unidades adicionales:", abs(diferencia))
        else:
            print("Estado: Conforme")


# Buscar una recepción por número de guía
def buscar_recepcion(guia):

    recepciones = cargar_recepciones()
    encontrado = False

    for datos in recepciones:

        if datos[0] == guia:

            print("\n===== RECEPCIÓN ENCONTRADA =====")
            print("Número de guía:", datos[0])
            print("Proveedor:", datos[1])
            print("Producto:", datos[2])
            print("Presentación:", datos[3])
            print("Cantidad solicitada:", datos[4])
            print("Cantidad recibida:", datos[5])

            diferencia = int(datos[6])

            if diferencia > 0:
                print("Cajas faltantes:", diferencia)
            elif diferencia < 0:
                print("Unidades adicionales:", abs(diferencia))
            else:
                print("Estado: Conforme")

            encontrado = True

    if not encontrado:
        print("No se encontró la recepción.")
