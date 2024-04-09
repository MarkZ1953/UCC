from PySide6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy

from Componentes.TablaResultados import TablaResultados


class VentanaResultados(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabla de Resultados")

        self.layoutPrincipal = QVBoxLayout()

        self.tablaResultados = TablaResultados()
        self.tablaResultados.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.layoutPrincipal.addWidget(self.tablaResultados)

        self.setLayout(self.layoutPrincipal)
