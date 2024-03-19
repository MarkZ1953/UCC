import locale

from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QIcon, QFont, QBrush, QColor
from PySide6.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QVBoxLayout, QLineEdit, \
    QSizePolicy, QApplication, QLabel, QHBoxLayout, QTableWidget, QHeaderView, QTableWidgetItem
import math
from matplotlib import pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()

        self.datosOperacion = {}
        self.historialOperaciones = {}
        self.contadorHistorialOperaciones = 0

        self.contadorPeticiones = 0
        self.botones = {}
        self.grid_layout = None
        self.entrada_texto = None
        self.resize(500, 500)
        self.operaciones = {}
        # self.setWindowIcon(QIcon(QPixmap("Imagenes/calculator-gray.png")))

        self.setWindowTitle("Calculadora")
        # self.setFixedSize(235, 270)

        self.tablaResultados = TablaResultados()

        # Creamos un layout principal
        self.layout_principal = QVBoxLayout()
        self.layoutCalculadora = QVBoxLayout()
        self.layoutTabla = QVBoxLayout()
        self.layoutTabla.addWidget(self.tablaResultados)

        #self.layout_principal.addLayout(self.layoutCalculadora)
        self.layout_principal.addLayout(self.layoutCalculadora)
        self.layout_principal.addLayout(self.layoutTabla)

        # Llamamos al metodo que crea la entrada de texto
        self.crearEntradaDeTexto()

        # Creamos los botonesMenuInquilinos
        self.crearBotones()

        # Agregamos el QGridLayout al layout principal
        self.layoutCalculadora.addWidget(self.peticiones)
        self.layoutCalculadora.addWidget(self.entrada_texto)
        self.layoutCalculadora.addLayout(self.grid_layout)

        # canvas = FigureCanvas(plt.figure())
        # self.layout_principal.addWidget(canvas)

        # Dibujar ecuación en la figura
        # ax = canvas.figure.add_subplot(111)
        # ax.text(0.5, 0.5, r'$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$', fontsize=20, ha='center')
        # ax.axis('off')

        # Creamos un componente QWidget txtPara alojar al layout principal
        self.componente_general = QWidget(self)
        self.componente_general.setLayout(self.layout_principal)

        # Publicamos el componente general
        self.setCentralWidget(self.componente_general)

    def crearEntradaDeTexto(self):
        # Peticiones que se le haran al usuario
        self.peticiones = QLabel()
        self.peticiones.setFixedHeight(30)
        self.peticiones.setText("Ingrese la funcion: ")

        # Creamos la entrada de texto
        self.entrada_texto: QLineEdit = QLineEdit()

        # Modificamos algunas propiedades
        self.entrada_texto.setMinimumHeight(100)
        self.entrada_texto.setReadOnly(True)
        self.entrada_texto.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.entrada_texto.setAlignment(Qt.AlignmentFlag.AlignRight)

    def crearBotones(self):
        # Creamos el grid layout donde estan estaran los botonesMenuInquilinos
        self.grid_layout = QGridLayout()

        botones = {
            "(": (0, 0),
            ")": (0, 1),
            "C": (0, 2),
            "\u232B": (0, 3),
            "/": (1, 3),
            "sen": (1, 0),
            "cos": (1, 1),
            "tan": (1, 2),
            "7": (2, 0),
            "8": (2, 1),
            "9": (2, 2),
            "*": (2, 3),
            "4": (3, 0),
            "5": (3, 1),
            "6": (3, 2),
            "-": (3, 3),
            "1": (4, 0),
            "2": (4, 1),
            "3": (4, 2),
            "+": (4, 3),
            "0": (5, 0),
            ".": (5, 2),
            "=": (5, 3),
            "X": (6, 0),
            "e": (6, 1),
            "pi": (6, 2)
        }

        for texto_boton, posicion in botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton)
            self.botones[texto_boton].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.botones[texto_boton].setMinimumSize(40, 40)
            self.botones[texto_boton].pressed.connect(lambda k=texto_boton: self.botonPulsado(k))

            if texto_boton == "C":
                self.botones[texto_boton].setShortcut(Qt.Key.Key_Delete)
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1])
            elif texto_boton == "\u232B":
                self.botones[texto_boton].setShortcut(Qt.Key.Key_Backspace)
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1])
            elif texto_boton == "0":
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1], 1, 2)
            elif texto_boton == "=":
                self.botones[texto_boton].setShortcut(Qt.Key.Key_Return)
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1])
            else:
                self.grid_layout.addWidget(self.botones[texto_boton], posicion[0], posicion[1])

    def keyPressEvent(self, event) -> None:

        # print(f"Se presiono la Key : {event.key()}")

        permitidos = [Qt.Key.Key_1,
                      Qt.Key.Key_2,
                      Qt.Key.Key_3,
                      Qt.Key.Key_4,
                      Qt.Key.Key_5,
                      Qt.Key.Key_6,
                      Qt.Key.Key_7,
                      Qt.Key.Key_8,
                      Qt.Key.Key_9,
                      Qt.Key.Key_0,
                      Qt.Key.Key_Slash,
                      Qt.Key.Key_Minus,
                      Qt.Key.Key_Plus,
                      Qt.Key.Key_Asterisk]

        if event.key() == Qt.Key.Key_Return and (self.entrada_texto.text() != ""):
            self.botonPulsado("=")

        if self.entrada_texto.text() == "\u232B":
            self.eliminarUltimoCaracter()

        if event.key() in permitidos:
            if self.entrada_texto.text() in ["Ocurrio un Error", "No puedes Dividir por Cero"]:
                self.entrada_texto.clear()
                self.entrada_texto.insert(str(event.text()))
            else:
                self.entrada_texto.insert(str(event.text()))

    def botonPulsado(self, texto_boton):

        peticiones = {
            0: "Ingrese la funcion",
            1: "Ingrese la cantidad de iteraciones",
            2: "Ingrese el valor de A",
            3: "Ingrese el valor de B",
            4: "Ingrese el error porcentual al que desea llegar"
        }

    #try:
        if texto_boton == "C":
            self.entrada_texto.clear()
        elif texto_boton == "=":
            if self.contadorPeticiones < 4:

                self.contadorPeticiones += 1

                self.peticiones.setText(peticiones[self.contadorPeticiones])

                # Guardamos los datos que se van pidiendo en la calculadora
                self.datosOperacion.update({self.contadorPeticiones - 1: self.entrada_texto.text()})

                print(self.datosOperacion)

                self.entrada_texto.clear()
            else:
                print(self.datosOperacion)
                # Cuando termina de pedir todos los datos, entonces hace la operacion
                # resultado = str(eval(self.entrada_texto.text()))
                self.entrada_texto.clear()
                self.contadorHistorialOperaciones += 1
                self.historialOperaciones.update({self.contadorHistorialOperaciones: self.datosOperacion})
                resultado = self.retornarResultadoOperacion(self.datosOperacion)
                self.entrada_texto.insert(resultado)
                contador = 0
        elif texto_boton == "\u232B":
            self.eliminarUltimoCaracter()
        else:
            if self.entrada_texto.text() in ["Ocurrio un Error", "No puedes Dividir por Cero"]:
                self.entrada_texto.clear()
                self.entrada_texto.insert(texto_boton)
            else:
                self.entrada_texto.insert(texto_boton)
    #except ZeroDivisionError:
        #self.entrada_texto.clear()
        #self.entrada_texto.insert("No puedes Dividir por Cero")
    #except Exception as e:
       ##  self.entrada_texto.clear()
       # self.entrada_texto.insert(f"Ocurrio un Error: {e}")

    def eliminarUltimoCaracter(self):
        texto = self.entrada_texto.text()
        self.entrada_texto.clear()
        self.entrada_texto.insert(texto[:-1])

    def retornarResultadoOperacion(self, datosOperacion: dict):
        operacion: str = datosOperacion[0]

        operacion = (operacion.replace("sen", "math.sin")
                     .replace("tan", "math.tan")
                     .replace("cos", "math.cos")
                     .replace("e", "math.e"))

        # Metodo de Biseccion
        iteraciones: int = int(datosOperacion[1])
        a: float = float(datosOperacion[2])
        b: float = float(datosOperacion[3])
        fafc = ""
        fbfc = ""
        ea: float = 100

        cActual: float = 0

        # Datos de ejemplo

        # 5*x**3-5*x**2+6*x-2
        # x**4+3*x**3-2
        contadorResultados = 0
        data = []
        resultados = {}

        for i in range(iteraciones):
            data = []
            cAnterior = cActual

            # Calculamos f(a)
            fa = eval(operacion.replace("X", f"({a})"))

            # Calculamos f(b)
            fb = eval(operacion.replace("X", f"({b})"))

            # Calculamos ci
            cActual = b - (fb * (a - b)) / (fa - fb)

            # Calculamos f(ci)
            fc = eval(operacion.replace("X", f"({cActual})"))

            # Calculamos Ea

            # Ea = (a-c)/a * 100
            data.append(str(a))
            data.append(str(b))
            data.append(str(cActual))
            data.append(str(fa))
            data.append(str(fb))
            data.append(str(fc))

            # Hallamos f(a) * f(ci)

            if fa * fc < 0:
                b = cActual
                fafc = "-"
                fbfc = "+"

            # Hallamos f(ci) * f(b)

            if fb * fc < 0:
                a = cActual
                fbfc = "-"
                fafc = "+"

            try:
                ea = abs((cAnterior - cActual) / cActual * 100)
            except Exception as e:
                pass

            data.append(fafc.ljust(1))
            data.append(fbfc.ljust(1))
            data.append(f"{ea} %")

            resultados.update({contadorResultados: data})
            contadorResultados += 1

        self.tablaResultados.actualizarTablaReservas(resultados)


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

    def actualizarTablaReservas(self, resultadosOperacion):

        locale.setlocale(locale.LC_ALL, 'es_CO.utf8')

        print(resultadosOperacion)

        for iteracion, resultado in resultadosOperacion.items():

            print(f"Iteracion: {iteracion}")
            print(resultado)
            self.insertRow(iteracion)
            self.setRowHeight(iteracion, 30)

            # Iteraciones
            self.setItem(iteracion, 0, QTableWidgetItem(str(iteracion+1)))
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

            print(resultado[7])
            # fb * fc
            self.setItem(iteracion, 8, QTableWidgetItem(str(resultado[7])))
            self.item(iteracion, 8).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 8).setFlags(~Qt.ItemFlag.ItemIsEditable)

            # ea
            self.setItem(iteracion, 9, QTableWidgetItem(str(resultado[8])))
            self.item(iteracion, 9).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.item(iteracion, 9).setFlags(~Qt.ItemFlag.ItemIsEditable)

            #if reserva.estadoR == "Pendiente":
              #  self.setItem(fila, 9, QTableWidgetItem(reserva.estadoR))
             #   self.item(fila, 9).setTextAlignment(Qt.AlignmentFlag.AlignCenter)
               # self.item(fila, 9).setBackground(QBrush(QColor("yellow")))
               # self.item(fila, 9).setForeground(QBrush(Qt.GlobalColor.black))
              #  self.item(fila, 9).setFlags(~Qt.ItemFlag.ItemIsEditable)
            #elif reserva.estadoR == "Pagado":
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



if __name__ == '__main__':
    app = QApplication([])
    ventana = Calculadora()
    ventana.show()
    app.exec()
