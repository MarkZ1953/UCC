from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QFormLayout, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton


class DetalleTerremoto(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la ventana
        self.setWindowTitle("Detalle Terremoto")
        self.setFixedSize(600, 260)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        layoutPrincipal = QHBoxLayout()

        frameFormulario = QGroupBox("Informacion Registro Terremoto")
        layoutFormulario = QFormLayout()
        frameFormulario.setLayout(layoutFormulario)

        self.txtNombreTerremoto = QLineEdit()
        self.txtNombreTerremoto.setReadOnly(True)
        self.txtNombreTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Nombre"), self.txtNombreTerremoto)

        self.txtFechaTerremoto = QLineEdit()
        self.txtFechaTerremoto.setReadOnly(True)
        self.txtFechaTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Fecha"), self.txtFechaTerremoto)

        self.txtMagnitudTerremoto = QLineEdit()
        self.txtMagnitudTerremoto.setReadOnly(True)
        self.txtMagnitudTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Magnitud"), self.txtMagnitudTerremoto)

        self.txtDepartamentoTerremoto = QLineEdit()
        self.txtDepartamentoTerremoto.setReadOnly(True)
        self.txtDepartamentoTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Departamento"), self.txtDepartamentoTerremoto)

        self.txtNumeroMuertosTerremoto = QLineEdit()
        self.txtNumeroMuertosTerremoto.setReadOnly(True)
        self.txtNumeroMuertosTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("No.Muertos Aproximados"), self.txtNumeroMuertosTerremoto)

        self.txtAyudaEstadoTerremoto = QLineEdit()
        self.txtAyudaEstadoTerremoto.setReadOnly(True)
        self.txtAyudaEstadoTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Ayuda Estado"), self.txtAyudaEstadoTerremoto)

        frameFunciones = QGroupBox("Funciones")
        layoutFunciones = QVBoxLayout()
        layoutFunciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFunciones.setLayout(layoutFunciones)

        self.btnSalir = QPushButton("Salir")
        self.btnSalir.setToolTip("Salir de la ventana")
        self.btnSalir.setIcon(QIcon(QPixmap("Imagenes/btnCruz.png")))
        self.btnSalir.setFixedSize(120, 40)
        self.btnSalir.clicked.connect(lambda: self.close())
        layoutFunciones.addWidget(self.btnSalir)

        layoutPrincipal.addWidget(frameFormulario)
        layoutPrincipal.addWidget(frameFunciones)
        self.setLayout(layoutPrincipal)
