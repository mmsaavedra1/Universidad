n = int(input())
cota_superior = n
cota_inferior = 0

for i in range(10):
    print(cota_inferior, cota_superior)

    medio = (cota_inferior + cota_superior) / 2
    if (medio ** 2) < n:
        cota_inferior = medio

    elif (medio ** 2) > n:
        cota_superior = medio
    else:
        break

print(medio)