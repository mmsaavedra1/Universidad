import numpy as np


class Simulacion:
    def __init__(self):
        # Contador de tiempo en el sistema
        self. individuos_en_sistema = 0

        # Tiempos
        self.reloj = 0.0
        self.tiempo_llegada = self.generar_llegada_interna() # Alguien llega al sistema.
        self.tiempo_salida = float("inf") # Alguien abandona el sistema, porque fue atendido.

        # Estadisticas
        self.numero_llegadas = 0
        self.numero_salidas = 0
        self.tiempo_total_espera = 0

    def avanzar_en_el_tiempo(self):
        """
        Funcion que actualiza los tiempos de ocurrencia de los proximos eventos
        """

        # Variable que define el tiempo del proximo evento:
        #   - Tiempo de llegada
        #   - TIempo de salida

        tiempo_proximo_evento = min(self.tiempo_llegada, self.tiempo_salida)

        # Suma la espera de cada usuario
        self.tiempo_total_espera += self.individuos_en_sistema * (tiempo_proximo_evento - self.reloj)

        # Actualiza el reloj actual como el nuevo evento
        self.reloj = tiempo_proximo_evento

        #
        if self.tiempo_llegada <= self.tiempo_salida:
            self.manejo_evento_llegada()
        else:
            self.manejo_evento_salida()


    def manejo_evento_llegada(self):
        """
        Actualizacion del mundo segun la llegada de un individuo que esta en
        cola esperando su atencion.
        """

        print("\t[EVENTO] Llegada individuo")

        self.individuos_en_sistema += 1
        self.numero_llegadas += 1

        # Si el individuo es el unico en cola, es obvio que pasa altiro a la
        # atencion y este sale del sistema segun la atencion del servidor.
        if self.individuos_en_sistema <= 1:
            self.tiempo_salida = self.reloj + self.generar_servicio()

        # Actualiza el proximo tiempo de llegada
        self.tiempo_llegada = self.reloj + self.generar_llegada_interna()


    def manejo_evento_salida(self):
        """
        Actualizacion del mundo segun la salida de un individuo que en
        la caja recibiendo servicio.
        """

        print("\t[EVENTO] Salida individuo")

        self.individuos_en_sistema -= 1
        self.numero_salidas += 1

        # Si hay individuos en el sistema (en cola esperando) se tiene que
        # conocer un tiempo de salida en base a la atencion del servidor
        if self.individuos_en_sistema > 0:
            self.tiempo_salida = self.reloj + self.generar_servicio()

        # ¿por que ocurre esto?
        else:
            self.tiempo_salida = float("inf")



    def generar_llegada_interna(self):
        """
        Funcion que genera tiempos de  llegadas al
        sistema segun una tasa exponencial.

        :return: Tiempo llegada.
        """

        return round(np.random.exponential(1/3)*10, 2)

    def generar_servicio(self):
        """
        Funcion que genera tiempos de atencion de cada servidor.

        :return: Tiempo servicio.
        """

        return round(np.random.exponential(1/4)*10, 2)


s = Simulacion()



# Estadisticas
print("----- E S T A D I S T I C A S -----\n")
# Se corre la simulacion
for i in range(1, 101):
    print("Iteracion: {} - Tiempo actual: {}".format(i, s.reloj))
    s.avanzar_en_el_tiempo()
    print("\tIndividuos que llegaron al sistema: {}".format(s.numero_llegadas))
    print("\tIndividuos que fueron atendidos en el sistema: {}\n".format(s.numero_salidas))


print("Tiempo promedio de espera: {}".format(round(s.tiempo_total_espera/s.numero_llegadas), 2))