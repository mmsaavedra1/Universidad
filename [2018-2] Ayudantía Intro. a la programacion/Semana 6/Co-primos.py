numeros = input()
lista_numeros_1 = numeros.split(" ")
lista_numeros = list()

# Se busca el numero mas grande, se convierten todos los str de la lista a int
for i in lista_numeros_1:
    lista_numeros.append(int(i))
numero_maximo = max(lista_numeros)

coprimo = 1

for i in range(1, numero_maximo + 1):
    coprimo_nuevo = True

    for j in lista_numeros:
        if int(j) % i != 0:
            coprimo_nuevo = False
            break

    if coprimo_nuevo:
        coprimo = i

if coprimo == 1:
    print("Coprimo")
else:
    print("No es coprimo. MCD:", coprimo)
