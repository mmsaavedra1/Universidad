n = int(input())
numeros = input()

# Operaciones de lista
lista = numeros.split(" ")
lista.sort()

for i in range(n):
    print(int(lista[i]))