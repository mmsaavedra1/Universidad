# Recibimiento del input y su transformacion a lista.
s = input()
lista = []
while True:
    coma = s.find(',')
    if coma == -1:
        lista.append(int(s))
        break
    else:
        lista.append(int(s[:coma]))
        s = s[coma + 1:]

# Empieza tu código acá
pascal = list()

# Se setea el valor inicial
pascal.append(lista[0])

# Se suman los de al medio
largo_lista = len(lista)
for i in range(largo_lista - 1):
    pascal.append(lista[i] + lista[i + 1])

# Se setea el valor final
pascal.append(lista[-1])

print(pascal)