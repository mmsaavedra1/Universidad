from math import sqrt

def pertenencia(a, b, c, x, y):
    return a * x + b * y + c == 0

def funcion(a, b, c, x):
    try:
        y = -(a * x + c) / b
    except ZeroDivisionError:
        y = 0
    return y

def distRectaPunto(a, b, c, x, y):
    try:
        dist = abs(a*x + b*y + c)/sqrt(a**2 + b**2)
    except ZeroDivisionError:
        dist = -1
    return dist

def norma(x, y):
    return sqrt(x**2 + y**2)

def distPuntos(x1, y1, x2, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)