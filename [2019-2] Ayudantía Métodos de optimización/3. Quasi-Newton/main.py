__author__ = "Moises Saavedra Caceres"
__email__ = "mmsaavedra1@ing.puc.cl"


from quasi_newton import *
from newton import *


# Este comando genera los valores aleatorios para cada ejecucion
np.random.seed(1)

# Testeo de Newton, primero se generan datos para la funcion
n = 4
Q, c = generar_datos(n)

# Se ocupa el vector de "unos" como punto de inicio
# (notar el salto que pega) de la iteracion 1 a la 2 el valor objetivo
# -- Queda a tu eleccion que vector ingresar como solucion para la iteracion 1 --
x0 = np.ones((n, 1))

# Error asociado 10% este caso
epsilon = 0.1

# Maximo de iteraciones (para que no quede un loop infinito)
iteracion_maxima = 200

# Se ejecutan ambos codigos como muestra
quasinewton_BFGS(Q, c, x0, epsilon, iteracion_maxima)
newton(Q, c, x0, epsilon, iteracion_maxima)
