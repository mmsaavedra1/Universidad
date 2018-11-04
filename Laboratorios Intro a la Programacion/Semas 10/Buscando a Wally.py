lista = input().split(" ")

while True:
    cota_superior = len(lista)
    centro = cota_superior // 2

    if cota_superior % 2 == 0:
        centro -= 1

    if lista[centro] == "U":
        print("U")
        lista = lista[centro + 1:]

    elif lista[centro] == "D":
        print("D")
        lista = lista[:centro]
    else:
        print("W")
        brea