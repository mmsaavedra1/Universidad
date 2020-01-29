nombre = input()
masa = int(input())
# Ojo que int solo soporta numeros enteros, en cambio float cualquier numero racional
estatura = float(input())

imc = masa/(estatura**2)

# Cuidado con los espacio al imprimir
print(nombre + " tiene un IMC de " + str(imc) + " kg/m^2")