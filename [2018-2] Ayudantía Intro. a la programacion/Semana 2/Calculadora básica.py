numero_1 = float(input())
numero_2 = float(input())
operacion = input()

if operacion == "Sumar":
    resultado = numero_1 + numero_2

elif operacion == "Restar":
    resultado = numero_1 - numero_2

elif operacion == "Multiplicar":
    resultado = numero_1 * numero_2

else:
    resultado = numero_1 / numero_2

print(resultado)
