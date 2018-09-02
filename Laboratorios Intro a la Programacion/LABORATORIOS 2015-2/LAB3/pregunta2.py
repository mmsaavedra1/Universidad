n = int(input("Ingrese un numero: "))

def tobin(x):
    return tobin(x//2) + [x%2] if x > 1 else [x]

#print("".join(str(l) for l in tobin(n)))

#print("El numero " + str(n) + " en representacion binaria es " + str(bin(n)).strip("0b"))

print("El numero " + str(n) + " en representacion binaria es " + str("".join(str(l) for l in tobin(n))))