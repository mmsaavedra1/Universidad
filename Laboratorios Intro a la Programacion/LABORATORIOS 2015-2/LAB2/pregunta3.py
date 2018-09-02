a = int(input("Ingrese el valor numerico del coeficiente a: "))
b = int(input("Ingrese el valor numerico del coeficiente b: "))
c = int(input("Ingrese el valor numerico del coeficiente c: "))

delta = (b ** 2) - (4 * a *c)

if a == 0:
    print("Los coeficientes no corresponden a una ecuacion cuadratica (a = 0).")
elif delta > 0:
    print("Los valores ingresados corresponden a una ecuacion cuadratica cuyas soluciones son numeros reales y distintas.")
elif delta == 0:
    print("Los valores ingresados corresponden a una ecuacion cuadratica con una solucion de numero real.")
elif delta < 0:
    print("Los valores ingresados corresponden a una ecuacion cuadratica con con dos soluciones de numeros complejos.")
