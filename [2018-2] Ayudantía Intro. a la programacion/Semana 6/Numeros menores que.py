numeros = input()
n = int(input())

lista_de_numeros = numeros.split(" ")
lista_final = list()

for i in lista_de_numeros:
    if int(i) <= n:
        lista_final.append(int(i))

print(lista_final)
