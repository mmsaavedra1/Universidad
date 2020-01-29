import math


def jolly_jumper(s1, s2, s3, s4, s5):
    dif_1 = int(math.fabs(s1 - s2))
    dif_2 = int(math.fabs(s2 - s3))
    dif_3 = int(math.fabs(s3 - s4))
    dif_4 = int(math.fabs(s4 - s5))

    # Aux que define a priori si es Jolly, en caso de que un no cumpla deja automaticamente de ser jolly
    es_jolly = True

    # Se busca al menos un diferencia
    if math.fabs(dif_1 - dif_2) != 1:
        es_jolly = False

    elif math.fabs(dif_2 - dif_3) != 1:
        es_jolly = False

    elif math.fabs(dif_3 - dif_4) != 1:
        es_jolly = False

    # Ahora se retorna si son Jolly o no, e imprime los numero si lo es
    if es_jolly:
        print(dif_1, dif_2, dif_3, dif_4)

    return es_jolly


# Te sugerimos no modificar el siguiente código
if __name__ == "__main__":
    [x1, x2, x3, x4, x5] = list(map(int, input().strip().split(' ')))
    es_jolly = jolly_jumper(x1, x2, x3, x4, x5)
    print(es_jolly)