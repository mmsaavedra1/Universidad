
from gurobipy import *
import numpy
import time

# Se setea que opcion de resolucion ocupar
opcion = int(input("Ingresa 0 para no ocupar Benders, \ncualquier otra tecla para usar Benders: "))
if opcion == 0:
    no_benders = True
else:
    no_benders = False


######################################
#   Invencion de parametros base     #
######################################

numpy.random.seed(1)

# Numero de depositos
n = 500
N = range(n)

# Parametros
q = numpy.random.randint(10, 50, (n,n))
c = numpy.random.randint(5,40, (n,n))
s = numpy.random.randint(500, 1000, n)
d = numpy.random.randint(500, 2000, (n,n))

########################################
#  Opimiza deterministico equivalente  #
# (modelo resuleto sin ocupar BENDERS) #
########################################
if no_benders:
    deterministico = Model()
    deterministico.Params.Threads = 1

    # Generacion de variables
    x = deterministico.addVars(N, N, vtype=GRB.CONTINUOUS, lb=0)
    y = deterministico.addVars(N, N, vtype=GRB.CONTINUOUS, lb=0)

    # Generacion de restricciones
    R1 = deterministico.addConstrs(
        (quicksum(x[ii, jj] for jj in N if jj!=ii) <= s[ii]) for ii in N
    )

    R2 = deterministico.addConstrs(
        (quicksum(y[ii, jj] for jj in N if jj!=ii) <= s[ii] + quicksum(x[ll, ii] for ll in N if ll!=ii) - quicksum(x[ii, ll] for ll in N if ll!=ii)) for ii in N
    )

    R3 = deterministico.addConstrs(
        (y[ii, jj] <= d[ii][jj]) for ii in N for jj in N if jj!=ii
    )

    # Generacion de funcion objetivo
    deterministico.setObjective(
        quicksum(quicksum(q[ii][jj]*y[ii,jj] - c[ii][jj]*x[ii,jj] for jj in N if jj!=ii) for ii in N),
        GRB.MAXIMIZE
    )

    # Optimiza el equivalente
    inicio = time.time()
    deterministico.update()
    deterministico.optimize()
    final = time.time()

    print("Valor objetivo - Tiempo de resolucion ")
    print(deterministico.objVal, "   -   ", deterministico.Runtime)

else:
    ########################################
    #   Inicia  Descomposicion Benders
    #########################################

    # Define problema maestro
    maestro = Model()
    maestro.Params.OutputFlag = 0

    # Generacion de variables
    xm = maestro.addVars(N, N, vtype=GRB.CONTINUOUS, lb=0)
    theta = maestro.addVar(vtype=GRB.CONTINUOUS)

    # Generacion de restricciones
    R1m = maestro.addConstrs(
        (quicksum(xm[i,j] for j in N if j!=i) <= s[i]) for i in N
    )

    # Generacion de funcion objetivo
    maestro.setObjective(
        theta + quicksum(quicksum(c[i,j]*xm[i,j] for j in N if j!=i) for i in N),
        GRB.MINIMIZE
    )


    # *********************************************************************************

    ##### Definicion de subproblema ####
    subproblema = Model()
    subproblema.Params.OutputFlag = 0

    # Generacion de variables
    ysub = subproblema.addVars(N, N, vtype=GRB.CONTINUOUS, lb=0)

    # Generacion de restricciones
    R1sub = subproblema.addConstrs(
        (quicksum(ysub[i,j] for j in N if j!=i) <= 0) for i in N
    )

    R2sub = subproblema.addConstrs(
        (ysub[i,j] <= d[i,j]) for i in N for j in N
    )

    # Genera funcion objetivo
    subproblema.setObjective(
        quicksum(quicksum(q[i,j]*ysub[i,j] for j in N if j!=i) for i in N),
        GRB.MAXIMIZE
    )

    subproblema.update()

    ##################################
    #         Ciclo Benders          #
    ##################################

    print("")
    print("---------- CICLOS BENDERS-------------")
    print("")
    print("Ciclo - Master - Subproblema")
    inicio = time.time()
    contador = 0

    # Se inician las iteracion controladas
    while contador <= 10:
        contador += 1

        # Resuelve el modelo maestro
        maestro.update()
        maestro.optimize()

        # Se crean las variables duales para cada iteracion asociada
        pi_R1 = numpy.zeros((n))
        pi_R2 = numpy.zeros((n, n))

        # Actualizacion de restricciones segun lo calculado en el maestro
        for i in N:
            R1sub[i].RHS = s[i] + quicksum(xm[l,i] for l in N if l!=i).getValue() - quicksum(xm[i,n] for n in N if n!=i).getValue()

        # Optimizacion del subproblema
        subproblema.update()
        subproblema.optimize()


        # Acumula el valor en la FO
        FO = subproblema.objVal
        print(contador, "/", maestro.objVal, "/", subproblema.objVal)

        # Condicion de quiebre de BENDERS

        if 0.001 >= abs(1-(FO)/(FO + 0.1)):
            print("**** Termino por convergencia ****")
            break

        # Se cargan las variables duales
        for i in N:
            pi_R1[i] = R1sub[i].Pi
        for i in N:
            for j in N:
                pi_R2[i,j] = R2sub[i,j].Pi

        # Si es infactible agrega cortes de factibilidad
        if subproblema.status == 4:
            maestro.addConstr(
                quicksum(s[i] * pi_R1[i] for i in N)
                +quicksum(quicksum(xm[l,i] * pi_R1[i] for l in N if i!=l)for i in N)
                -quicksum(quicksum(xm[i,n] * pi_R1[i] for n in N if i!=n)for i in N)
                +quicksum(quicksum(d[i,j] * pi_R2[i,j] for j in N if j!=i)for i in N) <= 0
            )
        # Si es factible agrega corte de optimalidad
        else:
            maestro.addConstr(
                quicksum(s[i] * pi_R1[i] for i in N)
                + quicksum(quicksum(xm[l, i] * pi_R1[i] for l in N if i != l) for i in N)
                - quicksum(quicksum(xm[i, n] * pi_R1[i] for n in N if i != n) for i in N)
                + quicksum(quicksum(d[i, j] * pi_R2[i, j] for j in N if i != j) for i in N) <= theta
            )


    final = time.time()
    print("")
    print(" Tiempo de ejecucion:", (final - inicio))
