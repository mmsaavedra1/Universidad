numero = str(input("Ingrese numero telefonico: ")).strip()
hora = int(input("Ingrese hora de la llamada: "))
contestar = False

if hora > 0 and hora <= 7:
    contestar = True
elif hora < 14:
    contestar = int(numero[-3:]) == 909
elif hora < 19:
    contestar = hora >= 17 and not (int(numero[:3]) == 877)
else:
    contestar = False

print("CONTESTAR" if contestar else "NO CONTESTAR")
