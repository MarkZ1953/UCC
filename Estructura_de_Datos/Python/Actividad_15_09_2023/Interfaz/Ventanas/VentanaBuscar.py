from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QFormLayout, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QGridLayout


class VentanaBuscar(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la ventana
        self.setWindowTitle("Buscar Terremoto")
        self.setFixedSize(600, 320)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        layoutPrincipal = QGridLayout()

        frameFormulario = QGroupBox("Informacion Busqueda Terremoto")
        layoutFormulario = QFormLayout()
        frameFormulario.setLayout(layoutFormulario)

        self.txtNombreTerremoto = QLineEdit()
        self.txtNombreTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Nombre"), self.txtNombreTerremoto)

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

        frameBuscarPor = QGroupBox("Buscar Por")
        layoutBuscarPor = QHBoxLayout()
        layoutBuscarPor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameBuscarPor.setLayout(layoutBuscarPor)

        self.btnBuscarPorNombre = QPushButton("Nombre")
        self.btnBuscarPorNombre.setFixedSize(170, 40)
        layoutBuscarPor.addWidget(self.btnBuscarPorNombre)

        self.btnBuscarPorNumeroMuertos = QPushButton("Numero de Muertos")
        self.btnBuscarPorNumeroMuertos.setFixedSize(170, 40)
        layoutBuscarPor.addWidget(self.btnBuscarPorNumeroMuertos)

        frameBuscar = QGroupBox("Buscar")
        layoutBuscar = QVBoxLayout()
        layoutBuscar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameBuscar.setLayout(layoutBuscar)

        self.btnMayorNumeroMuertos = QPushButton("Mayor Numero de Muertos")
        self.btnMayorNumeroMuertos.setFixedSize(170, 40)
        layoutBuscar.addWidget(self.btnMayorNumeroMuertos)

        self.btnMenorNumeroMuertos = QPushButton("Menor Numero de Muertos")
        self.btnMenorNumeroMuertos.setFixedSize(170, 40)
        layoutBuscar.addWidget(self.btnMenorNumeroMuertos)

        self.btnMayorMagnitud = QPushButton("Mayor Magnitud")
        self.btnMayorMagnitud.setFixedSize(170, 40)
        layoutBuscar.addWidget(self.btnMayorMagnitud)

        self.btnMenorMagnitud = QPushButton("Menor Magnitud")
        self.btnMenorMagnitud.setFixedSize(170, 40)
        layoutBuscar.addWidget(self.btnMenorMagnitud)

        frameFunciones = QGroupBox("Funciones")
        layoutFunciones = QHBoxLayout()
        layoutFunciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFunciones.setLayout(layoutFunciones)

        self.btnSalir = QPushButton()
        self.btnSalir.setIcon(QIcon(QPixmap("Imagenes/btnCruz.png")))
        self.btnSalir.setFixedSize(80, 40)
        self.btnSalir.setToolTip("Salir de la ventana")
        layoutFunciones.addWidget(self.btnSalir)

        self.btnLimpiar = QPushButton()
        self.btnLimpiar.setIcon(QIcon(QPixmap("Imagenes/btnNuevo.png")))
        self.btnLimpiar.setToolTip("Limpiar todas las casillas")
        self.btnLimpiar.setFixedSize(80, 40)
        self.btnLimpiar.clicked.connect(self.limpiarVentanaRegistro)
        layoutFunciones.addWidget(self.btnLimpiar)

        layoutPrincipal.addWidget(frameFormulario, 0, 0)
        layoutPrincipal.addWidget(frameBuscar, 0, 1)
        layoutPrincipal.addWidget(frameBuscarPor, 1, 0)
        layoutPrincipal.addWidget(frameFunciones, 1, 1)

        self.setLayout(layoutPrincipal)

    def limpiarVentanaRegistro(self):
        self.txtNombreTerremoto.setText("")
        self.txtMagnitudTerremoto.setText("")
        self.txtNumeroMuertosTerremoto.setText("")
        self.txtDepartamentoTerremoto.setText("")
        self.txtFechaTerremoto.setText("")
