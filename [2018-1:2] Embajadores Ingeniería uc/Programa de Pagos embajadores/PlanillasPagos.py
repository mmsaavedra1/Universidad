import sys
import os
import GoogleSheet

from InterfazGrafica import *
from MatrizDePagos import *

from pprint import pprint


class Main(QObject):

    def __init__(self):

        # Se muestra en pantalla el menu de bienvenida
        self.bienvenida = Bienvenida()
        self.bienvenida.show()
        self.base_de_datos = self.cargar()

        # Se conectan las señales
        self.bienvenida.enviar.clicked.connect(
            lambda: self.iniciar_nueva_hoja(
                self.bienvenida.mensaje1.text()
                + self.bienvenida.semana.currentText()
                + self.bienvenida.mensaje2.text()
                + self.bienvenida.mes.currentText(),
                GoogleSheet.URl_FORMULARIO, GoogleSheet.URL_HISTORIAL
            )
        )

        self.bienvenida.actualizar.clicked.connect(lambda: self.cargar_base_de_datos())

    def iniciar_nueva_hoja(self, nombre, link_formulario, link_historial):
        """
        :param nombre: Nombre de la hoja que se desea trabajar
        :param link_formulario: Link de la hoja que se desea trabajar
        :return:
        """

        # Se comprueba si hay que abrir/crear una hoja para el pago
        GoogleSheet.comprobar_hoja(nombre, link_formulario)
        GoogleSheet.comprobar_hoja(nombre.replace("Formulario", "Actividades"),
                                   link_historial)

        # Se almacena el nombre de la sheet
        self.hoja_formulario = nombre
        self.hoja_historial = nombre.replace("Formulario", "Actividades")

        # Se crea la lista que almacenará toda la informacion para ser enviada
        # a cada hoja
        self.datos = list()

        # Se genera la instacia del form y se oculta la bienvenida
        self.form = Form()
        self.form.show()
        self.bienvenida.hide()

        # Se setea el nombre de la hoja
        self.form.setWindowTitle(self.hoja_formulario)

        # Se da forma a la instancia del form
        self.nombres_completos, self.rut_completos, self.correos_uc = GoogleSheet.ordenar_informacion(self.cargar())
        self.form.nombre_completo.addItems(self.nombres_completos)
        self.form.actividad.addItems(PARAMETROS_SIMBOLOGIA_2018.keys())

        # Se conectan las señales
        self.form.sheet_formulario.clicked.connect(lambda: GoogleSheet.abrir_formulario_google())
        self.form.sheet_historial.clicked.connect(lambda: GoogleSheet.abrir_historial_google())
        self.form.cambiar_pago.clicked.connect(lambda: self.cambiar_pago())
        self.form.enviar.clicked.connect(lambda: self.enviar())
        self.form.agregar.clicked.connect(lambda: self.agregar())
        self.form.eliminar.clicked.connect(lambda: self.eliminar())

    def cargar_base_de_datos(self):
        """
        Funcion que genera un archivo .txt que almacena la base de datos.
        :return:
        """

        BASE_DE_DATOS = GoogleSheet.obtener_datos(GoogleSheet.URL_BASE_DATOS)

        with open("Base de Datos.txt", "w", encoding="utf-8") as file:
            for dato in BASE_DE_DATOS:
                cadena = str.join(";", dato)
                file.write(cadena)
                file.write("\n")

        QMessageBox.warning(QWidget(), "Listo", "Base de datos actualizada!")
        return BASE_DE_DATOS

    def cargar(self):
        """
        Funcion que carga los datos del archivo .txt con la base de datos
        :return:
        """
        if os.path.exists("Base de Datos.txt"):
            datos = list()
            with open("Base de Datos.txt", "r", encoding="utf-8") as file:
                for linea in file:
                    linea = linea[:-1]
                    _datos = linea.split(";")
                    datos.append(_datos)

            return datos
        else:
            return self.cargar_base_de_datos()

    def agregar(self):
        """
        Metodo encargador de ir almacenando la informacion en una lista,
        mostrar la en lista.
        """

        if self.form.nombre_completo.currentText():

            # * Se busca el rut asoociado al nombre
            indice = self.nombres_completos.index(
                self.form.nombre_completo.currentText())

            # Se crea el pack que se almacena
            pack = [self.hoja_formulario,
                    self.hoja_historial,
                    self.form.nombre_completo.currentText(),
                    self.rut_completos[indice],
                    self.form.fecha.text(),
                    self.form.rbd.text(),
                    self.form.actividad.currentText()]

            # Se guarda el pack de informacion en la lista de datos, para
            # ser enviado cuando termine
            self.datos.append(pack)

            # Se setea en la lista los datos
            mensaje = "{} | Tipo de actividad: {} | Fecha: {}".format(self.form.nombre_completo.currentText(),
                                                                      self.form.actividad.currentText(),
                                                                      self.form.fecha.text())
            self.form.listado.addItem(mensaje)
            self.form.listado.show()


    def eliminar(self):
        """
        Metodo que una vez elegido un valor de la lista este se elimina.
        """

        if self.form.listado.currentItem():

            # Borramos de la lista y de la pantalla el usuario seleccionado.
            self.datos.pop(self.form.listado.currentRow())
            self.form.listado.takeItem(self.form.listado.currentRow())
            pprint(self.datos)
        else:
            QMessageBox.warning(QWidget(), "",
                "Debes seleccionar un nombre de la lista para borrar.")

    def cambiar_pago(self):
        """
        Retorna al Menu de inicio para abrir una nueva hoja
        """
        self.form.close()
        self.bienvenida.show()

    def enviar(self): # Unir con el metodo de envio de GoogleSheet
        """
        Funcion que recibe la informacion y escribe en la hoja de pagos.
        """

        for pack in self.datos:
            GoogleSheet.enviar_datos_formulario(pack)
            pprint(pack)

        QMessageBox.warning(QWidget(), "Listo", "Datos enviados e ingresados!")


if __name__ == '__main__':
    def hook(type, value, traceback):
        print(type)
        print(traceback)

    sys.__excepthook__ = hook
    app = QApplication(sys.argv)
    _main = Main()
    sys.exit(app.exec_())
