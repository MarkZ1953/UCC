from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QFormLayout, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton


class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la ventana
        self.setWindowTitle("Registrar Terremoto")
        self.setFixedSize(600, 240)

        layoutPrincipal = QHBoxLayout()

        frameFormulario = QGroupBox("Informacion Registro Terremoto")
        layoutFormulario = QFormLayout()
        frameFormulario.setLayout(layoutFormulario)

        self.txtCiudadTerremoto = QLineEdit()
        self.txtCiudadTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Ciudad"), self.txtCiudadTerremoto)

        self.txtFechaTerremoto = QLineEdit()
        self.txtFechaTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Fecha"), self.txtFechaTerremoto)

        self.txtMagnitudTerremoto = QLineEdit()
        self.txtMagnitudTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Magnitud"), self.txtMagnitudTerremoto)

        self.txtDepartamentoTerremoto = QLineEdit()
        self.txtDepartamentoTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Departamento"), self.txtDepartamentoTerremoto)

        self.txtNumeroMuertosTerremoto = QLineEdit()
        self.txtNumeroMuertosTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("No.Muertos Aproximados"), self.txtNumeroMuertosTerremoto)

        frameFunciones = QGroupBox("Funciones")
        layoutFunciones = QVBoxLayout()
        layoutFunciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFunciones.setLayout(layoutFunciones)

        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.setFixedSize(120, 40)
        layoutFunciones.addWidget(self.btnAceptar)

        self.btnSalir = QPushButton("Salir")
        self.btnSalir.setFixedSize(120, 40)
        layoutFunciones.addWidget(self.btnSalir)

        layoutPrincipal.addWidget(frameFormulario)
        layoutPrincipal.addWidget(frameFunciones)
        self.setLayout(layoutPrincipal)

    def limpiarVentanaRegistro(self):
        self.txtCiudadTerremoto.setText("")
        self.txtMagnitudTerremoto.setText("")
        self.txtNumeroMuertosTerremoto.setText("")
        self.txtDepartamentoTerremoto.setText("")
        self.txtFechaTerremoto.setText("")
