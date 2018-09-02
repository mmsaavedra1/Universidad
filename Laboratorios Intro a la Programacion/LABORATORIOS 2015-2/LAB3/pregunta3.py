import random as r

saldo = 1000

while True:
    perdida = False

    apuesta = int(input("Tu saldo es "+ str(saldo) +". Cuanto deseas apostar?: "))

    while apuesta < 1 or apuesta > 100:
        apuesta = int(input("Tu saldo es 1000. Cuanto deseas apostar?: "))

    saldo -= apuesta

    numero = r.randint(2, 21)

    print("Tu apuesta es: " + str(apuesta) + ". Tu numero es: " + str(numero))

    otro_n = input("Deseas aumentar el numero? (si / no): ") == "si"

    while otro_n and not perdida:
        otro_numero = r.randint(1, 10)
        numero += otro_numero

        if otro_numero + numero > 21:
            perdida = True
            break

        if otro_n: print("Tu aumento es de " + str(otro_numero) + ". Tu nuevo numero es: " + str(numero) + ".")
        otro_n = input("Deseas aumentar el numero? (si / no): ") == "si"

        if numero > 21:
            perdida = True

    if numero > 21:
        print("Tu numero (" + str(numero) + ") es mayor que 21. Has perdido")
        continue

    print("Tu numero es: " + str(numero) + ".")

    numero_pc = r.randint(2, 21)

    print("El computador tiene el numero " + str(numero_pc) + ".")

    perdida_pc = False

    while not perdida_pc:
        otro_numero_pc = r.randint(1, 10)
        if otro_numero_pc + numero_pc > 21:
            perdida_pc = True
            break
        numero_pc += otro_numero_pc
        print("El computador aumenta el numero en " + str(otro_numero_pc) + ". Ahora tiene el " + str(numero_pc) + ".")
        perdida_pc = numero_pc > 16

    print("El computador no puede aumentar mas. Su numero es: " + str(numero_pc) + ".")

    if numero_pc > 21:
        saldo += apuesta * 2
        print("Gana usuario. Su nuevo saldo es " + str(saldo))

    if numero > numero_pc:
        saldo += apuesta * 2
        print("Gana usuario (" + str(numero) + ">" + str(numero_pc) + "). Su nuevo saldo es " + str(saldo))

    if numero < numero_pc:
        print("Gana pc (" + str(numero) + "<" + str(numero_pc) + "). Su nuevo saldo es " + str(saldo))

    if saldo <= 0:
        print("Te has quedado sin dinero!")
        break

    repetir = input("Deseas continuar jugando? (si / no): ") == "no"

    if repetir:
        print("Gracias por jugar!!!")
        break