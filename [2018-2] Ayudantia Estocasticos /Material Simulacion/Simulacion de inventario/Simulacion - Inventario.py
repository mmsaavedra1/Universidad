import numpy as np


class Simulacion:
    def __init__(self, inventario_minimo, orden_de_destino):
        """
        Aqui se crean los atributos del sistema a simular.
        """
        self.inventario = 0
        self.cantidad_ordenada = 0

        self.tiempo_actual = 0
        self.tiempo_cliente = self.generar_llegadas()
        self.tiempo_delivery = float("inf")

        self.ingresos = 0
        self.costo_ordenes = 0
        self.costo_inventario = 0

        self.cota_de_inventario = inventario_minimo
        self.orden_de_destino = orden_de_destino

    def avanzar_el_tiempo(self):
        """
        Metodo que actualiza el tiempo de los proximos eventos por ocurrir
        que para este caso son solo dos opciones:
        1º --> LLegada de un nuevo cliente
        2º --> Entrega de un delivery
        """

        # Mensaje amigable
        print("[INVENTARIO] Tiempo actual {} e inventario {}\n".format(self.tiempo_actual, self.inventario))

        # Se calcula el tiempo del proximo evento por ocurrir
        tiempo_evento = min(self.tiempo_cliente, self.tiempo_delivery)

        # Se calcula el costo de inventario asociado a la cantidad de
        # dias que han pasado y la cantida de elementos
        # en el inventario durante estos dias.
        self.costo_inventario += 2*self.inventario*(tiempo_evento - self.tiempo_actual)


        # Se analiza que evento realizar primero segun los tiempo del proximo
        # evento por ocurrir y se ejecuta dicho metodo.
        if self.tiempo_delivery <= self.tiempo_cliente:
            self.manejo_evento_delivery()

        else:
            self.manejo_evento_de_cliente()

        # Actualiza el tiempo
        self.tiempo_actual = tiempo_evento


    def manejo_evento_de_cliente(self):
        """Metodo que simula la demanda de productos por cliente"""

        # Genera una demanda por el cliente actual en el sistema.
        demanda = self.generar_demanda()

        # Mensaje amigable
        print("[CLIENTE] Ha llegada un cliente en {} y demanda {} de productos\n".format(self.tiempo_actual, demanda))

        # Analiza si el inventario ACTUAL es mayor que la demanda
        # o no para ver que acciones realizar segun sea el caso.
        if self.inventario > demanda:
            self.ingresos += 100*demanda
            self.inventario -= demanda
        else:
            self.ingresos += 100*demanda
            self.inventario = 0

        # Ahora analiza si una vez realiazada la compra por el usuario
        # se debe realizar un pedido segun la restriccion de cantidad
        # minima en inventario: INVENTARIO < s.

        if (self.inventario < self.cota_de_inventario) and self.cantidad_ordenada == 0:
            self.cantidad_ordenada = self.cota_de_inventario - self.inventario
            self.costo_ordenes += 5*self.cantidad_ordenada
            self.tiempo_delivery = self.tiempo_actual + 2
            self.tiempo_cliente = self.tiempo_actual + self.generar_llegadas()

        else:
            self.tiempo_cliente = self.tiempo_actual + self.generar_llegadas()

    def manejo_evento_delivery(self):
        """
        Metodo que simula el delivery de productos hacia la empresa
        para abastecer el inventario.
        """

        # Se actualiza el inventario actual con la cantidad ordenada 2 dias atras
        self.inventario += self.cantidad_ordenada

        # Mensaje amigable
        print("[ORDEN] Ha llegado a inventario {} en el tiempo {}\n".format(self.cantidad_ordenada, self.tiempo_actual))

        # Se indica que la cantidad ordenada fue recibida.
        self.cantidad_ordenada = 0

        # Tiempo de ocurrencia del proximo delivery se define como "infinito"
        # esto es con el fin de indicar que solamente ocurriran llegadas
        # de clientes en el corto plazo a menos que se quede sin inventario
        # y se pida una nueva orden de delivery fijando un nuevo
        # tiempo de delivery.
        self.tiempo_delivery = float("inf")

    def generar_llegadas(self):
        """
        Metodo que genera tiempos aleatorios de llegadas al sistema
        """
        return np.random.exponential(5)

    def generar_demanda(self):
        """
        Metodo que genera una demanda aleatoria de productos
        """
        return np.random.randint(1, 5)

    def imprimir_estadisticas(self):
        """
        Metodo en el que se imprimen las estadisiticas al final del sistema
        """
        print("\n------ ESTADISTICAS ------")
        print("Los ingresos totales son: {}".format(self.ingresos))
        print("Los costos de mantencion de inventario son: {}".format(self.costo_inventario))
        print("Los costos de ordenes de inventario son: {}".format(self.costo_ordenes))
        print("\n")
        print("Los beneficios totales para la empresa son: {}".format(self.ingresos - self.costo_inventario - self.costo_ordenes))

if __name__ == '__main__':
    s = Simulacion(10, 30)  # Cuando se tiene menos de 10 en inventario se piden 30

    # Se setea la cantidad de tiempo que se desea operar
    limite_tiempo = int(input("Ingrese cuanto tiempo desea simular: "))

    while s.tiempo_actual < limite_tiempo:
        # Se actualiza el tiempo en cada iteracion
        s.avanzar_el_tiempo()

    # Al terminar se imprimen las estadisticas
    s.imprimir_estadisticas()
