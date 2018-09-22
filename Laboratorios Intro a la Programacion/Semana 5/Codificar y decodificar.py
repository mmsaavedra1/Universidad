def decodificar(string):
    letra = ""
    numero = 1
    palabra = ""

    for caracter in string:
        if caracter.isalpha():

            # Guarda la letra que solo se multiplica por 1
            if letra != "":
                palabra += letra

            letra = caracter
            numero = 1
        else:
            numero = int(caracter)
            palabra += (letra * numero)

            letra = ""
            numero = 1

    if numero == 1:
        palabra += letra

    return palabra


def codificar(string):
    # Completa esta funcion
    string += " "

    contador = 0
    letra_pasada = string[0]
    palabra = ""

    for letra in string:
        if letra_pasada == letra:
            contador += 1

        else:
            palabra += letra_pasada
            palabra += str(contador)

            letra_pasada = letra
            contador = 1

    return palabra.replace("1", "")


string = input()
funcion = input()
if funcion == 'decodificar':
    print(decodificar(string))
else:
    print(codificar(string))