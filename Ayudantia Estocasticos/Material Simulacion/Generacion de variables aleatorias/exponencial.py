import numpy as np
import matplotlib.pyplot as plt


def instancias_de_exponenciales(_lambda):
    """Funcion que genera variables aleatoias y returna su valor
    evaluado en la funcion inversa de la densidad"""
    u = np.random.uniform(0, 1)
    f_inversa = -np.log(1-u)/_lambda

    return f_inversa

# Ahora se crean las cantidades de instancias que se desean obtener
# junto con los parametros necesario: tasa lambda y vector donde almacenar
# la informacion

instancias_deseadas = 10000  # Mientas + grande el numero, mejor la aproximacion
tasa = 0.1  # Corresponde a la tasa pedida por la formula densidad
x = np.zeros(instancias_deseadas)  # Vector de numeros que se va actualizando por iteracion


# Ahora se ejecuta el programa
for i in range(instancias_deseadas):
    x[i] = instancias_de_exponenciales(tasa)
    

# Ahora se debe generar un histograma que refleje la frecuencia
# de cada dato que se necesita.

plt.hist(x, 50, facecolor="r", alpha=0.75)  # Se genera el objeto a graficar

plt.xlabel("Valores")  # Titulo eje x
plt.ylabel("Frecuencia")  # Titulo eje Y
plt.title("Histograma")  # Titulo del histograma
plt.axis([0,50,0,2000])  # Largo del eje x, largo del eje Y
plt.grid(True)  # Se setea la grilla
plt.show()  # Mostramos en pantalla el histograma

