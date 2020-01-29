from gurobipy import *
import numpy as np
from time import time


# Creacion de parametros para el problema
inicio = time()
m = 40
n = 22
M = range(m)
N = range(n)

np.random.seed(0)
a = np.random.randint(5,20,(m,n))
c = np.random.randint(0,10,(m,n))
b = np.random.randint(15,20,(n))

# Se setea que opcion de resolucion ocupar
opcion = int(input("Ingresa 0 para no ocupar Relajacion Lagrangeana, \ncualquier otra tecla para usarla: "))
if opcion == 0:
    no_lagrange = True
else:
    no_lagrange = False


###################
#  Modelo normal  #
###################
if no_lagrange:
    # Creacion del modelo
    modelo = Model("Modelo Normal")

    # Creacion de variables
    x = modelo.addVars(M, N, vtype=GRB.BINARY)

    # Creacion de restricciones
    R1 = modelo.addConstrs(
        (quicksum(x[i, j] for j in N) == 1) for i in M
    )

    R2 = modelo.addConstrs(
        (quicksum(a[i,j]*x[i,j] for i in M) >= b[j]) for j in N
    )

    # Se crea la funcion objetivo
    modelo.setObjective(
        quicksum(c[i,j]*x[i,j] for i in M for j in N), GRB.MINIMIZE
    )

    # Se actualizan los valores en el modelo y optimiza
    modelo.update()
    modelo.optimize()

    print("\nValor óptimo:", modelo.objVal)
    print("Tiempo de ejecucion [s]:", time()-inicio)


###########################
#  Relajacion Lagrangeana #
###########################
else:
    # Se crea el modelo de relajacion lagrangeana
    lagrangeano = Model("Relajacion Lagrangeana")
    lagrangeano.Params.OutputFlag = 0

    # Se crean las variables asociadas
    x = lagrangeano.addVars(M, N, vtype=GRB.BINARY)
    u = [2.0]*m

    # Se agregan las restrcciones no relajadas
    R1 = lagrangeano.addConstrs(
        (quicksum(a[i,j]* x[i,j] for i in M) >= b[j]) for j in N
    )

    # Vector direccion de descenso
    h = [0.0] * m

    for iteracion in range(1, 100):
        # Se crea la funcion objetivo
        lagrangeano.setObjective(
            quicksum(quicksum(c[i,j]*x[i,j] for i in M) for j in N)
            + quicksum(quicksum(u[j]*x[i,j] for i in M) for j in N)
            - quicksum(u[i] for i in M),
            GRB.MINIMIZE
        )

        # Se actualiza y optimiza
        lagrangeano.update()
        lagrangeano.optimize()

        print("Iteracion: ", iteracion)
        print("Valor óptimo:", lagrangeano.objVal)
        print("\n")

        # Aqui se realiza el paso de la variable dual
        # 1º Se crea el vector de descenso que pertenezca al subgradiente
        for i in M:
            h[i] = quicksum(x[i,j] for j in N).getValue() - 1

        # 2º Se analiza si cumple el criterio de parada
        stop = True
        error = 10e-6
        for i in M:
            if abs(u[i]) > error and abs(h[i]) > error:
                stop = False
                break

        if stop:
            print("*** ¡Termina por convergencia! ***")
            break

        # 3º Si no se termina por convergencia se crea el paso a la sgte iteracion
        else:
            rho = 1.0/iteracion
            for i in M:
                u[i] = min(0.0, u[i] + rho*h[i])


    print("\nValor óptimo:", lagrangeano.objVal)
    print("Tiempo de ejecucion [s]:", time()-inicio)

