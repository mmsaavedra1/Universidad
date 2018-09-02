telefono = int(input())
hora = int(input())
minutos = int(input())

# condicion 1 [00:00 - 8:20]
if (0 <= hora < 8) or (hora == 8 and (0 <= minutos <= 20)):
    print("CONTESTAR")

# condicion 2 (8:20 - 13:00)
elif (hora == 8 and (20 < minutos <= 59)) or (9 <= hora < 12) or (
        hora == 12 and (0 <= minutos <= 59)):
    if telefono % 100000 == 909:
        print("CONTESTAR")
    else:
        print("NO CONTESTAR")

# condicion 3 [13:00 - 19:50]
elif (13 <= hora <= 18) or (hora == 19 and (0 <= minutos <= 50)):
    if telefono // 100000 == 877:
        print("NO CONTESTAR")
    else:
        print("CONTESTAR")

# condicion 4 (19:00 - 23:59]
else:
    print("NO CONTESTAR")