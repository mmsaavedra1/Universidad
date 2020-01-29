mensaje = input()
sub_string = input()

mensaje += "."

numero_actual = 0
numero_total = 0

string = ""

for letra in mensaje:

    if (letra not in ";.,"):
        string += letra

    # Si no corresponde a un signo de puntuacion se agrega al string por analizar
    else:

        string += letra

        # Se borra el primer espacio y la puntuacion final
        if string[0] == " ":
            string = string.lstrip()

        if string[-1] in ";.,":
            string = string.rstrip(string[-1])

        # Se analiza el string asociado
        palabra = ""
        ocupadas = ""

        # Comodin de seguridad
        string += " "

        for _letra in string:

            palabra += _letra

            if _letra == " " or (_letra in ";.,"):

                # Se analiza si substring esta en la palabra
                if (sub_string in palabra) and (palabra not in ocupadas):
                    numero_actual += 1
                    ocupadas += palabra + " "

                # Se actualiza el mundo
                palabra = ""

        # Si hay al menos un substring se imprime
        if numero_actual != 0:
            string = string.rstrip()
            print(string + ":", numero_actual)

        # Se actualiza el total
        numero_total += numero_actual

        # Se actualiza el mundo
        numero_actual = 0
        palabra = ""
        string = ""

print("Total:", numero_total)