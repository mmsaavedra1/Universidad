inicio = int(input())
final = int(input())

# Se imprime el texto pedido
print("Los numeros perfectos son:")

for numero in range(inicio, final + 1):
    # Se hace el tema de los divisores y la suma de estos
    suma = 0

    for divisor in range(1, numero):
        if numero % divisor == 0:
            suma += divisor

    if numero == suma:
        print(numero)