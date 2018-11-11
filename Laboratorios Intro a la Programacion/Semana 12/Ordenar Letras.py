def ordenar(lista):
    letras = "".join(sorted(list(lista[0])))

    if len(lista) == 1:
        return letras

    return letras + " " + ordenar(lista[1:])


entrada = input().split(" ")
print(ordenar(entrada))