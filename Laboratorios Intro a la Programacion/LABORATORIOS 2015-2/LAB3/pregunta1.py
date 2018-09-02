import random as r

dados = [0, 0]
done = False
counter = 0

while not done:
    dados = [r.randint(1, 6) for i in dados]
    done = (sum(dados) == 7) or (dados[0] == 6 and dados[1] == 6) or (dados[0] == 6 and dados[1] % 2 != 0) or (dados[1] == 6 and dados[0] % 2 != 0)
    counter += 1

print(counter)