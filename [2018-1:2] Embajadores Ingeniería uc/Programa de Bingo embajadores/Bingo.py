import sys
from Interfaz import *
from random import choice


NOMBRES = list()

with open("nombres.txt", "r", encoding="utf-8") as file:
    for linea in file:
        if not linea in NOMBRES and linea != "\n":
            NOMBRES.append(linea.strip())


class Main(QObject):
    def __init__(self):
        self.bingo = Bingo()
        self.bingo.show()

        self.nombres = NOMBRES

        # Señales ligadas
        self.bingo.boton.clicked.connect(lambda: self.azar())

    def azar(self):

        if len(self.nombres) > 0:
            nombre = str(choice(self.nombres))
            numero = self.nombres.index(nombre)
            self.nombres.pop(numero)
            self.bingo.nombre.setText(nombre)
        else:
            self.bingo.nombre.setText("Game over.")


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    _main = Main()
    sys.exit(app.exec_())