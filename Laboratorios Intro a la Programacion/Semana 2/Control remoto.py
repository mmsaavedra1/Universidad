canal_objetivo = int(input())
canal_actual = int(input())

# Se crean variables que digan cuantas veces se debe cambiar arriba o abajo
veces_arriba = 0
veces_abajo = 0

# Primero analizar arriba
if ((canal_objetivo - canal_actual) < 0) and (
        canal_actual <= 99 and canal_objetivo < 99):
    diferencia_arriba = 100 - canal_actual
    diferencia_arriba += canal_objetivo
else:
    diferencia_arriba = canal_objetivo - canal_actual

# Ahora analizar abajo
if (canal_actual - canal_objetivo < 0) and (
        canal_actual < 99 and canal_objetivo <= 99):
    diferencia_abajo = 100 - canal_objetivo
    diferencia_abajo += canal_actual
else:
    diferencia_abajo = canal_actual - canal_objetivo

if diferencia_abajo < diferencia_arriba:
    print(str(diferencia_abajo) + " veces abajo")
else:
    print(str(diferencia_arriba) + " veces arriba")
