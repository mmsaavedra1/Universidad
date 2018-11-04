instrucciones = input().split(" ")
cartas = ["As", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]

for instruccion in instrucciones:

    centro = len(cartas) // 2
    if len(cartas) % 2 == 0:
        centro -= 1

    if instruccion == "mayor":
        cartas = cartas[centro + 1:]
    elif instruccion == "menor":
        cartas = cartas[:centro]
    else:
        print(cartas[centro])
        break