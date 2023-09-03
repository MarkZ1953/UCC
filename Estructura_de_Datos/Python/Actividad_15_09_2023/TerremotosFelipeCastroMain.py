import locale

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QGroupBox, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, \
    QMessageBox, QGridLayout, QComboBox, QTableWidgetItem

from Interfaz.VentanaDetalles.DetalleTerremoto import DetalleTerremoto
from Interfaz.Ventanas.TablaInformacion import TablaInformacion
from Interfaz.Ventanas.VentanaBuscar import VentanaBuscar
from Interfaz.Ventanas.VentanaRegistro import VentanaRegistro
from TerremotoFelipeCastro import TerremotoFelipeCastro

from Base_de_Datos.TerremotosDB import InformacionTerremotos


class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Agregamos algunas configuraciones a VentanaPrincipal
        self.setWindowTitle("Terremoto - Felipe Castro")
        self.resize(1000, 600)

        # Creamos el Widget y el Layout para VentanaPrincipal
        self.widgetVentanaPrincipal = QWidget()
        self.layoutVentanaPrincipal = QGridLayout()
        self.widgetVentanaPrincipal.setLayout(self.layoutVentanaPrincipal)

        # Importamos las ventanas
        self.ventanaRegistrarTerremoto = VentanaRegistro()
        self.ventanaBuscarTerremoto = VentanaBuscar()
        self.ventanaDetalleTerremoto = DetalleTerremoto()

        # Agregamos las funciones a la ventana de buscar
        self.ventanaBuscarTerremoto.btnSalir.clicked.connect(lambda: self.ventanaBuscarTerremoto.close())
        self.ventanaBuscarTerremoto.btnMayorNumeroMuertos.clicked.connect(self.buscarTerremotoConMayorNumeroDeMuertosFelipeCastro)
        self.ventanaBuscarTerremoto.btnBuscarPorNumeroMuertos.clicked.connect(self.buscarTerremotoPorNumeroDeMuertosFelipeCastro)
        self.ventanaBuscarTerremoto.btnMenorNumeroMuertos.clicked.connect(self.buscarTerremotoConMenorNumeroDeMuertos)
        self.ventanaBuscarTerremoto.btnBuscarPorNombre.clicked.connect(self.buscarTerremotoPorNombreFelipeCastro)
        self.ventanaBuscarTerremoto.btnMayorMagnitud.clicked.connect(self.buscarTerremotoConMayorMagnitud)
        self.ventanaBuscarTerremoto.btnMenorMagnitud.clicked.connect(self.buscarTerremotoConMenorMagnitud)

        # Agregamos las funciones a la ventana de registrar
        self.ventanaRegistrarTerremoto.btnAceptar.clicked.connect(self.registrarTerremotoFelipeCastro)
        self.ventanaRegistrarTerremoto.btnSalir.clicked.connect(lambda: self.ventanaRegistrarTerremoto.close())

        # Agregamos las funciones a la ventana de detalle
        self.ventanaDetalleTerremoto.btnSalir.clicked.connect(lambda: self.ventanaDetalleTerremoto.close())

        self.tablaInformacion = TablaInformacion()

        frameOrdenamiento = QGroupBox("Ordenamiento")
        layoutOrdenamiento = QHBoxLayout()
        layoutOrdenamiento.addWidget(self.tablaInformacion)
        frameOrdenamiento.setLayout(layoutOrdenamiento)
        self.layoutVentanaPrincipal.addWidget(frameOrdenamiento, 0, 0)

        frameInformacion = QGroupBox("Informacion")
        layoutVertical = QVBoxLayout()
        layoutVertical.addWidget(self.tablaInformacion)
        frameInformacion.setLayout(layoutVertical)
        self.layoutVentanaPrincipal.addWidget(frameInformacion, 1, 0)

        frameFunciones = QGroupBox("Funciones")
        layoutFunciones = QVBoxLayout()
        layoutFunciones.setAlignment(Qt.AlignmentFlag.AlignCenter)
        frameFunciones.setLayout(layoutFunciones)
        self.layoutVentanaPrincipal.addWidget(frameFunciones, 0, 1, 2, 1)

        # Creamos los Botones para las Funciones
        btnRegistrar = QPushButton("Registrar")
        btnRegistrar.setFixedSize(120, 40)
        btnRegistrar.clicked.connect(self.abrirVentanaRegistro)
        layoutFunciones.addWidget(btnRegistrar)

        self.btnListar = QPushButton("Listar")
        self.btnListar.setFixedSize(120, 40)
        self.btnListar.clicked.connect(self.listarTerremotosFelipeCastro)
        layoutFunciones.addWidget(self.btnListar)

        btnBuscar = QPushButton("Buscar")
        btnBuscar.setFixedSize(120, 40)
        btnBuscar.clicked.connect(self.abrirVentanaBuscar)
        layoutFunciones.addWidget(btnBuscar)

        self.cbOrdenamiento = QComboBox()
        self.cbOrdenamiento.addItem("Nombres (Ascendente)", 0)
        self.cbOrdenamiento.addItem("Nombres (Descendente)", 1)
        self.cbOrdenamiento.addItem("Numero de Muertos (Ascendente)", 2)
        self.cbOrdenamiento.addItem("Numero de Muertos (Descendente)", 3)
        self.cbOrdenamiento.addItem("Magnitud (Ascendente)", 4)
        self.cbOrdenamiento.addItem("Magnitud (Descendente)", 5)
        self.cbOrdenamiento.setFixedHeight(40)
        layoutOrdenamiento.addWidget(self.cbOrdenamiento)

        btnOrdenar = QPushButton("Ordenar")
        btnOrdenar.setFixedSize(120, 40)
        btnOrdenar.clicked.connect(self.ordenarTerremotosPor)
        layoutOrdenamiento.addWidget(btnOrdenar)

        self.btnSalir = QPushButton("Salir")
        self.btnSalir.setFixedSize(120, 40)
        self.btnSalir.clicked.connect(lambda: self.close())
        layoutFunciones.addWidget(self.btnSalir)

        self.setCentralWidget(self.widgetVentanaPrincipal)

    def registrarTerremotoFelipeCastro(self):
        try:
            InformacionTerremotos.registrarTerremoto(TerremotoFelipeCastro(
                self.ventanaRegistrarTerremoto.txtCiudadTerremoto.text(),
                self.ventanaRegistrarTerremoto.txtFechaTerremoto.text(),
                self.ventanaRegistrarTerremoto.txtMagnitudTerremoto.text(),
                self.ventanaRegistrarTerremoto.txtDepartamentoTerremoto.text(),
                self.ventanaRegistrarTerremoto.txtNumeroMuertosTerremoto.text()
            ))
        except Exception as e:
            QMessageBox.critical(self, "Error", f"{e}", QMessageBox.StandardButton.Ok)
        finally:
            self.ventanaRegistrarTerremoto.limpiarVentanaRegistro()
            self.tablaInformacion.clearContents()
            self.tablaInformacion.setRowCount(0)
            self.tablaInformacion.actualizarTablaInformacion()

    def ordenarPorMagnitudFelipeCastro(self, ascendente):
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()

        if ascendente:
            for i in range(len(terremotos)):
                for j in range(0, len(terremotos)-i-1):
                    if terremotos[j].getMagnitud > terremotos[j+1].getMagnitud:
                        terremotos[j], terremotos[j+1] = terremotos[j+1], terremotos[j]
        else:
            for i in range(len(terremotos)):
                for j in range(0, len(terremotos) - i - 1):
                    if terremotos[j].getMagnitud < terremotos[j + 1].getMagnitud:
                        terremotos[j], terremotos[j + 1] = terremotos[j + 1], terremotos[j]

        self.ordenarTablaInformacion(terremotos)

    def ordenarPorNumeroMuertosFelipeCastro(self, ascendente):
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()

        if ascendente:
            for i in range(len(terremotos)):
                for j in range(0, len(terremotos)-i-1):
                    if terremotos[j].getNumeroMuertos > terremotos[j+1].getNumeroMuertos:
                        terremotos[j], terremotos[j+1] = terremotos[j+1], terremotos[j]
        else:
            for i in range(len(terremotos)):
                for j in range(0, len(terremotos) - i - 1):
                    if terremotos[j].getNumeroMuertos < terremotos[j + 1].getNumeroMuertos:
                        terremotos[j], terremotos[j + 1] = terremotos[j + 1], terremotos[j]

        self.ordenarTablaInformacion(terremotos)

    def ordenarPorNombreFelipeCastro(self, ascendente):
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()

        if ascendente:
            for i in range(len(terremotos)):
                for j in range(0, len(terremotos)-i-1):
                    if terremotos[j].getNombre > terremotos[j+1].getNombre:
                        terremotos[j], terremotos[j+1] = terremotos[j+1], terremotos[j]
        else:
            for i in range(len(terremotos)):
                for j in range(0, len(terremotos) - i - 1):
                    if terremotos[j].getNombre < terremotos[j + 1].getNombre:
                        terremotos[j], terremotos[j + 1] = terremotos[j + 1], terremotos[j]

        self.ordenarTablaInformacion(terremotos)

    def ordenarTerremotosPor(self):
        if self.cbOrdenamiento.currentData() == 0:
            self.ordenarPorNombreFelipeCastro(True)
        if self.cbOrdenamiento.currentData() == 1:
            self.ordenarPorNombreFelipeCastro(False)
        if self.cbOrdenamiento.currentData() == 2:
            self.ordenarPorNumeroMuertosFelipeCastro(True)
        if self.cbOrdenamiento.currentData() == 3:
            self.ordenarPorNumeroMuertosFelipeCastro(False)
        if self.cbOrdenamiento.currentData() == 4:
            self.ordenarPorMagnitudFelipeCastro(True)
        elif self.cbOrdenamiento.currentData() == 5:
            self.ordenarPorMagnitudFelipeCastro(False)

    def listarTerremotosFelipeCastro(self):
        self.tablaInformacion.clearContents()
        self.tablaInformacion.setRowCount(0)
        self.tablaInformacion.actualizarTablaInformacion()

    def buscarTerremotoPorNombreFelipeCastro(self):
        nombreTerremoto = self.ventanaBuscarTerremoto.txtNombreTerremoto.text()
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()
        terremotoPorNombre = ""

        for terremoto in terremotos:
            if nombreTerremoto.lower() == terremoto.getNombre.lower():
                terremotoPorNombre = terremoto

        self.ventanaBuscarTerremoto.txtNombreTerremoto.setText(terremotoPorNombre.getNombre)
        self.ventanaBuscarTerremoto.txtFechaTerremoto.setText(terremotoPorNombre.getFecha)
        self.ventanaBuscarTerremoto.txtMagnitudTerremoto.setText(str(terremotoPorNombre.getMagnitud))
        self.ventanaBuscarTerremoto.txtDepartamentoTerremoto.setText(terremotoPorNombre.getDepartamento)
        self.ventanaBuscarTerremoto.txtNumeroMuertosTerremoto.setText(str(terremotoPorNombre.getNumeroMuertos))


    def buscarTerremotoPorNumeroDeMuertosFelipeCastro(self):
        pass

    def buscarTerremotoConMayorNumeroDeMuertosFelipeCastro(self):
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()
        tempNumMayor = terremotos[0].getNumeroMuertos
        terremotoNumMuertosMayor = terremotos[0]

        for terremoto in terremotos:
            if tempNumMayor < terremoto.getNumeroMuertos:
                tempNumMayor = terremoto.getNumeroMuertos
                terremotoNumMuertosMayor = terremoto

        self.ventanaBuscarTerremoto.txtNombreTerremoto.setText(terremotoNumMuertosMayor.getNombre)
        self.ventanaBuscarTerremoto.txtFechaTerremoto.setText(terremotoNumMuertosMayor.getFecha)
        self.ventanaBuscarTerremoto.txtMagnitudTerremoto.setText(str(terremotoNumMuertosMayor.getMagnitud))
        self.ventanaBuscarTerremoto.txtDepartamentoTerremoto.setText(terremotoNumMuertosMayor.getDepartamento)
        self.ventanaBuscarTerremoto.txtNumeroMuertosTerremoto.setText(str(terremotoNumMuertosMayor.getNumeroMuertos))

    def buscarTerremotoConMenorNumeroDeMuertos(self):
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()
        tempNumMenor = terremotos[0].getNumeroMuertos
        terremotoNumMuertosMenor = terremotos[0]

        for terremoto in terremotos:
            if tempNumMenor > terremoto.getNumeroMuertos:
                tempNumMenor = terremoto.getNumeroMuertos
                terremotoNumMuertosMenor = terremoto

        self.ventanaBuscarTerremoto.txtNombreTerremoto.setText(terremotoNumMuertosMenor.getNombre)
        self.ventanaBuscarTerremoto.txtFechaTerremoto.setText(terremotoNumMuertosMenor.getFecha)
        self.ventanaBuscarTerremoto.txtMagnitudTerremoto.setText(str(terremotoNumMuertosMenor.getMagnitud))
        self.ventanaBuscarTerremoto.txtDepartamentoTerremoto.setText(terremotoNumMuertosMenor.getDepartamento)
        self.ventanaBuscarTerremoto.txtNumeroMuertosTerremoto.setText(str(terremotoNumMuertosMenor.getNumeroMuertos))

    def buscarTerremotoConMenorMagnitud(self):
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()
        tempMenorMagnitud = terremotos[0].getMagnitud
        terremotoMenorMagnitud = terremotos[0]

        for terremoto in terremotos:
            if tempMenorMagnitud > terremoto.getMagnitud:
                tempMenorMagnitud = terremoto.getMagnitud
                terremotoMenorMagnitud = terremoto

        self.ventanaBuscarTerremoto.txtNombreTerremoto.setText(terremotoMenorMagnitud.getNombre)
        self.ventanaBuscarTerremoto.txtFechaTerremoto.setText(terremotoMenorMagnitud.getFecha)
        self.ventanaBuscarTerremoto.txtMagnitudTerremoto.setText(str(terremotoMenorMagnitud.getMagnitud))
        self.ventanaBuscarTerremoto.txtDepartamentoTerremoto.setText(terremotoMenorMagnitud.getDepartamento)
        self.ventanaBuscarTerremoto.txtNumeroMuertosTerremoto.setText(str(terremotoMenorMagnitud.getNumeroMuertos))

    def buscarTerremotoConMayorMagnitud(self):
        terremotos = InformacionTerremotos.seleccionarTodosLosTerremotosObj()
        tempMayorMagnitud = terremotos[0].getMagnitud
        terremotoMayorMagnitud = terremotos[0]

        for terremoto in terremotos:
            if tempMayorMagnitud < terremoto.getMagnitud:
                tempMayorMagnitud = terremoto.getMagnitud
                terremotoMayorMagnitud = terremoto

        self.ventanaBuscarTerremoto.txtNombreTerremoto.setText(terremotoMayorMagnitud.getNombre)
        self.ventanaBuscarTerremoto.txtFechaTerremoto.setText(terremotoMayorMagnitud.getFecha)
        self.ventanaBuscarTerremoto.txtMagnitudTerremoto.setText(str(terremotoMayorMagnitud.getMagnitud))
        self.ventanaBuscarTerremoto.txtDepartamentoTerremoto.setText(terremotoMayorMagnitud.getDepartamento)
        self.ventanaBuscarTerremoto.txtNumeroMuertosTerremoto.setText(str(terremotoMayorMagnitud.getNumeroMuertos))

    def ordenarTablaInformacion(self, arreglo):
        datos = arreglo
        locale.setlocale(locale.LC_ALL, '')

        self.tablaInformacion.clearContents()
        self.tablaInformacion.setRowCount(0)

        for fila, terremoto in enumerate(datos):

            self.tablaInformacion.insertRow(fila)
            self.tablaInformacion.setRowHeight(fila, 30)

            self.tablaInformacion.setItem(fila, 0, QTableWidgetItem(terremoto.getNombre))
            self.tablaInformacion.item(fila, 0).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.tablaInformacion.item(fila, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.tablaInformacion.setItem(fila, 1, QTableWidgetItem(terremoto.getFecha))
            self.tablaInformacion.item(fila, 1).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.tablaInformacion.item(fila, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.tablaInformacion.setItem(fila, 2, QTableWidgetItem(str(terremoto.getMagnitud)))
            self.tablaInformacion.item(fila, 2).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.tablaInformacion.item(fila, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.tablaInformacion.setItem(fila, 3, QTableWidgetItem(terremoto.getDepartamento))
            self.tablaInformacion.item(fila, 3).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.tablaInformacion.item(fila, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.tablaInformacion.setItem(fila, 4, QTableWidgetItem(str(terremoto.getNumeroMuertos)))
            self.tablaInformacion.item(fila, 4).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.tablaInformacion.item(fila, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def abrirVentanaRegistro(self):
        if self.ventanaRegistrarTerremoto.isVisible():
            self.ventanaRegistrarTerremoto.close()
        else:
            self.ventanaRegistrarTerremoto.show()

    def abrirVentanaBuscar(self):
        if self.ventanaBuscarTerremoto.isVisible():
            self.ventanaBuscarTerremoto.close()
        else:
            self.ventanaBuscarTerremoto.show()

    def closeEvent(self, event) -> None:
        ventanas = [
            self.ventanaRegistrarTerremoto,
            self.ventanaBuscarTerremoto
        ]
        for ventana in ventanas:
            if ventana.isVisible():
                ventana.close()


if __name__ == '__main__':
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
