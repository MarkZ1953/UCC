import locale

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QTableWidget, QHeaderView, QTableWidgetItem


class TablaResultados(QTableWidget):
    def __init__(self):
        super().__init__()

        # Cabeceras de la tabla
        self.cabezeras = ["Iteracion", "a", "b", "c", "f(a)", "f(b)", "f(ci)", "f(a) * f(ci)", "f(b) * f(ci)", "Ea (%)"]

        # Se asignan la cantidad de columnas que va a tener la tabla
        self.setColumnCount(len(self.cabezeras))

        # La tabla se expande horizontalmente
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # Darle nombres a las cabeceras de la tabla
        self.setHorizontalHeaderLabels(self.cabezeras)

        # Se crea un evento txtPara cuando se presione el la columna y pueda detectar el click del mouse
        self.cellClicked.connect(self.confirmar)

        # Ajustar tamaño de columnas y filas
        self.resizeColumnsToContents()

    def actualizarTablaResultados(self, resultadosOperacion):
        locale.setlocale(locale.LC_ALL, 'es_CO.utf8')

        for iteracion, resultado in resultadosOperacion.items():
            self.insertRow(iteracion)
            self.setRowHeight(iteracion, 30)

            # Iteraciones
            self.setItem(iteracion, 0, QTableWidgetItem(str(iteracion + 1)))
            self.item(iteracion, 0).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 0).setFont(QFont("Arial", 10, QFont.Bold))
            self.item(iteracion, 0).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # a
            self.setItem(iteracion, 1, QTableWidgetItem(str(resultado[0])))
            self.item(iteracion, 1).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 1).setFont(QFont("Arial", 10, QFont.Bold))
            self.item(iteracion, 1).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # b
            self.setItem(iteracion, 2, QTableWidgetItem(str(resultado[1])))
            self.item(iteracion, 2).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 2).setFont(QFont("Arial", 10, QFont.Bold))
            self.item(iteracion, 2).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # c
            self.setItem(iteracion, 3, QTableWidgetItem(str(resultado[2])))
            self.item(iteracion, 3).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 3).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # f(a)
            self.setItem(iteracion, 4, QTableWidgetItem(str(resultado[3])))
            self.item(iteracion, 4).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 4).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # f(b)
            self.setItem(iteracion, 5, QTableWidgetItem(str(resultado[4])))
            self.item(iteracion, 5).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 5).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # f(c)
            self.setItem(iteracion, 6, QTableWidgetItem(str(resultado[5])))
            self.item(iteracion, 6).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 6).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # fa * fc
            self.setItem(iteracion, 7, QTableWidgetItem(str(resultado[6])))
            self.item(iteracion, 7).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 7).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # fb * fc
            self.setItem(iteracion, 8, QTableWidgetItem(str(resultado[7])))
            self.item(iteracion, 8).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 8).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # ea
            self.setItem(iteracion, 9, QTableWidgetItem(str(resultado[8])))
            self.item(iteracion, 9).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 9).setFlags(~Qt.ItemFlag.ItemIsEditable)

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

    def confirmar(self, fila, columna):
        if columna == 0:
            idInquilino = self.item(fila, columna)

            if not self.ventanaDetalleInquilino.isVisible():
                self.ventanaDetalleInquilino.show()
            else:
                self.ventanaDetalleInquilino.raise_()

            self.ventanaDetalleInquilino.frame_persona.cambiarValores(idInquilino.text().replace(".", ""))

        elif columna == 1:

            idPago = self.item(fila, columna)

            if not self.ventanaDetallePago.isVisible():
                self.ventanaDetallePago.show()
            else:
                self.ventanaDetallePago.raise_()

            self.ventanaDetallePago.frame_pago.cambiarValores(idPago.text())