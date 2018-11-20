### Codigo ocupado y modificado del siguiente link:
### https://scikit-learn.org/stable/auto_examples/decomposition/plot_image_denoising.html#sphx-glr-auto-examples-decomposition-plot-image-denoising-py
### ARREGLOS SEGUN LA PARIDAD Y LA ALTARESOLUCION SE ELIMINO

from time import time

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp

from sklearn.decomposition import MiniBatchDictionaryLearning
from sklearn.feature_extraction.image import extract_patches_2d
from sklearn.feature_extraction.image import reconstruct_from_patches_2d
from skimage import io

# #############################################################################
# Se definen la funciones por ocupar en el proyecto


def imagen_a_vector(imagen, gris=True):
    """ Funcion que recibe una imagen y devuelve un vector con los
    valores hexagecimales de la imagen asociadax"""

    # Lee los datos y los convierte en una matriz de pixeles de blanco y negro
    image = io.imread(imagen, as_grey=gris)

    return image

def show_with_diff(image, reference, title):
    """Helper function to display denoising"""
    plt.figure(figsize=(5, 3.3))
    plt.subplot(1, 2, 1)
    plt.title('Imagen')
    plt.imshow(image, vmin=0, vmax=1, cmap=plt.cm.gray,
               interpolation='nearest')
    plt.xticks(())
    plt.yticks(())
    plt.subplot(1, 2, 2)
    difference = image - reference

    plt.title('Diferencia' % np.sqrt(np.sum(difference ** 2)))
    plt.imshow(difference, vmin=-0.5, vmax=0.5, cmap=plt.cm.PuOr,
               interpolation='nearest')
    plt.xticks(())
    plt.yticks(())
    plt.suptitle(title, size=16)
    plt.subplots_adjust(0.02, 0.02, 0.98, 0.79, 0.02, 0.2)


# #############################################################################
# Se carga la imagen y genera un ruido aleatorio sobre ella


plt.rcParams['image.cmap'] = 'gray'
imagen = imagen_a_vector("Profe.jpeg", gris=True)
alto, largo = imagen.shape

# Se aplica un ruido uniforme aleatorio a la imagen
print("Distrosionando imagen...")
imagen_distorsionada = imagen.copy()
if largo%2 == 0:
    imagen_distorsionada[:, largo // 2:] += 0.075 * np.random.randn(alto, largo // 2)
else:
    imagen_distorsionada[:, largo // 2 + 1:] += 0.075 * np.random.randn(alto, largo // 2)


# #############################################################################
# Extrae toda las referencia del patch del lado izquierdo

"""
Examples
    --------

    >>> from sklearn.feature_extraction import image
    >>> one_image = np.arange(16).reshape((4, 4))
    >>> one_image
    array([[ 0,  1,  2,  3],
           [ 4,  5,  6,  7],
           [ 8,  9, 10, 11],
           [12, 13, 14, 15]])
    >>> patches = image.extract_patches_2d(one_image, (2, 2))
    >>> print(patches.shape)
    (9, 2, 2)
    >>> patches[0]
    array([[0, 1],
           [4, 5]])
    >>> patches[1]
    array([[1, 2],
           [5, 6]])
    >>> patches[8]
    array([[10, 11],
           [14, 15]])
    """

print("Extrayendo patches de referencia...")
t0 = time()
patch_size = (7, 7) # A gusto del usuario
if largo%2 == 0:
    data = extract_patches_2d(imagen_distorsionada[:, :largo // 2], patch_size)
else:
    data = extract_patches_2d(imagen_distorsionada[:, :largo // 2+1], patch_size)

data = data.reshape(data.shape[0], -1)
data -= np.mean(data, axis=0)
data /= np.std(data, axis=0)
print('Hecho en %.2fs.' % (time() - t0))


# #############################################################################
# Learn the dictionary from reference patches

print('Dictionary Learning...')
t0 = time()
dico = MiniBatchDictionaryLearning(n_components=100, alpha=1, n_iter=500)
V = dico.fit(data).components_
dt = time() - t0
print('Hecho en %.2fs.' % dt)

# Se grafican los diccionarios obtenidos (patch_size**2 de dimension)
plt.figure(figsize=(4.2, 4))
for i, comp in enumerate(V[:100]):
    plt.subplot(10, 10, i + 1)
    plt.imshow(comp.reshape(patch_size), cmap=plt.cm.gray_r,
               interpolation='nearest')
    plt.xticks(())
    plt.yticks(())

plt.suptitle('Dictionary learned desde los patches de la imagen\n' +
             'Tiempo calculos %.1fs en %d patches' % (dt, len(data)),
             fontsize=16)
plt.subplots_adjust(0.08, 0.02, 0.92, 0.85, 0.08, 0.23)


# #############################################################################
# Muestra la imagen distorsionada (junto con la distorsion a un lado)


show_with_diff(imagen_distorsionada, imagen, 'Imagen y su respectivo ruido')


# #############################################################################
# Extrae el ruido y luego reconstruye ocuopando los diccionadios


print('Extrayendo los patches con ruido... ')
t0 = time()
if largo%2 == 0:
    data = extract_patches_2d(imagen_distorsionada[:, largo // 2:], patch_size)
else:
    data = extract_patches_2d(imagen_distorsionada[:, largo // 2+1:], patch_size)

data = data.reshape(data.shape[0], -1)
intercept = np.mean(data, axis=0)
data -= intercept
print('Hecho en %.2fs.' % (time() - t0))


# #############################################################################
# Reconstruye ocupando los diccionadios y diferentes metodos


algoritmos_transformacion = [
    ('Orthogonal Matching Pursuit\n1 atom', 'omp',
     {'transform_n_nonzero_coefs': 1}),
    ('Orthogonal Matching Pursuit\n2 atoms', 'omp',
     {'transform_n_nonzero_coefs': 2}),
    ('Least-angle regression\n5 atoms', 'lars',
     {'transform_n_nonzero_coefs': 5}),
    ('Thresholding\n alpha=0.1', 'threshold', {'transform_alpha': .1})]

reconstructions = {}
for titulo, algoritmo, kwargs in algoritmos_transformacion:
    print(titulo + '...')
    reconstructions[titulo] = imagen.copy()
    t0 = time()
    dico.set_params(transform_algorithm=algoritmo, **kwargs)
    code = dico.transform(data)
    patches = np.dot(code, V)

    patches += intercept
    patches = patches.reshape(len(data), *patch_size)

    if algoritmo == 'threshold':
        patches -= patches.min()
        patches /= patches.max()

    if largo%2 == 0:
        reconstructions[titulo][:, largo // 2:] = reconstruct_from_patches_2d(patches, (alto, largo // 2))
    else:
        reconstructions[titulo][:, largo // 2 + 1:] = reconstruct_from_patches_2d(patches, (alto, largo // 2))

    dt = time() - t0
    print("Hecho en %.2fs." % dt)
    show_with_diff(reconstructions[titulo], imagen, titulo + " (Tiempo: %.1fs)" % dt)


plt.show()