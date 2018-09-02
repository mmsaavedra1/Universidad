from poker import Carta, Baraja, Tablero

player1 = "Hugo"
player2 = "Paco"
scores = {player1:0, player2:0}
scoreboard = "\n"+player1 + ": {"+player1+"} - " + player2 + ": {"+player2+"}"
win = "Gano {}!"
win_msg = "\nEl ganador final es {0}, con {1} puntos!"
values = {'A':20, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':11, 'Q':12, 'K':13}

deck = Baraja()
deck.barajar()

card1 = card2 = None
table = Tablero(width=30, height=12)
table.dibujarBorde(0, 0, 29, 11)
table.escribirMensaje("- Hugo -", 4, 1)
table.escribirMensaje("- Paco -", 18, 1)

for i in range(26):
    print("\n\nEstas son las cartas:")
    card1 = deck.obtenerCarta()
    card2 = deck.obtenerCarta()

    table.dibujarCarta(card1, 4, 3)
    table.dibujarCarta(card2, 18, 3)

    print(table)

    if values[card1.obtenerValor()] != values[card2.obtenerValor()]:
        comp = values[card1.obtenerValor()] > values[card2.obtenerValor()]
        scores[player1] += 2 * comp
        scores[player2] += 2 * (not comp)
        print(win.format(player1 if comp else player2))
    else:
        if card1.obtenerPalo() == 'C' and card2.obtenerPalo() != 'C':
            scores[player1] += 2
            print(win.format(player1))
        elif card1.obtenerPalo() != 'C' and card2.obtenerPalo() == 'C':
            scores[player2] += 2
            print(win.format(player1))
        else:
            scores[player1] += 1
            scores[player2] += 1
            print("Empate!")

    print(scoreboard.format(**scores))

if scores[player1] == scores[player2]:
    print("\nSe logro un empate con {} puntos!".format(scores[player1]))
else:
    winner1 = scores[player1] > scores[player2]
    print(win_msg.format(*([player1, scores[player1]] if winner1 else [player2, scores[player2]])))