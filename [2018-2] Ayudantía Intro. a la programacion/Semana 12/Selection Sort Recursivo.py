def sort(lista, nuevo):
    if len(lista) == 1:
        nuevo.insert(0, int(min(lista)))
        return nuevo

    nuevo.insert(0, int(min(lista)))
    indice = lista.index(min(lista))
    lista.pop(indice)
    print(nuevo)

    return sort(lista, nuevo)

entrada = input().split(" ")
aux = [int(min(entrada))]
indice = entrada.index(min(entrada))
entrada.pop(indice)

if len(entrada) > 0:
    print(sort(entrada, aux))
else:
    print(aux)
