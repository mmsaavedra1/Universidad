while True:
    notas = input()

    if notas == "end":
        break

    lista_notas = notas.split(";")

    I1 = float(lista_notas[0])
    I2 = float(lista_notas[1])
    E = float(lista_notas[2])
    T1 = float(lista_notas[3])
    T2 = float(lista_notas[4])
    T3 = float(lista_notas[5])
    P = float(lista_notas[6])

    nota_final = 0.15 * I1 + 0.15 * I2 + 0.3 * E + 0.1 * T1 + 0.1 * T2 + 0.1 * T3 + 0.1 * P

    if nota_final >= 3.95:
        print("APROBADO")
    else:
        print("REPROBADO")