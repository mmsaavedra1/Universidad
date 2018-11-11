def binario(n, numero):
    if n == 0:
        return (2**0) * int(numero[0])
    return (2**n) * int(numero[0]) + binario(n-1, numero[1:])

entrada = input()
print(binario(len(entrada)-1, entrada))
