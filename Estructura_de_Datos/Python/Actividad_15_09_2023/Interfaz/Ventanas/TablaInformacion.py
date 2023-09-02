import locale

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView

from Base_de_Datos.TerremotosDB import InformacionTerremotos


class TablaInformacion(QTableWidget):
    def __init__(self):
        super().__init__()

        cabezeras = ["Id Terremoto", "Ciudad", "Fecha", "Magnitud", "Departamento", "No.Muertos Aprox"]
        self.setColumnCount(len(cabezeras))
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Darle nombres a las cabeceras de la tabla
        self.setHorizontalHeaderLabels(cabezeras)

        # Llamamos al metodo txtPara poder ingresarle los valores de la base de datos a la tabla
        self.actualizarTablaInquilinos()

        # self.cellClicked.connect(self.celdaSeleccionada)

        # Ajustar tamaño de columnas y filas
        self.resizeColumnsToContents()

    def actualizarTablaInquilinos(self):

        datos = InformacionTerremotos.seleccionarTodosLosTerremotos()
        locale.setlocale(locale.LC_ALL, '')

        for fila, (idTerremoto, cedula, nombres, apellidos, telefono, correo) in enumerate(datos):

            self.insertRow(fila)
            self.setRowHeight(fila, 30)

            self.setItem(fila, 0, QTableWidgetItem(locale.format_string('%d', idTerremoto, grouping=True)))
            self.item(fila, 0).setFlags(~Qt.ItemFlag.ItemIsEditable)
            # self.item(fila, 0).setForeground(QBrush(QColor("blue")))
            self.item(fila, 0).setFont(QFont("Roboto", 10, QFont.Bold))
            self.item(fila, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 1, QTableWidgetItem(cedula))
            self.item(fila, 1).setFlags(~Qt.ItemFlag.ItemIsEditable)
            # self.item(fila, 0).setForeground(QBrush(QColor("blue")))
            self.item(fila, 1).setFont(QFont("Roboto", 10, QFont.Bold))
            self.item(fila, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 2, QTableWidgetItem(nombres))
            self.item(fila, 2).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 3, QTableWidgetItem(str(apellidos)))
            self.item(fila, 3).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 4, QTableWidgetItem(str(telefono)))
            self.item(fila, 4).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

            self.setItem(fila, 5, QTableWidgetItem(str(correo)))
            self.item(fila, 5).setFlags(~Qt.ItemFlag.ItemIsEditable)
            self.item(fila, 5).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

    def celdaSeleccionada(self, row, column):
        if column == 0:
            id_persona = self.item(row, column)

            if not self.detalleInquilino.isVisible():
                self.detalleInquilino.show()
            else:
                self.detalleInquilino.raise_()

            self.detalleInquilino.frame_persona.cambiarValores(id_persona.text().replace(".", ""))
