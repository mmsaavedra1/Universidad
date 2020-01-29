from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QLineEdit,
                             QApplication, QComboBox, QDateEdit, QCheckBox,
                             QMessageBox, QListWidget)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import pyqtSignal, QObject


class Bienvenida(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(500, 300, 400, 130)
        self.setFixedSize(400, 130)
        self.setWindowTitle("Programa Pagos de Actividades")

        # Mensaje de bienvenida
        self.mensaje = QLabel(self)
        self.mensaje.setGeometry(30, 20, 240, 20)
        self.mensaje.setText("Ingresa el nombre de la hoja de cálculo")

        # Etiqueta de relleno
        self.mensaje1 = QLabel(self)
        self.mensaje1.setGeometry(20, 50, 80, 20)
        self.mensaje1.setText("Formulario - ")

        # Opcion de semana para el nombre de la hoja del formulario
        self.semana = QComboBox(self)
        self.semana.setGeometry(100, 50, 50, 20)
        self.semana.addItems(["1", "2"])

        # Etiqueta de relleno
        self.mensaje2 = QLabel(self)
        self.mensaje2.setGeometry(150, 50, 60, 20)
        self.mensaje2.setText(" quincena ")

        # Opcion de mes para el nombre de la hoja del formulario
        self.mes = QComboBox(self)
        self.mes.setGeometry(210, 50, 80, 20)
        self.mes.addItems(["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
                           "Agosto", "Septiembre", "Octubre", "Noviembre",
                           "Diciembre"])

        # Boton de envio
        self.enviar = QPushButton(self)
        self.enviar.setGeometry(210, 90, 80, 20)
        self.enviar.setText("Enviar")

        # Boton actualizacion de Base de datos
        self.actualizar = QPushButton(self)
        self.actualizar.setGeometry(20, 90, 180, 20)
        self.actualizar.setText("Actualizar Base de Datos")

        # Imagen de embajadores ❤️
        self.embajadores = QLabel(self)
        self.embajadores.setGeometry(290, 1, 110, 120)
        self.embajadores.setPixmap(QPixmap("Imagenes/logo_embajadores.png").scaled(110, 120))


class Form(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 300, 640, 400)
        self.setFixedSize(640, 400)
        self.setWindowTitle("ACA DEBE IR EL NOMBRE DE LA HOJA QUE SE ESTA ABRIENDO")

        # Mensaje de bienvenida
        self.subtitulo = QLabel(self)
        self.subtitulo.setGeometry(40, 20, 460, 70)
        self.subtitulo.setPixmap(QPixmap("Imagenes/Banner_blanco.png").scaled(460, 70))

        # Imagen de embajadores
        self.embajadores = QLabel(self)
        self.embajadores.setGeometry(500, -7.5, 110, 120)
        self.embajadores.setPixmap(QPixmap("Imagenes/logo_embajadores.png").scaled(110, 120))

        # Etiqueta de nombre con su dato
        self.etiqueta_nombre = QLabel(self)
        self.etiqueta_nombre.setGeometry(35, 110, 110, 20)
        self.etiqueta_nombre.setText("Nombre Completo")

        self.nombre_completo = QComboBox(self)
        self.nombre_completo.setGeometry(155, 105, 450, 25)

        # Etiqueta de fecha junto con su dato
        self.etiqueta_fecha = QLabel(self)
        self.etiqueta_fecha.setGeometry(35, 145, 180, 16)
        self.etiqueta_fecha.setText("Fecha que realizo la actividad")

        self.fecha = QDateEdit(self)
        self.fecha.setGeometry(225, 145, 100, 20)

        # Etiqueta de RBD con su dato
        self.etiqueta_rbd = QLabel(self)
        self.etiqueta_rbd.setGeometry(400, 145, 50, 20)
        self.etiqueta_rbd.setText("RBD")

        self.rbd = QLineEdit(self)
        self.rbd.setGeometry(455, 145, 110, 20)

        # Etiqueta tipo de actividad realizada con su dato
        self.etiqueta_actividad = QLabel(self)
        self.etiqueta_actividad.setGeometry(110, 185, 170, 15)
        self.etiqueta_actividad.setText("Tipo de actividad realizada")

        self.actividad = QComboBox(self)
        self.actividad.setGeometry(285, 180, 240, 25)

        # Lista de nombres de las actividades
        self.listado = QListWidget(self)
        self.listado.setGeometry(60, 220, 410, 110)

        # Boton para agregar persona a la lista
        self.agregar = QPushButton(self)
        self.agregar.setGeometry(490, 245, 120, 30)
        self.agregar.setText("Agregar")

        # Boton para eliminar persona de la lista
        self.eliminar = QPushButton(self)
        self.eliminar.setGeometry(490, 275, 120, 30)
        self.eliminar.setText("Borrar")

        # Boton abrir Formulario GoogleSheet
        self.sheet_formulario = QPushButton(self)
        self.sheet_formulario.setGeometry(10, 340, 150, 40)
        self.sheet_formulario.setText("Abrir Formulario")

        # Boton abrir Historial GoogleSheet
        self.sheet_historial = QPushButton(self)
        self.sheet_historial.setGeometry(170, 340, 150, 40)
        self.sheet_historial.setText("Abrir Historial")

        # Boton abrir otro pago
        self.cambiar_pago = QPushButton(self)
        self.cambiar_pago.setGeometry(330, 340, 150, 40)
        self.cambiar_pago.setText("Cambiar de pago")

        # Boton para enviar los datos
        self.enviar = QPushButton(self)
        self.enviar.setGeometry(490, 340, 140, 40)
        self.enviar.setText("Enviar")


