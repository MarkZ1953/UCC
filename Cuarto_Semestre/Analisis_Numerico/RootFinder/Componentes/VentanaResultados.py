from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QFrame, QHBoxLayout

from Componentes.TablaResultados import TablaResultados
from Utiles import Etiqueta


class VentanaResultados(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabla de Resultados")

        self.layoutPrincipal = QVBoxLayout()

        self.__crearAreaTitulo()

        self.tablaResultados = TablaResultados()
        self.tablaResultados.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutPrincipal.addWidget(self.tablaResultados)

        frameTitulo = QFrame()
        frameTitulo.setFixedHeight(40)
        frameTitulo.setStyleSheet("background-color: rgb(14, 49, 129);")

        layoutTitulo = QHBoxLayout()
        frameTitulo.setLayout(layoutTitulo)

        self.layoutPrincipal.addWidget(frameTitulo)

        self.setLayout(self.layoutPrincipal)

    def __crearAreaTitulo(self):

        frameTitulo = QFrame()
        frameTitulo.setFixedHeight(80)
        frameTitulo.setStyleSheet("background-color: rgb(14, 49, 129);")

        layoutTitulo = QHBoxLayout()
        frameTitulo.setLayout(layoutTitulo)

        titulo = Etiqueta(texto="Tabla de Resultados", bold=True, font="Arial", font_size=16)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("color: white;")
        layoutTitulo.addWidget(titulo)

        self.layoutPrincipal.addWidget(frameTitulo)
