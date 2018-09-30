string = input()

lista_numeros = string.split(",")
lista_final = list()

for i in lista_numeros:

    es_primo = True

    for j in range(2, int(i)):
        if int(i) % j == 0:
            es_primo = False
            break

    if es_primo:
        lista_final.append(int(i) + 1)
    else:
        lista_final.append(int(i))

print(lista_final)