altuve = float(input())

# Cuantos Shappy hay por Altuve

# x = 1/2.9 shappy/km
# y = 1000/1.55 altuve/km
constante = (1/2.9) * (1.55/1000)

shappy = constante * altuve

print(shappy)