numero = int(input())

# Se define la cantidad de cifras que tiene
contador = 10
cifras = 1

while numero // contador != 0:
    cifras += 1
    contador *= 10

# Cuando se tienen las cantidades de cifras se itera
invertido = 0
for i in range(1, cifras + 1):
    # Se busca el resto
    resto = numero % (10 ** i)
    # Se obtiene el resultado entero del resto con la cantidad de ceros asociados
    cifra = resto // (10 ** (i - 1))
    # Se suma al invertido el numero
    invertido += (cifra) * (10 ** (cifras - i))

print(invertido)