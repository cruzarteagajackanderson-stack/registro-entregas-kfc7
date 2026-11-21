# Análisis del proceso de recepción de productos en KFC

## 1. Problema identificado

Durante la observación del proceso de recepción de productos se identificó que el registro de cantidades se realiza manualmente. Esta situación puede ocasionar errores de escritura, pérdida de información, dificultades para consultar registros anteriores y diferencias entre las cantidades solicitadas y recibidas.

Por ejemplo, en una recepción se solicitaron 40 cajas de pollo fresco troceado, pero se recibieron 38, identificándose 2 cajas faltantes.

## 2. Objetivo

Desarrollar un prototipo en Python que permita registrar, almacenar, mostrar y buscar las recepciones de productos, facilitando el control de las cantidades solicitadas y recibidas.

## 3. Entradas, procesos y salidas

### Entradas
- Número de guía.
- Nombre del proveedor.
- Nombre del producto.
- Presentación del producto.
- Cantidad solicitada.
- Cantidad recibida.

### Procesos
- Validar los datos ingresados.
- Comparar las cantidades solicitadas y recibidas.
- Calcular las diferencias.
- Guardar los registros en un archivo.
- Cargar los registros en una lista.
- Mostrar y buscar recepciones.

### Salidas
- Confirmación del registro.
- Cantidad de productos faltantes.
- Cantidad de productos adicionales.
- Estado de conformidad.
- Información de las recepciones registradas.

## 4. Pseudocódigo

INICIO

Mostrar menú principal.

Mientras la opción no sea salir:

    Solicitar opción.

    Si opción es 1:
        Solicitar datos de recepción.
        Validar los datos.
        Comparar cantidades.
        Calcular diferencias.
        Guardar recepción en archivo.

    Si opción es 2:
        Cargar recepciones en una lista.
        Mostrar los registros.

    Si opción es 3:
        Solicitar número de guía.
        Buscar recepción en la lista.
        Mostrar resultado.

    Si opción es 4:
        Finalizar programa.

FIN

## 5. Pruebas del prototipo

Las siguientes pruebas deben ejecutarse en la terminal para registrar los resultados reales.

| Prueba | Datos o acción | Resultado esperado | Resultado obtenido |
|---|---|---|---|
| 1 | Solicitar 40 y recibir 38 | Mostrar 2 faltantes | El programa identificó que se solicitaron 40 cajas y se recibieron 38, por lo que calculó correctamente 2 cajas faltantes y registró la recepción|
| 2 | Solicitar 40 y recibir 40 | Mostrar recepción conforme | . El programa comprobó que las 40 cajas solicitadas coinciden con las 40 cajas recibidas y registró la recepción como conforme.|
| 3 | Ingresar cantidad negativa | Rechazar el dato |El programa rechazó el valor negativo (-5), mostrando el mensaje «La cantidad solicitada debe ser mayor que cero» y evitando registrar la recepción. |
| 4 | Ingresar letras en la cantidad | Rechazar el dato |El programa rechazó las letras ingresadas en la cantidad y mostró un mensaje indicando que debe ser un número mayor que cero. |
| 5 | Buscar guía registrada | Mostrar la recepción |Prueba realizada correctamente. El programa encontró la recepción mediante su número de guía y mostró los datos registrados, identificando 2 cajas faltantes. |
| 6 | Buscar guía inexistente | Mostrar que no se encontró | Prueba realizada correctamente. El programa no encontró la guía ingresada porque no existe en los registros almacenados. |

## 6. Validaciones y correcciones

El prototipo incorpora validaciones para comprobar que el número de guía tenga una longitud mínima, que los campos de texto no estén vacíos y que las cantidades ingresadas sean numéricas y válidas.

Las pruebas permitirán identificar posibles errores. Las correcciones realizadas se documentarán después de comprobar el comportamiento del programa.

## 7. Recursos de programación utilizados

- Estructuras de control: while, if, elif, else y for.
- Funciones: validación, registro, búsqueda y visualización.
- Listas: almacenamiento temporal de las recepciones mediante una lista de Python.
- Cadenas de caracteres: procesamiento de guías y datos de productos.
- Archivos: almacenamiento permanente en recepciones.txt.
- Módulos: separación del programa en main.py y utilidades.py.
- Git y GitHub: registro progresivo de los cambios del proyecto.

## 8. Conclusión

El prototipo permite organizar el registro de recepción de productos mediante herramientas de programación en Python. Su funcionamiento facilita la identificación de diferencias entre las cantidades solicitadas y recibidas, además de permitir consultar la información almacenada.