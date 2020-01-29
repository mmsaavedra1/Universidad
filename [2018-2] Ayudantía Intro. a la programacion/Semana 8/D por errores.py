n = int(input())

for i in range(n):
    texto = input()

    _texto = ""
    for letra in texto:

        # Se cambian las letras
        if letra == "d":
            letra = "r"
        elif letra == "r":
            letra = "d"
        elif letra == "D":
            letra = "R"
        elif letra == "R":
            letra = "D"

        _texto += letra

    print(_texto)