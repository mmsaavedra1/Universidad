n = int(input())

# Se setean contadores
contador = 2
primos_encontrados = 0

# Se analizan hasta el n-esimo numero
while primos_encontrados < n:
    divisor = 2

    # Se asume a priori que el numero es primo, en caso de no serlo se cambia la condicion y
    # no se ejecuta la secuencia logica asociada
    es_primo = True

    # Se analiza si el numero n tiene mas divisores aparte de 1 y si mismo
    while divisor < contador:
        if contador % divisor == 0:
            # Se dice que ya no es primo
            es_primo = False
            # Se corta el ciclo
            break

        # Se pasa al siguiente divisor
        divisor += 1

    # Si es primo se imprime y se suma a los primos encontrados
    if es_primo == True:
        print(contador)
        primos_encontrados += 1

    contador += 1
