
# Proyecto: Registro de Entregas KFC7

## 1. Descripción del proyecto

El proyecto consiste en desarrollar un programa en Python
que permita registrar, mostrar y buscar las entregas
realizadas por los estudiantes.

## 2. Pseudocódigo preliminar

ALGORITMO REGISTRO_ENTREGAS_KFC7

INICIO

    REPETIR

        MOSTRAR "1. Registrar entrega"
        MOSTRAR "2. Mostrar entregas"
        MOSTRAR "3. Buscar entrega"
        MOSTRAR "4. Salir"

        LEER opcion

        SEGÚN opcion HACER

            CASO 1:
                LEER código del estudiante
                VALIDAR código

                SI el código es válido ENTONCES
                    LEER nombre
                    LEER tipo de entrega
                    VALIDAR tipo
                    LEER descripción
                    GUARDAR entrega en archivo
                FIN SI

            CASO 2:
                LEER entregas del archivo
                MOSTRAR entregas

            CASO 3:
                LEER código del estudiante
                BUSCAR código en el archivo

                SI se encuentra ENTONCES
                    MOSTRAR entrega
                SINO
                    MOSTRAR "Entrega no encontrada"
                FIN SI

            CASO 4:
                MOSTRAR "Programa finalizado"

            DE OTRO MODO:
                MOSTRAR "Opción incorrecta"

        FIN SEGÚN

    HASTA QUE opcion = 4

FIN

## 3. Pruebas del programa

Se comprobará el registro, la visualización,
la búsqueda y la validación de datos.

## 4. Conclusión

El prototipo permite registrar, almacenar,
mostrar y buscar entregas mediante un programa
desarrollado en Python.