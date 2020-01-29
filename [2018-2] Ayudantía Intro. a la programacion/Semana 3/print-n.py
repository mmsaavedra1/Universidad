# Numeros por recibir
n = int(input())

# Almacen de resultados
resultados = int(input())

while n != 0:
    nuevo_input = int(input())
    resultados += nuevo_input
    print(resultados)

    # Se setea la suma
    resultados = nuevo_input

    # Condicion de flujo
    n -= 1