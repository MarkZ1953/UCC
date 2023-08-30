from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QGroupBox, QVBoxLayout, QWidget, QHBoxLayout, QPushButton

from ServGeologicoFelipeCastro.Interfaz.Ventanas.TablaInformacion import TablaInformacion


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a VentanaPrincipal
        self.setWindowTitle("Terremoto - Felipe Castro")
        self.resize(1000, 600)

        # Creamos el Widget y el Layout para VentanaPrincipal
        self.widgetVentanaPrincipal = QWidget()
        self.layoutVentanaPrincipal = QHBoxLayout()
        self.widgetVentanaPrincipal.setLayout(self.layoutVentanaPrincipal)

        self.tablaInformacion = TablaInformacion()

        frameInformacion = QGroupBox("Informacion")
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(self.tablaInformacion)
        frameInformacion.setLayout(layoutVertical)
        self.layoutVentanaPrincipal.addWidget(frameInformacion)

        frameFunciones = QGroupBox("Funciones")
        layoutFunciones = QVBoxLayout()
        layoutFunciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFunciones.setLayout(layoutFunciones)
        self.layoutVentanaPrincipal.addWidget(frameFunciones)

        # Creamos los Botones para las Funciones
        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setFixedSize(120, 40)
        layoutFunciones.addWidget(btnRegistrar)

        btnBuscar = QPushButton("Buscar")
        btnBuscar.setFixedSize(120, 40)
        layoutFunciones.addWidget(btnBuscar)

        btnOrdenar = QPushButton("Ordenar")
        btnOrdenar.setFixedSize(120, 40)
        layoutFunciones.addWidget(btnOrdenar)

        btnListar = QPushButton("Listar")
        btnListar.setFixedSize(120, 40)
        layoutFunciones.addWidget(btnListar)

        self.layoutVentanaPrincipal.addWidget(frameFunciones)
        self.setCentralWidget(self.widgetVentanaPrincipal)


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
