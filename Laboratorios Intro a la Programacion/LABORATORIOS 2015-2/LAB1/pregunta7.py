a = input("Ingrese la PT, PI, NE y PP con comas entremedio: ").split(',')
print(round(0.3 * (int(a[0]) + int(a[1]) + int(a[2])) + 0.1 * int(a[3])))
