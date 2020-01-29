def b_veces_c(b, c):
    return b * c


def modulo_entre_numeros(numero, funcion_anterior):
    return numero % funcion_anterior


input_1 = int(input())
input_2 = int(input())
input_3 = int(input())

# Llamado a la primera funcion
resultado_funcion_1 = b_veces_c(input_2, input_3)

# Llamado a la segundo funcion
resultado_funcion_2 = modulo_entre_numeros(input_1, resultado_funcion_1)

print(resultado_funcion_2)