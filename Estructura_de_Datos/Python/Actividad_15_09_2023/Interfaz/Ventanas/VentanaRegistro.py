from PySide6.QtCore import Qt, QDate
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QFormLayout, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QDateEdit


class VentanaRegistro(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la ventana
        self.setWindowTitle("Registrar Terremoto")
        self.setFixedSize(600, 240)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        layoutPrincipal = QHBoxLayout()

        frameFormulario = QGroupBox("Informacion Registro Terremoto")
        layoutFormulario = QFormLayout()
        frameFormulario.setLayout(layoutFormulario)

        self.txtNombreTerremoto = QLineEdit()
        self.txtNombreTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Nombre"), self.txtNombreTerremoto)

        self.dateFechaTerremoto = QDateEdit(QDate.currentDate())
        self.dateFechaTerremoto.setCalendarPopup(True)
        self.dateFechaTerremoto.setDisplayFormat("dd/MM/yyyy")
        self.dateFechaTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Fecha"), self.dateFechaTerremoto)

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
        self.btnSalir.setIcon(QIcon(QPixmap("Imagenes/btnCruz.png")))
        self.btnSalir.setFixedSize(120, 40)
        layoutFunciones.addWidget(self.btnSalir)

        layoutPrincipal.addWidget(frameFormulario)
        layoutPrincipal.addWidget(frameFunciones)
        self.setLayout(layoutPrincipal)

    def limpiarVentanaRegistro(self):
        self.txtNombreTerremoto.setText("")
        self.txtMagnitudTerremoto.setText("")
        self.txtNumeroMuertosTerremoto.setText("")
        self.txtDepartamentoTerremoto.setText("")
        self.dateFechaTerremoto.setDate(QDate.currentDate())
