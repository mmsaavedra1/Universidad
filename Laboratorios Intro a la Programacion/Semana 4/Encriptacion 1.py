# Enter your code here. Read input from STDIN. Print output to STDOUT
numero = int(input())


def cod_digitos(arg_numero):
    # Numero codificado
    numero_codificado = 0

    # Se define la cantidad de cifras que tiene
    contador = 10
    cifras = 1
    while arg_numero // contador != 0:
        cifras += 1
        contador *= 10

    n = cifras  # ¡Si se quiere ocupar informacion que se itera se almacena en var auxiliares!

    # Se recorre el numero
    for i in range(1, cifras + 1):
        # Se obtiene el resultado entero del resto con la cantidad de ceros asociados
        cifra = arg_numero // (10 ** (n - i))

        # Se ejecuta la operacion de cifrado
        resultado = n * cifra

        # Se define la cantidad de cifras que tiene
        contador = 10
        cifras_final = 1
        while resultado // contador != 0:
            cifras_final += 1
            contador *= 10

        # Se obtiene el primer numero
        final = resultado // (10 ** (cifras_final - 1))

        numero_codificado += (final) * (10 ** (n - i))

        # Se actualiza el numero
        arg_numero = arg_numero % (10 ** (n - i))

    return int(numero_codificado)


def cod_impares(arg_numero):
    # Numero codificado
    numero_codificado = 0

    # Se define la cantidad de cifras que tiene
    contador = 10
    cifras = 1
    while arg_numero // contador != 0:
        cifras += 1
        contador *= 10

    n = cifras  # ¡Si se quiere ocupar informacion que se itera se almacena en var auxiliares!

    for i in range(1, cifras + 1):
        # Se divide parte entera
        cifra = arg_numero // (10 ** (n - i))
        # Se ejecuta la operacion de cifrado
        resultado = n * cifra

        # Condiciones de filtro
        if (n - i + 1) % 2 == 0:
            final = (cifra - 1) % 10
        else:
            final = (cifra + 1) % 10

        # Se actualiza el numero
        arg_numero = arg_numero % (10 ** (n - i))

        # Finalmetne se suma al numero codificado
        numero_codificado += (final) * (10 ** (n - i))

    return numero_codificado * cifras


numero_cod = cod_digitos(numero)
numero_cod_2 = cod_impares(numero_cod)

print(numero_cod)
print(numero_cod_2)