mensaje = input()
palabra = ""
mensaje_codificado = ""

for letra in mensaje:
    if letra != " ":
        palabra += letra

    else:
        # Aqui se invierte la palabra
        if len(palabra) % 2 == 0:
            palabra = palabra[::-1]

        # Aqui se agregan los espacios
        palabra += letra

        # Se actualiza el mensaje codificado
        mensaje_codificado += palabra

        # Se deja "palabra" para aceptar nuevas letras
        palabra = ""

# Queda una palabra fuera
if len(palabra) % 2 == 0:
    palabra = palabra[::-1]

# Se actualiza el mensaje codificado
mensaje_codificado += palabra

# Se deja "palabra" para aceptar nuevas letras
palabra = ""

print(mensaje_codificado)
