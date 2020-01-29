import numpy as np
import matplotlib.pyplot as plt


def _probabilidad(t, tasa, k):
    """Proceso de Poisson."""
    return np.exp(-1 * tasa * t) * ((tasa * t) ** k) / (np.math.factorial(k))


def cero_eventos():
    """Funcion que grafica P{N(t) = 0}"""

    # Ejes independientes
    tiempo = np.arange(0, 10, 0.1)

    # Eje dependiente
    probabilidad = list()
    for t in tiempo:
        probabilidad.append(_probabilidad(t, 1, 0))
    probabilidad = np.array(probabilidad)

    # Se instancia el grafico 2D
    plt.plot(tiempo, probabilidad)


    # Se setean las etiquetas y titulos del grafico
    plt.title("Gráfico P{N(t)=0} en función del tiempo.")
    plt.xlabel('Tiempo', alpha=2)
    plt.ylabel('Probabilidad', alpha=2)

    plt.show()


def un_evento():
    """Funcion que grafica P{N(t) = 1}"""

    # Ejes independientes
    tiempo = np.arange(0, 10, 0.1)

    # Eje dependiente
    probabilidad = list()
    for t in tiempo:
        probabilidad.append(_probabilidad(t, 1, 1))
    probabilidad = np.array(probabilidad)

    # Se instancia el grafico 2D
    plt.plot(tiempo, probabilidad)


    # Se setean las etiquetas y titulos del grafico
    plt.title("Gráfico P{N(t)=1} en función del tiempo.")
    plt.xlabel('Tiempo', alpha=2)
    plt.ylabel('Probabilidad', alpha=2)

    plt.show()

if __name__ == '__main__':
    cero_eventos()
    un_evento()


    