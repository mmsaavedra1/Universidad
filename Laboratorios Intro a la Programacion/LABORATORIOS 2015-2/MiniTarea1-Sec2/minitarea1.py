import statistics
from functools import reduce
import math

a = input("Ingrese tres numeros enteros: \n")
b = input()
c = input()

print("\nCalculando...\n")

# lambda function with map to convert string to int
# abc = list(map(lambda x:int(x), [a, b, c]))
# prefer list comprehension as so:
abc = [int(x) for x in [a, b, c]]
abc.sort()

# recursive function found on:
# https://en.wikipedia.org/wiki/Euclidean_algorithm#Implementations
gcd = lambda a,b: a if b is 0 else gcd(b, a % b)
lcm = lambda a,b: a * b // gcd(a, b)

print("1- El numero minimo es: " + str(min(abc)))
print("2- El numero maximo es: " + str(max(abc)))
print("3- Su promedio es: %.2f" % (sum(abc) / len(abc)))
print("4- El maximo comun divisor es: " + str(reduce(gcd, abc)))
print("5- El minimo comun multiplo es: " + str(reduce(lcm, abc)))
print("6- El conjunto de numeros " + ("si" if (min(abc)**2) + (abc[abc.index(min(abc)) + 1]**2) is (max(abc)**2) else "no") + " es una terna pitagorica")
print("7- La desviacion estandar poblacional es: %.2f" % (statistics.pstdev(abc)))
print("8- La varianza poblacional es: %.2f" % (statistics.pvariance(abc)))
print("9- La razon entre el a y b es: %.2f" % (abc[0]/abc[1]) + ", entre b y c es: %.2f" % (abc[1]/abc[2]) + " y entre a y c es: %.2f" % (abc[0]/abc[2]))
heron = (math.sqrt((sum(abc)/2) * ((sum(abc)/2)-abc[0]) * ((sum(abc)/2)-abc[1]) * ((sum(abc)/2)-abc[2]))) if (min(abc) + abc[abc.index(min(abc)) + 1] >= max(abc)) else False
print("10- El triangulo formado por los 3 numeros" + ((" tiene area: %.2f" % heron) if heron is not False else " forma un triangulo imposible"))
