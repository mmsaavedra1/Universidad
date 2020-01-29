from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit,
                             QApplication, QComboBox, QDateEdit, QCheckBox,
                             QMessageBox, QListWidget)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSignal, QObject


class Bingo(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 300, 750, 470)
        self.setFixedSize(750, 470)
        self.setWindowTitle("Bingo")

        self.nombre = QLabel(self)
        self.nombre.setGeometry(90, 100, 600, 260)
        self.nombre.setText("Nombre")
        self.nombre.setFont(QFont("Sanserif", 100, QFont.Bold))
        self.nombre.setAlignment(Qt.AlignCenter)

        self.boton = QPushButton(self)
        self.boton.setGeometry(320, 320, 130, 30)
        self.boton.setText("Nuevo nombre👀")

        self.logo1 = QLabel(self)
        self.logo1.setGeometry(40, 10, 130, 130)
        self.logo1.setPixmap(QPixmap("logo_embajadores.png").scaled(130, 130))

        self.logo2 = QLabel(self)
        self.logo2.setGeometry(600, 10, 130, 130)
        self.logo2.setPixmap(QPixmap("logo_embajadores.png").scaled(130, 130))

        self.nino = QLabel(self)
        self.nino.setGeometry(40, 300, 120, 130)
        self.nino.setPixmap(QPixmap("nino.png").scaled(100, 130))

        self.nina = QLabel(self)
        self.nina.setGeometry(610, 300, 120, 130)
        self.nina.setPixmap(QPixmap("nina.png").scaled(100, 130))