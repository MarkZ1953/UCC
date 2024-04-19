import locale

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem


class TablaResultados(QTableWidget):
    def __init__(self):
        super().__init__()

        # La tabla se expande horizontalmente
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Se crea un evento txtPara cuando se presione el la columna y pueda detectar el click del mouse
        # self.cellClicked.connect(self.confirmar)

        # Ajustar tamaño de columnas y filas
        self.resizeColumnsToContents()

    def crearItem(self, row: int, column: int, value, editable: bool = True):
        self.setItem(row, column, QTableWidgetItem(value))
        self.item(row, column).setTextAlignment(Qt.AlignmentFlag.AlignCenter)

        # Cambiar el estado de la celda para que no sea editable
        if not editable:
            self.item(row, column).setFlags(~Qt.ItemFlag.ItemIsEditable)

    def actualizarTablaResultados(self, resultadosOperacion: dict, cabezeras: list):
        locale.setlocale(locale.LC_ALL, 'es_CO.utf8')

        columnsLength = len(cabezeras)

        # Se asignan la cantidad de columnas que va a tener la tabla
        self.setColumnCount(columnsLength)

        # Darle nombres a las cabeceras de la tabla
        self.setHorizontalHeaderLabels(cabezeras)

        for iteracion, resultado in resultadosOperacion.items():
            self.insertRow(iteracion)
            self.setRowHeight(iteracion, 30)
            
            for column in range(columnsLength):
                if column == 0:
                    self.crearItem(row=iteracion, column=column, value=str(iteracion + 1), editable=False)
                else:
                    print(resultado[column - 1])
                    self.crearItem(row=iteracion, column=column, value=str(resultado[column - 1]), editable=False)

            # if reserva.estadoR == "Pendiente":
            #  self.setItem(fila, 9, QTableWidgetItem(reserva.estadoR))
            #   self.item(fila, 9).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            # self.item(fila, 9).setBackground(QBrush(QColor("yellow")))
            # self.item(fila, 9).setForeground(QBrush(Qt.GlobalColor.black))
            #  self.item(fila, 9).setFlags(~Qt.ItemFlag.ItemIsEditable)
            # elif reserva.estadoR == "Pagado":
            ## self.item(fila, 9).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            #  self.item(fila, 9).setBackground(QBrush(QColor("green")))
            #  self.item(fila, 9).setForeground(QBrush(Qt.GlobalColor.white))
            # self.item(fila, 9).setFlags(~Qt.ItemFlag.ItemIsEditable)

    # def confirmar(self, fila, columna):
    #     if columna == 0:
    #         idInquilino = self.item(fila, columna)
    #
    #         if not self.ventanaDetalleInquilino.isVisible():
    #             self.ventanaDetalleInquilino.show()
    #         else:
    #             self.ventanaDetalleInquilino.raise_()
    #
    #         self.ventanaDetalleInquilino.frame_persona.cambiarValores(idInquilino.text().replace(".", ""))
    #
    #     elif columna == 1:
    #
    #         idPago = self.item(fila, columna)
    #
    #         if not self.ventanaDetallePago.isVisible():
    #             self.ventanaDetallePago.show()
    #         else:
    #             self.ventanaDetallePago.raise_()
    #
    #         self.ventanaDetallePago.frame_pago.cambiarValores(idPago.text())
