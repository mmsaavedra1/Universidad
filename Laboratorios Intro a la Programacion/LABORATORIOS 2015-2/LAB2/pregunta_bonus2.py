a = int(input("Ingrese el valor numerico del coeficiente a: "))
b = int(input("Ingrese el valor numerico del coeficiente b: "))
c = int(input("Ingrese el valor numerico del coeficiente c: "))

if a == 0:
    print("Ecuacion no valida.")
    exit(0)

delta = (b ** 2) - (4 * a *c)

if delta >= 0:
    import math
    x1 = ((-1 * b) + math.sqrt(delta)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(delta)) / (2 * a)
    print("La primera raiz, x1, es: %.2f y la segunda raiz, x2, es: %.2f" % (x1, x2))
else:
    import cmath
    x1 = ((-1 * b) + cmath.sqrt(delta)) / (2 * a)
    x2 = ((-1 * b) - cmath.sqrt(delta)) / (2 * a)
    print("La primera raiz, x1, es: " + str(x1) + " y la segunda raiz, x2, es: " + str(x2))


