lado = int(input())
area = int(input())
perimetro = int(input())

# Un buen truco es definir como falso todo a priori, y demostrar lo contrario
area_correcta = False
perimetro_correcto = False

# Calculamos los valores de area y perimetro
if lado ** 2 == area:
    area_correcta = True

if lado * 4 == perimetro:
    perimetro_correcto = True

# Analizamos las posibilidades (si se imprime ambas incorrectas las otras no)
if (area_correcta == False) and (perimetro_correcto == False):
    print("El área y el perímetro son incorrectos")

elif area_correcta == False:
    print("El área es incorrecta")

elif perimetro_correcto == False:
    print("El perímetro es incorrecto")

else:
    print("Todo es correcto")