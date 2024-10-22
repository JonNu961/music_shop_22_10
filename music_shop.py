# Super clase instrumento:
#   Esta clase tiene tres atributos basicos que tendrán los instrumentos y
#   se ocupara de los errores por tipo de clase (TypeError) y signo (con getter y setter) de estos últimos:
#       Fabricante: tiene que ser un string.
#       Precio: debe de ser un integer o float y ser positivo.
#   Ambos serán atributos privados por seguridad (EN EL GETTER!!!). (Las características definidas
#   para los atributos con getter y setter también serán herenciadas!)

class Instrumento:
    def __init__(self, fabricante, precio):
       self.fabricante = fabricante #OJO, si defines como privado el atributo en el constructor,
       # después el setter no va a ir; ya se ha alterado internamente el nombre del atributo,
       self.precio = precio

    # Getter para fabricante (aquí sí se define como privado el atributo):
    @property
    def fabricante (self):
        return self.__fabricante

    # Setter para fijar el posible fallo (con raise == flanco):
    @fabricante.setter
    def fabricante(self, valor):
        if not isinstance(valor, str):
            raise TypeError('Fabricante incorrecto, no es un string. Intentelo otra vez.')
        self.__fabricante = valor

    # Procedimiento casi idéntico para el atributo "precio"
    @property
    def precio (self):
        return self.__precio

    @precio.setter
    def precio (self, valor):
        # Error por clase del input:
        if not isinstance(valor, (int ,float)):
            raise TypeError('Precio incorrecto, no es un integer o float. Intentelo otra vez.')

        # Error si el input de precio no es mayor que cero.
        elif valor <= 0:
            raise ValueError('El precio tiene que ser mayor a 0. Intentelo otra vez.')
        self.__precio = valor

    # Por último, defino una función para testear la clase. Ya que esta función no altera
    # la clase ni se nutre de atributos o metodos de esta misma, le añado el decorador @staticmethod.
    # De esta mmanera cada test y los atr./met. de la clase quedan encapsulados en uno (en el main
    # hay que llamar a Instrumento, ya que no es una función fuera de la clase).

    @staticmethod
    def test_instrumento():
        # Si el fabricante no es de la clase string:
        try:
            instrument = Instrumento(1, 2000)
        except TypeError as e:
            print(e)

        # Si el precio no es de la clase integer o float:
        try:
            instrument = Instrumento('Bösendorfer', '2')
        except TypeError as e:
            print(e)

        # Si el precio es inferior o igual a cero:
        try:
            instrument = Instrumento('Bösendorfer', -200)
        except ValueError as e:
            print(e)

        # Todos los inputs son correctos (los flancos no saltan y no aparecen errores en la consola):
        try:
            instrument = Instrumento('Bösendorfer', 5000)
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)

# Una vez definida la super clase instrumento, definimos los instrumentos que se venden en la
# tienda. Cada uno de estos herenciará los tres atributos de la super clase Instrumento y se les
# añadira lo siguiente (con getters y setters):
#   Stock: tendra que ser un integer y mayor o igual que cero. Representa el número de existencias
#          de dicho instrumento.
#   Modelo: tendra que ser un string.
#   Familia de instrumento: en base al instrumento adquirirá un valor (string) y se tendrá que respetar.
#       * Es decir, si introduzco como dueño de la tienda un violín como instrumento de viento dara un error.
# Para simplificar, habrá 3 instrumentos, uno por cada familia principal.
class Violin(Instrumento):
    def __init__(self, fabricante, precio, stock, modelo, familia):
        super().__init__(fabricante, precio) # Herenciar de la superclase Instrumento.
        #Definición de nuevos atributos.
        self.stock = stock
        self.modelo = modelo
        self.familia = familia

    @property
    def stock (self):
        return self.__stock

    @stock.setter
    def stock(self, valor):
        # Error por clase del input:
        if not isinstance(valor, int):
            raise TypeError('El número de existencias es incorrecto, no es un integer. Intentelo otra vez.')

        # Error si el input de precio no es mayor que cero.
        elif valor < 0:
            raise ValueError('El stock tiene que ser mayor o igual 0. Intentelo otra vez.')
        self.__stock = valor

    @property
    def modelo (self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        if not isinstance(valor, str):
            raise TypeError('Modelo incorrecto, no es un string. Intentelo otra vez.')
        self.__modelo = valor

    @property
    def familia (self):
        return self.__familia

    @familia.setter
    def familia(self, valor):
        if not isinstance(valor, str):
            raise TypeError('Familia de instrumento incorrecta, no es un string. Intentelo otra vez.')
        elif not valor == 'Cuerda':
            raise ValueError('El violín pertenece a la familia cuerda. Intentelo otra vez.')
        self.__familia = valor


    @staticmethod
    def test_violin():
        # Si el fabricante no es de la clase string (PARA COMPROBAR INHERITANCE DE LOS SET/GET):
        try:
            violin = Violin(1, 1725, 100, 'V 20 G 4/4', 'Cuerda')
        except TypeError as e:
            print(e)

        # Si el stock no es de la clase integer:
        try:
            violin = Violin('Yamaha', 2000, '1', 'V 20 G 4/4', 'Cuerda')
        except TypeError as e:
            print(e)

        # Si el stock es negativo:
        try:
            violin = Violin('Yamaha', 2000, -10, 'V 20 G 4/4', 'Cuerda')
        except ValueError as e:
            print(e)

        # Si el modelo no es de la clase string:
        try:
            violin = Violin('Yamaha', 2000, 10, 20, 'Cuerda')
        except TypeError as e:
            print(e)

        # Si la familia no es de la clase string:
        try:
            violin = Violin('Yamaha', 2000, 10, 'V 20 G 4/4', 2)
        except TypeError as e:
            print(e)

        # Si la familia no es correcta (cuerda):
        try:
            violin = Violin('Yamaha', 2000, 10, 'V 20 G 4/4', 'Viento')
        except ValueError as e:
            print(e)

# Una vez definido un instrumento (violín) se pueden herenciar de está los atributos cambiando solo lo que
# diferencia un instrumento de otro (en este caso): la familia.
class Trombon(Violin):
    def __init__(self, fabricante, precio, stock, modelo, familia):
        super().__init__(fabricante, precio, stock, modelo, familia)

    # Redefino el getter y setter de familia para que satisfaga a trombon (familia == viento):
    # OJO: el TypeError de string también se redefine!!!!
    @property
    def familia (self):
        return self.__familia

    @familia.setter
    def familia(self, valor):
        if not isinstance(valor, str):
            raise TypeError('Familia de instrumento incorrecta, no es un string. Intentelo otra vez.')
        if not valor == 'Viento':
            raise ValueError('El trombón pertenece a la familia viento. Intentelo otra vez.')
        self.__familia = valor

    # Como ha ocurrido previamente en Violin con los atributos de Instrumento, solo tendremos que
    # comprobar que la familia del trombón es de viento:
    @staticmethod
    def test_trombon():
         try:
             trombon = Trombon('Thomman', 2000, 10, 'Classic TEB480 L', 'Percusion')
         except ValueError as e:
             print(e)
         # Por si acaso verificamos un error herenciado de Violin:
         try:
             trombon = Trombon('Thomman', 2000, 10, 'Classic TEB480 L', 2)
         except TypeError as e:
             print(e)

# Hacemos lo propio para la clase restante:
class Bateria(Violin):
    def __init__(self, fabricante, precio, stock, modelo, familia):
        super().__init__(fabricante, precio, stock, modelo, familia)

    # Redefino el getter y setter de familia para que satisfaga a trombon (familia == viento):
    # OJO: el TypeError de string también se redefine!!!!
    @property
    def familia (self):
        return self.__familia

    @familia.setter
    def familia(self, valor):
        if not isinstance(valor, str):
            raise TypeError('Familia de instrumento incorrecta, no es un string. Intentelo otra vez.')
        if not valor == 'Percusion':
            raise ValueError('La batería pertenece a la familia percusión. Intentelo otra vez.')
        self.__familia = valor

    @staticmethod
    def test_bateria():
        try:
            bateria = Bateria('Pearl', 1099, 10, 'EXX725BR/C', 2)
        except TypeError as e:
            print(e)
        # Por si acaso verificamos un error herenciado de Violin:
        try:
            bateria = Bateria('Pearl', 1099, 10, 'EXX725BR/C', 'Viento')
        except ValueError as e:
            print(e)

# Ya identificadas las clases principales de nuestra tienda, creo la clase "Duenio".
# * (mejor no herenciar tres clases a la vez en este caso duenio. Se instanciara cada instrumento en el main).
# **(por simplificar el código no se han añadido excepciones de error por tipos de clase (string, float...)
#    en esta clase).

# El dueño tendra a su alcance las siguientes acciones:
#   Añadir un instrumento a un inventario.
#   Vender instrumentos y, por lo tanto, reducir el stock del modelo vendido.
#       * Si llega a cero el stock de un modelo, se elimina dicho instrumento (o fila).
#   Visualizar el inventario.
#   Ver el balance actual de la tienda en base a las ventas.
#   Guardar el inventario en un fichero.

class Duenio():
    def __init__(self, filename, balance_tienda = 0):
        self.inventario = [] # Por default la tienda empieza sin exsitencias.
        # (posible mejora metodo cargar_inventario para generar y poder cargar desde
        # el inicio inventarios existentes).
        self.filename = filename
        self.balance_tienda = balance_tienda

    # Cada instrumento se meterá en la lista inventario y está se guardar en el fichero mediante
    # el metodo "guardar_inventario".
    def agregar_instrumento(self, instrumento):
        self.inventario.append(instrumento)
        self.guardar_inventario()

    # Si se vende un instrumento, el stock de este último variará. Si se queda a cero se eliminará.
    def venta(self, modelo): # Se tiene en cuenta el modelo ya que puede haber más de un mismo tipo de instr.
        # Bucle for para encontrar, uno a uno, aquel instrumento que se ha vendido.
        for instrumento in self.inventario:
            # Para discernir el modelo, se compara el valor de este último:
            if instrumento.modelo == modelo:
                # Si el stock es mayor de cero, se sigue restando al stock existente y se suma el precio
                # correspondiente del modelo vendido al balance de la tienda.
                if instrumento.stock > 0:
                    instrumento.stock -= 1
                    self.balance_tienda += instrumento.precio
                    print(f'\nHemos vendido el modelo {modelo}.')
                    print(f'Las existencias de dicho modelo son {instrumento.stock}.')

                    # DESPUÉS DE HACER UNA VENTA, si llega a cero = no queda stock, por lo que se elimina del inventario.
                    if instrumento.stock == 0:
                        print(f'Se ha terminado el stock del {modelo}. ** ELIMINANDO DE INVENTARIO **')
                        self.inventario.remove(instrumento)
                    self.guardar_inventario() # Actualizamos el archivo.
                else:
                    print(f'Stock agotado para el modelo {modelo}.')

    def datos_tienda(self):
        # En caso de que el inventario este vacio avisar al dueño:
        if not self.inventario:
           print('INVENTARIO VACIO!')

        # Visualizamos el inventario:
        print(f'El inventario acutal contiene lo siguiente:')
        for instrumento in self.inventario:
            print(f'Fabricante: {instrumento.fabricante}, Precio: {instrumento.precio},'
                  f' Stock: {instrumento.stock}, Modelo: {instrumento.modelo}, Familia: {instrumento.familia}')

        # Y el balance:
        print(f'\nEl balance actual de la tienda es de: {self.balance_tienda} €.')

    # Por último el metodo con el que creamos el fichero que contiene el inventario:
    def guardar_inventario(self):
        try:
            with open(self.filename, 'w') as file:
                for instrumento in self.inventario:
                    file.write(f'{instrumento.fabricante},{instrumento.precio},{instrumento.stock},'
                           f'{instrumento.modelo},{instrumento.familia}\n')
        except FileNotFoundError:
                print('El archivo no se encuentra definido.')

# Zona de pruebas con las funciones que he definido en cada clase:
if __name__ == '__main__':
    print('\n--- Test Instrumento ---\n')
    Instrumento.test_instrumento()

    print('\n--- Test Violín ---\n')
    Violin.test_violin()

    print('\n--- Test Trombón ---\n')
    Trombon.test_trombon()

    print('\n--- Test Batería ---\n')
    Bateria.test_bateria()

    print('\n--- Test Duenio ---\n')
    # Definimos el nombre del archivo a guardar el inventario.
    duenio = Duenio('inventario.txt')

    # Agregamos varios instrumentos de distintos modelos:
    try:
        violin_yamaha = Violin('Yamaha', 2000, 10, 'V 20 G 4/4', 'Cuerda')
        violin_stentor = Violin('Stentor', 599, 1, 'SR1864 Verona 4/4', 'Cuerda')
        trombon = Trombon('Antoine Courtois', 9999, 3, 'AC551BHA Bass', 'Viento')

        duenio.agregar_instrumento(violin_yamaha)
        duenio.agregar_instrumento(violin_stentor)
        duenio.agregar_instrumento(trombon)
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

    # Visualizamos si nuestra tienda ya tiene o no las existencias definidas.
    duenio.datos_tienda()

    # Cometemos un error al nombrar la familia de uno de los instrumentos:
    try:
        duenio.agregar_instrumento(Bateria('Pearl', 1099, 10,
                                   'EXX725BR/C', 'Cuerda'))
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

    # Logramos alguna venta y vemos si ha bajado el stock y ha subido nuestro balance:
    try:
        duenio.venta('V 20 G 4/4') # Vendemos un violin yamaha.
        duenio.datos_tienda()
        duenio.venta('V 20 G 4/4') # Otro violin yamaha, stock = 8
        duenio.datos_tienda()
        duenio.venta('AC551BHA Bass') # Vendemos un trombón. Nuevo stock = 2
        duenio.datos_tienda()
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

    # Nos quedamos a cero en el stock del violin stentor; tendría que desaparecer de la lista/archivo:
    try:
        duenio.venta('SR1864 Verona 4/4')
        duenio.datos_tienda()
    except TypeError as e:
        print(e)
    except ValueError as e:
        print(e)

    # El metodo guardar_inventario se ejecuta dentro de los metodos agregar instrumento y ventas.