import numpy as np
from skimage import io
import scipy.ndimage
import matplotlib.pyplot as plt

############### COMENTARIOS ###############

    # El proyecto falla por la mala aproximacion conseguida en el
    # kernel ya que este obtiene valores tan pequeño que es detectado
    # y genera un determinante = 0, lo que impide invertir A para obtener
    # el R de cada iteracion


def imagen_a_vector(imagen):
    """ Funcion que recibe una imagen y devuelve un vector con los
    valores hexagecimales de la imagen asociadax"""

    # Lee los datos y los convierte en una matriz de pixeles de blanco y negro
    image = io.imread(imagen, as_grey=True)

    return image

def FISTA(A,b,tau,n_iteraciones):
    """Funcion que aplica el metodo FISTA para resolver el problema
    de LASSO planteado"""

    m, n = A.shape # A es un elemento array

    # Se definen los parametros por ocupar en el metodo de FISTA
    xk = np.zeros((n, 1))
    xk1 = np.zeros((n,1))
    xk2 = np.zeros((n,1))
    zig = 0
    thetak = 1
    zk = xk
    angle = 0

    # Se guardan los datos
    solarray = list()
    R = np.sqrt(np.linalg.norm(np.linalg.inv(np.matmul(A, A)))) * np.linalg.norm(b)
    L = tau*np.sqrt(n) + np.linalg.norm(np.matmul(A, A))*R + np.linalg.norm(np.matmul(A, b))
    optval = tau*np.linalg.norm(xk, 1) + 0.5*np.linalg.norm(np.matmul(A, xk) - b)**2
    nb = np.linalg.norm(b, float("inf"))

    print("TIEMPO  VALOR OPTIMO  NORMA 1  ERROR")
    for t in range(1, n_iteraciones):
        yk = (1-thetak)*xk + thetak*zk
        g = np.matmul(A, np.matmul(A, yk) - b)

        for j in range(1, n):
            x1 = zk[j] - (1/L*thetak)*(g[j]+tau)
            x2 = zk[j] - (1/L*thetak)*(g[j]-tau)
            x3 = 0
            val1 = np.array(g[j]*x1 + tau*np.abs(x1) + (L*thetak/2)*(x1-zk[j])*(x1-zk[j]))
            val2 = np.array(g[j]*x2 + tau*np.abs(x2) + (L*thetak/2)*(x2-zk[j])*(x2-zk[j]))
            val3 = np.array(g[j]*x3 + tau*np.abs(x3) + (L*thetak/2)*(x3-zk[j])*(x3-zk[j]))
            if val1 <= np.minimum(val2, val3):
                zk[j] = x1
            else:
                if val2 <= np.minimum(val1, val3):
                    zk[j] = x2
                else:
                    zk[j] = x3

        # Se actualiza el mundo para la siguiente iteracion
        xk2 = xk1
        xk1 = xk
        xk = (1-thetak)*xk + thetak*zk
        thetak = 2/(1+np.sqrt(1 + 4/(thetak**2)))
        aux = np.linalg.norm(np.matmul(A, xk) - b)

        # Se almacenan los valores buscados
        optval = tau*np.linalg.norm(xk,1) + 0.5*aux**2
        error_residual_relativo = np.linalg.norm(np.matmul(A, xk) - b, float("inf"))/nb
        solarray.append([t, optval, np.linalg.norm(xk, 1), error_residual_relativo])

        print("{0: ^7}{1: ^13} {2: ^8} %{3: ^5}".format(t, round(optval, 5), round(np.linalg.norm(xk,1), 5), round(error_residual_relativo), 3)*100)

    sol = xk
    return optval, sol, solarray

def filtro_gaussiano(size, sigma):
    """
    Funcion que genera una matriz para aplicar filtro
    gaussiano sobre una imagen obtenida de:

    https://stackoverflow.com/questions/17190649/how-to-obtain-a-gaussian-filter-in-python
    """
    x, y = np.mgrid[-size//2 + 1:size//2 + 1, -size//2 + 1:size//2 + 1]
    gauss = np.exp(-((x**2 + y**2)/(2*sigma**2)))/(2*np.pi*sigma**2)
    return gauss


if __name__ == '__main__':
    # Configuracion necesaria de pyplot para ver las imagenes en escala de grises
    plt.rcParams['image.cmap'] = 'gray'

    ########################################################################

    # Lectura de la imagen
    imagen = imagen_a_vector("Profe.jpeg")
    kernel = filtro_gaussiano(imagen.shape[0], 2)
    blurring = scipy.ndimage.convolve(imagen, kernel)

    # Se muestra la imagen de la matriz 0 -> negro/ 1 -> blanco
    b = scipy.ndimage.gaussian_filter(imagen, 0.89)


    # Se crea la matriz por analizar para Fista
    A = kernel

    # Vector que almacena todos los valores
    x = list()

    for i in range(A.shape[0]):
        valor_optimo, solucion, solarrya = FISTA(A, scipy.transpose(b)[i], 10**(-4), 100)
        x.append(solucion)

    # Se busca la inversa de Fourier para obtener la imagen
    x = scipy.transpose(np.array(x))

    plt.imshow(np.real(x))
    plt.show()
