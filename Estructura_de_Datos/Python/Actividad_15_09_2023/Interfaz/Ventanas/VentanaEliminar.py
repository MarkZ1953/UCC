from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QWidget, QFormLayout, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit, QPushButton, \
    QGridLayout

from Base_de_Datos.TerremotosDB import InformacionTerremotos


class VentanaEliminar(QWidget):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a la ventana
        self.setWindowTitle("Buscar Terremoto")
        self.setFixedSize(600, 290)
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        layoutPrincipal = QGridLayout()

        frameFormulario = QGroupBox("Informacion Busqueda Terremoto")
        layoutFormulario = QFormLayout()
        layoutFormulario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFormulario.setLayout(layoutFormulario)

        self.txtIdTerremoto = QLineEdit()
        self.txtIdTerremoto.textChanged.connect(self.cambiarValoresVentanaEliminar)
        self.txtIdTerremoto.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Id"), self.txtIdTerremoto)

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

        self.txtAyudaEstado = QLineEdit()
        self.txtAyudaEstado.setFixedHeight(30)
        layoutFormulario.addRow(QLabel("Ayuda Estado"), self.txtAyudaEstado)

        frameFunciones = QGroupBox("Funciones")
        layoutFunciones = QVBoxLayout()
        layoutFunciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFunciones.setLayout(layoutFunciones)

        self.btnEliminar = QPushButton("Eliminar")
        self.btnEliminar.setIcon(QIcon(QPixmap("Imagenes/btnMenos.png")))
        self.btnEliminar.setToolTip("Ingresa el id de un terremoto en la casilla 'Id' para buscar el terremoto")
        self.btnEliminar.setFixedSize(120, 40)
        layoutFunciones.addWidget(self.btnEliminar)

        self.btnLimpiar = QPushButton("Limpiar")
        self.btnLimpiar.setIcon(QIcon(QPixmap("Imagenes/btnNuevo.png")))
        self.btnLimpiar.setToolTip("Limpiar todas las casillas")
        self.btnLimpiar.setFixedSize(120, 40)
        self.btnLimpiar.clicked.connect(self.limpiarVentanaEliminar)
        layoutFunciones.addWidget(self.btnLimpiar)

        self.btnSalir = QPushButton("Salir")
        self.btnSalir.setIcon(QIcon(QPixmap("Imagenes/btnCruz.png")))
        self.btnSalir.setFixedSize(120, 40)
        self.btnSalir.setToolTip("Salir de la ventana")
        self.btnSalir.clicked.connect(lambda: self.close())
        layoutFunciones.addWidget(self.btnSalir)

        layoutPrincipal.addWidget(frameFormulario, 0, 0)
        layoutPrincipal.addWidget(frameFunciones, 0, 1)

        self.setLayout(layoutPrincipal)

    def cambiarValoresVentanaEliminar(self):
        try:
            if self.txtIdTerremoto.text() != "" and self.txtIdTerremoto.text().isnumeric():
                terremoto = InformacionTerremotos.seleccionarTerremotoPorId(self.txtIdTerremoto.text())

                self.txtIdTerremoto.setText(str(terremoto.getIdTerremoto))
                self.txtNombreTerremoto.setText(terremoto.getNombre)
                self.txtMagnitudTerremoto.setText(str(terremoto.getMagnitud))
                self.txtNumeroMuertosTerremoto.setText(str(terremoto.getNumeroMuertos))
                self.txtDepartamentoTerremoto.setText(terremoto.getDepartamento)
                self.txtFechaTerremoto.setText(terremoto.getFecha)
                self.txtAyudaEstado.setText(terremoto.getAyudaEstado)
            else:
                self.limpiarVentanaEliminar()
        except Exception as e:
            pass

    def limpiarVentanaEliminar(self):
        self.txtIdTerremoto.setText("")
        self.txtNombreTerremoto.setText("")
        self.txtMagnitudTerremoto.setText("")
        self.txtNumeroMuertosTerremoto.setText("")
        self.txtDepartamentoTerremoto.setText("")
        self.txtFechaTerremoto.setText("")
        self.txtAyudaEstado.setText("")
