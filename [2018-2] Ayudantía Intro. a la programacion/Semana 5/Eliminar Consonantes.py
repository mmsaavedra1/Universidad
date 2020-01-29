palabra = input()
palabra_nueva = ""

for letra in palabra:
    if letra in "AEIOUaeiou ":
        palabra_nueva += letra

print(palabra_nueva)