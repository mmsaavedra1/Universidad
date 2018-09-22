palabra = input()
n = int(input())

sub_palabra = ""

palabra_final = ""

for letra in palabra:
    if letra != " " and letra != ".":
        sub_palabra += letra

    else:
        if len(sub_palabra) >= n:
            sub_palabra = sub_palabra[n:]

        palabra_final += sub_palabra
        palabra_final += " "

        sub_palabra = ""

# Se arregla la parte final del punto
palabra_final = palabra_final[:-1]
palabra_final += "."
print(palabra_final)