import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def _probabilidad(t, tasa, k):
    """Proceso de Poisson."""
    return np.exp(-1 * tasa * t) * ((tasa * t) ** k) / (np.math.factorial(k))


def cero_eventos():
    """Funcion que grafica P{N(t) = 0}"""

    # Ejes independientes
    tiempo = np.arange(0, 10, 0.1)
    eventos = np.zeros((1, 100))[0]

    # Eje dependiente
    probabilidad = list()
    for t in tiempo:
        for k in eventos:
            probabilidad.append(_probabilidad(t, 1, k))
            break
    probabilidad = np.array(probabilidad)

    # Se instancia el grafico tridimensional
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_wireframe(tiempo, eventos, probabilidad, linewidth=3)

    # Se setean las etiquetas y titulos del grafico
    ax.set_title("Gráfico P{N(t)=0} en función del tiempo.")
    ax.set_xlabel('Tiempo', alpha=2)
    ax.set_ylabel('Eventos', alpha=2)
    ax.set_zlabel('Probabilidad', alpha=2, size=1)

    plt.show()


def un_evento():
    """ Funcion que grafica P{N(t) = 1}"""

    # Ejes independientes
    tiempo = np.arange(0, 10, 0.1)
    eventos = np.ones((1, 100))[0]

    # Eje dependiente
    probabilidad = list()
    for t in tiempo:
        for k in eventos:
            probabilidad.append(_probabilidad(t, 1, k))
            break

    probabilidad = np.array(probabilidad)

    # Se instancia el grafico tridimensional
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot_wireframe(tiempo, eventos, probabilidad, linewidth=3)

    # Se setean las etiquetas y titulos del grafico
    ax.set_title("Gráfico P{N(t)=1} en función del tiempo.")
    ax.set_xlabel('Tiempo', alpha=2)
    ax.set_ylabel('Eventos', alpha=2)
    ax.set_zlabel('Probabilidad', alpha=2)
    plt.show()

if __name__ == '__main__':

    # Se ejecuta cada funcion por analizar.
    cero_eventos()
    un_evento()
