from math import sqrt

def determineRoots(a, b, c):
    delta = b**2 - 4*a*c
    roots = "Dos reales" if delta > 0 else ("Un real" if delta == 0 else "Dos complejos")
    return roots, delta

def calculateRoots(a, b, c):
    ret, delta = determineRoots(a, b, c)
    try:
        x1 = (-b + sqrt(delta)) / (2 * a)
        x2 = (-b - sqrt(delta)) / (2 * a)
    except ValueError:
        x1 = x2 = None

    return x1, x2

def minFunc(a, b, c, tol=0.01):
    x1 = x2 = x = 0
    while True:
        x1 = a*x**2+b*x+c
        x += tol
        x2 = a*x**2+b*x+c
        if x1 < x2:
            return x - tol

a = int(input("A: "))
b = int(input("B: "))
c = int(input("C: "))
eps = float(input("Epsilon: "))

print(determineRoots(a, b, c))
print(calculateRoots(a, b, c))
print(minFunc(a, b, c, eps))