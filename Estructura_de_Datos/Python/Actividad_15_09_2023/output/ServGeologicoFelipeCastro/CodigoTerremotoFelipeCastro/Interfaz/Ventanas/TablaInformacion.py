import locale

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView

from Base_de_Datos.TerremotosDB import InformacionTerremotos
from Interfaz.VentanaDetalles.DetalleTerremoto import DetalleTerremoto


class TablaInformacion(QTableWidget):
    def __init__(self):
        super().__init__()

        cabezeras = ["Id", "Nombre", "Fecha", "Magnitud", "Departamento", "No.Muertos Aprox"]
        self.setColumnCount(len(cabezeras))
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Darle nombres a las cabeceras de la tabla
        self.setHorizontalHeaderLabels(cabezeras)

        # Llamamos al metodo txtPara poder ingresarle los valores de la base de datos a la tabla
        self.actualizarTablaInformacion()

        self.detalleTerremoto = DetalleTerremoto()

        self.cellClicked.connect(self.celdaSeleccionada)

        # Ajustar tamaño de columnas y filas
        self.resizeColumnsToContents()

    def actualizarTablaInformacion(self):

        datos = InformacionTerremotos.seleccionarTodosLosTerremotos()
        locale.setlocale(locale.LC_ALL, '')

        for fila, (idTerremoto, nombreTerremoto, fechaTerremoto, magnitudTerremoto, departamentoTerremoto,
                   noMuertosTerremoto) in enumerate(datos):

            self.insertRow(fila)
            self.setRowHeight(fila, 30)

            self.setItem(fila, 0, QTableWidgetItem(str(idTerremoto)))
            self.item(fila, 0).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 1, QTableWidgetItem(nombreTerremoto))
            self.item(fila, 1).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 2, QTableWidgetItem(fechaTerremoto))
            self.item(fila, 2).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 3, QTableWidgetItem(str(magnitudTerremoto)))
            self.item(fila, 3).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 4, QTableWidgetItem(departamentoTerremoto))
            self.item(fila, 4).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 5, QTableWidgetItem(str(noMuertosTerremoto)))
            self.item(fila, 5).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 5).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def celdaSeleccionada(self, row, column):
        nombreTerremoto = self.item(row, 1)
        fechaTerremoto = self.item(row, 2)
        magnitudTerremoto = self.item(row, 3)
        departamentoTerremoto = self.item(row, 4)
        noMuertosTerremoto = self.item(row, 5)

        if not self.detalleTerremoto.isVisible():
            self.detalleTerremoto.txtNombreTerremoto.setText(nombreTerremoto.text())
            self.detalleTerremoto.txtMagnitudTerremoto.setText(magnitudTerremoto.text())
            self.detalleTerremoto.txtFechaTerremoto.setText(fechaTerremoto.text())
            self.detalleTerremoto.txtNumeroMuertosTerremoto.setText(noMuertosTerremoto.text())
            self.detalleTerremoto.txtDepartamentoTerremoto.setText(departamentoTerremoto.text())
            self.detalleTerremoto.show()
        else:
            self.detalleTerremoto.raise_()
