import locale

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView

from Base_de_Datos.TerremotosDB import InformacionTerremotos


class TablaInformacion(QTableWidget):
    def __init__(self):
        super().__init__()

        cabezeras = ["Nombre", "Fecha", "Magnitud", "Departamento", "No.Muertos Aprox"]
        self.setColumnCount(len(cabezeras))
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Darle nombres a las cabeceras de la tabla
        self.setHorizontalHeaderLabels(cabezeras)

        # Llamamos al metodo txtPara poder ingresarle los valores de la base de datos a la tabla
        self.actualizarTablaInformacion()

        # self.cellClicked.connect(self.celdaSeleccionada)

        # Ajustar tamaño de columnas y filas
        self.resizeColumnsToContents()

    def actualizarTablaInformacion(self):

        datos = InformacionTerremotos.seleccionarTodosLosTerremotos()
        locale.setlocale(locale.LC_ALL, '')

        for fila, (nombreTerremoto, fechaTerremoto, magnitudTerremoto, departamentoTerremoto,
                   noMuertosTerremoto) in enumerate(datos):

            self.insertRow(fila)
            self.setRowHeight(fila, 30)

            self.setItem(fila, 0, QTableWidgetItem(nombreTerremoto))
            self.item(fila, 0).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 1, QTableWidgetItem(fechaTerremoto))
            self.item(fila, 1).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 2, QTableWidgetItem(str(magnitudTerremoto)))
            self.item(fila, 2).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 3, QTableWidgetItem(departamentoTerremoto))
            self.item(fila, 3).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 4, QTableWidgetItem(str(noMuertosTerremoto)))
            self.item(fila, 4).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def celdaSeleccionada(self, row, column):
        if column == 0:
            id_persona = self.item(row, column)

            if not self.detalleInquilino.isVisible():
                self.detalleInquilino.show()
            else:
                self.detalleInquilino.raise_()

            self.detalleInquilino.frame_persona.cambiarValores(id_persona.text().replace(".", ""))
