mensaje = input()
mensaje += " "

palabra = ""
mensaje_final = ""

for letra in mensaje:
    # Primer paso es armar cada palabra del mensaje
    if letra != " ":
        palabra += letra
    else:
        # Aqui se analiza la palabra que se armo


        # Controla que existan letras repetidas dentro de la palabra
        letra_repetida = ""

        for _letra in palabra:
            # Se analiza si la letra actual esta repetida mas veces
            # si lo es se define la nueva letra repetida
            if palabra.count(_letra) == 2 and (_letra not in letra_repetida):
                mensaje_final += _letra
                letra_repetida += _letra

        # Condicion de no pillar ninguna letra
        if letra_repetida == "":
            mensaje_final += palabra[-1]

        # Se vuelven a las condiciones iniciales
        palabra = ""
        letra_repetida = ""

print(mensaje_final)