# music_shop_22_10
# Tienda de Instrumentos

Este programa simula una tienda de musicales, donde se gestionan las ventas, el inventario (dependiend del stock) y el balance de la tienda a través de clases y herencias en Python. En este caso, la tienda vende tres instrumentos distintos (violín, trombón, batería) y cada uno de estos está registrado en una de las familias de instrumento (cuerda, viento y percusión. Para testear el programa, se ha ejecutado un caso posible en el que el dueño decide vender x número de instruemntos, añadidos previamente.

## Características principales

### Superclase: `Instrumento`
La clase `Instrumento` es la clase base para todos los instrumentos de la tienda. Tiene los siguientes atributos:
- **Fabricante**: Un `string` que indica el fabricante del instrumento.
- **Precio**: Un `integer` o `float` que representa el precio del instrumento. Debe ser un valor positivo.

Ambos atributos son privados, y se accede a ellos a través de métodos *getter* y *setter*. Además, se manejan errores de tipo y signo:
- `TypeError` si el fabricante no es un `string` o el precio no es numérico.
- `ValueError` si el precio es menor o igual a 0.

### Subclases: Instrumentos Específicos
Los instrumentos heredan de la clase `Instrumento`, y cada uno agrega atributos y validaciones específicas:

- **`Violin`**
  - **Stock**: Un `integer` que indica la cantidad de unidades disponibles en inventario. Debe ser mayor o igual a 0.
  - **Modelo**: Un `string` que identifica el modelo del instrumento.
  - **Familia**: Siempre será `'Cuerda'`. Si se intenta asignar otro valor, lanzará un `ValueError`.

- **`Trombon`** y **`Bateria`**
  - Al igual que el `Violin`, pero con una validación diferente en el atributo `familia`. El `Trombon` pertenece a la familia `'Viento'` y la `Bateria` a `'Percusion'`.

### Clase `Duenio`
Esta clase simula la gestión de la tienda. El dueño puede:
- **Agregar instrumentos** al inventario.
- **Realizar ventas**, lo que reduce el stock y actualiza el balance de la tienda y el inventario actual (en caso de stock = 0).
- **Visualizar el inventario y el balance económico de la tienda** con los detalles de cada instrumento.
- **Guardar el inventario** en un archivo de texto (`inventario.txt`).

## Para ejecutar lo anterior, se han existen las siguientes clases:
- **`Duenio.agregar_instrumento()`**: Agrega un instrumento al inventario.
- **`Duenio.venta()`**: Realiza la venta de un instrumento y actualiza el inventario y balance.
- **`Duenio.datos_tienda()`**: Muestra el inventario y el balance de la tienda.
- **`Duenio.guardar_inventario()`**: Guarda el inventario en un archivo de texto.

### Para comprobar errores posibles en las distintas clases, se han encapsulado las siguientes funciones dentro de las clases:
- **`Instrumento.test_instrumento()`**: Prueba los métodos y validaciones de la clase `Instrumento`.
- **`Violin.test_violin()`**, **`Trombon.test_trombon()`**, **`Bateria.test_bateria()`**: Prueban los métodos y validaciones específicas de cada subclase.

## Testeo
El archivo incluye una sección de pruebas (main) con lo siguiente:
- Prueba de errores en los atributos de cada clase (instanciando las funciones que se han mencionado previamente).
- Caso real de un dueño de la tienda que añade instrumentos y efectua ventas.
