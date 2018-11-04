datos = input().split(";")

for numeros in datos:
    a, b, c = numeros.split(",")
    if (int(a)**2 + int(b)**2) == int(c)**2:
        print(int(a), int(b), int(c))