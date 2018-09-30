valores = input()
indices = input()

lista_valores = valores.split(" ")
lista_indices = indices.split(" ")

# Copia
lista_final = lista_valores.copy()

contador = 0

for valor in lista_valores:
    lista_final[int(lista_indices[contador])] = valor
    contador += 1

print(lista_final)