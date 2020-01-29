import math


def media(d1, d2, d3, d4, d5):
    var_media = (d1 + d2 + d3 + d4 + d5) / 5

    return var_media


def des_estandar(d1, d2, d3, d4, d5):
    var_media = media(d1, d2, d3, d4, d5)
    suma = ((d1 - var_media) ** 2) + ((d2 - var_media) ** 2) + (
        (d3 - var_media) ** 2) + ((d4 - var_media) ** 2) + (
           (d5 - var_media) ** 2)
    var_desv = math.sqrt(suma / 5)

    return var_desv


def varianza(d1, d2, d3, d4, d5):
    var_desv = des_estandar(d1, d2, d3, d4, d5)
    var_varianza = var_desv ** 2

    return var_varianza


# Se recomienda no modificar el siguiente código
if __name__ == "__main__":
    [x1, x2, x3, x4, x5] = list(map(float, input().strip().split(' ')))
    result_med = media(x1, x2, x3, x4, x5)
    result_de = des_estandar(x1, x2, x3, x4, x5)
    result_var = varianza(x1, x2, x3, x4, x5)

    print(result_med, result_de, result_var)
