import random as r

saldo = 1000



while True:
    apuesta = int(input("Tu saldo es "+ str(saldo) +". Cuanto deseas apostar?: "))

    while apuesta < 1 or apuesta > 100:
        apuesta = int(input("Tu saldo es " + str(saldo) + ". Cuanto deseas apostar?: "))

    saldo -= apuesta

    numero = r.randint(2, 21)

    print("Tu apuesta es: " + str(apuesta) + ". Tu numero es: " + str(numero))










    repetir = input("Deseas continuar jugando? (si / no): ") == "no"

    if repetir:
        print("Gracias por jugar!!!")
        break