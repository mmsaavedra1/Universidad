def mezcla(palabra1, palabra2):
    if len(palabra1)==1 and len(palabra2)==1:
        return palabra1 + palabra2
    return palabra1[0] + palabra2[0] + mezcla(palabra1[1:], palabra2[1:])

entrada1 = input()
entrada2 = input()

print(mezcla(entrada1, entrada2))
