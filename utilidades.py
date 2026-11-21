
# Validar el código del estudiante
def validar_codigo(codigo):
    if len(codigo.strip()) >= 6:
        return True
    return False


# Validar el tipo de entrega
def validar_tipo_entrega(tipo):
    tipos = ["tarea", "trabajo", "proyecto", "practica", "otro"]

    if tipo.lower() in tipos:
        return True
    return False


# Registrar una entrega en el archivo
def registrar_entrega(codigo, nombre, tipo, descripcion):
    with open("entregas.txt", "a", encoding="utf-8") as archivo:
        archivo.write(
            f"{codigo}|{nombre}|{tipo}|{descripcion}\n"
        )


# Mostrar todas las entregas
def mostrar_entregas():
    try:
        with open("entregas.txt", "r", encoding="utf-8") as archivo:
            contenido = archivo.readlines()

            if len(contenido) == 0:
                print("No hay entregas registradas.")
            else:
                print("\n===== ENTREGAS REGISTRADAS =====")

                for entrega in contenido:
                    print(entrega.strip())

    except FileNotFoundError:
        print("Todavía no existen entregas registradas.")


# Buscar una entrega mediante el código
def buscar_entrega(codigo):
    encontrado = False

    try:
        with open("entregas.txt", "r", encoding="utf-8") as archivo:

            for linea in archivo:
                datos = linea.strip().split("|")

                if datos[0] == codigo:
                    print("\n===== ENTREGA ENCONTRADA =====")
                    print("Código:", datos[0])
                    print("Nombre:", datos[1])
                    print("Tipo:", datos[2])
                    print("Descripción:", datos[3])

                    encontrado = True

        if not encontrado:
            print("No se encontró ninguna entrega.")

    except FileNotFoundError:
        print("No existen entregas registradas.")