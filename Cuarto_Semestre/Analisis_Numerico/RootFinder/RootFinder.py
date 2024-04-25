from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QVBoxLayout, QLineEdit, \
    QSizePolicy, QApplication, QLabel, QHBoxLayout, QComboBox, QFormLayout, QMessageBox, QFrame

from Componentes.VentanaResultados import VentanaResultados
from Excepciones.Excepciones import LlenarCamposVaciosException
from Metodos.Biseccion import MetodoBiseccion
from Componentes.TablaResultados import TablaResultados
from Metodos.FalsaPosicion import MetodoFalsaPosicion
from Metodos.Secante import MetodoSecante
from Utiles import Etiqueta


class RootFinder(QMainWindow):
    def __init__(self):
        super().__init__()

        self.datosOperacion = {}
        self.cajas = {}
        self.historialOperaciones = {}
        self.contadorHistorialOperaciones = 0

        self.setContentsMargins(10, 10, 10, 10)

        self.contadorPeticiones = 0
        self.botones = {}
        self.grid_layout = None
        self.entrada_texto = None
        # self.resize(800, 600)
        self.setFixedSize(650, 750)
        self.operaciones = {}

        self.setWindowTitle("RootFinder")
        # self.setFixedSize(235, 270)

        self.ventanaResultados = VentanaResultados()

        # Creamos un layout principal
        self.layout_principal = QVBoxLayout()

        self.__crearAreaTitulo()

        self.layoutOpciones = QHBoxLayout()

        self.layoutCalculadora = QVBoxLayout()
        self.layoutTabla = QVBoxLayout()

        self.layout_principal.addLayout(self.layoutCalculadora)
        self.layout_principal.addLayout(self.layoutTabla)

        self.layoutCajas = QGridLayout()

        # Creamos las cajas que recolectan la información
        self.crearCajas()

        # Creamos los botones
        self.crearBotones()

        # Agregamos el QGridLayout al layout principal
        self.layoutCalculadora.addLayout(self.layoutCajas)
        self.layoutCalculadora.addLayout(self.grid_layout)

        # canvas = FigureCanvas(plt.figure())
        # self.layout_principal.addWidget(canvas)

        # Dibujar ecuación en la figura
        # ax = canvas.figure.add_subplot(111)
        # ax.text(0.5, 0.5, r'$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$', fontsize=20, ha='center')
        # ax.axis('off')

        # Creamos un componente QWidget txtPara alojar al layout principal
        self.componentesGeneral = QWidget(self)
        self.componentesGeneral.setLayout(self.layout_principal)

        frameTitulo = QFrame()
        frameTitulo.setFixedHeight(40)
        frameTitulo.setStyleSheet("background-color: rgb(14, 49, 129);")

        layoutTitulo = QHBoxLayout()
        frameTitulo.setLayout(layoutTitulo)

        self.layout_principal.addWidget(frameTitulo)

        # Publicamos el componente general
        self.setCentralWidget(self.componentesGeneral)

    @staticmethod
    def verificarCamposCompletos(cajas: list):
        for caja in cajas:
            if caja == "":
                raise LlenarCamposVaciosException("Tienes que completar los campos necesarios")

    def crearCajas(self):

        layoutIzquierda = QFormLayout()
        layoutIzquierda.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutIzquierda.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)

        layoutDerecha = QFormLayout()
        layoutDerecha.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layoutDerecha.setLabelAlignment(Qt.AlignmentFlag.AlignCenter)

        # Creamos la entrada de texto
        self.entrada_texto: QLineEdit = QLineEdit()
        self.entrada_texto.setFixedHeight(50)
        self.entrada_texto.setReadOnly(True)
        self.entrada_texto.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.entrada_texto.setAlignment(Qt.AlignmentFlag.AlignRight)
        layoutIzquierda.addRow(QLabelCustom("Funcion"), self.entrada_texto)

        self.leA = QLineEdit()
        self.leA.setFixedHeight(50)
        layoutIzquierda.addRow(QLabelCustom("A"), self.leA)

        self.eA = QLineEdit()
        self.eA.setFixedHeight(50)
        layoutIzquierda.addRow(QLabelCustom("Ea"), self.eA)

        self.leIteraciones = QLineEdit()
        self.leIteraciones.setFixedHeight(50)
        layoutDerecha.addRow(QLabelCustom("Iteraciones"), self.leIteraciones)

        self.leB = QLineEdit()
        self.leB.setFixedHeight(50)
        layoutDerecha.addRow(QLabelCustom("B"), self.leB)

        self.cbMetodo = QComboBox()
        self.cbMetodo.setFixedHeight(50)
        self.cbMetodo.addItem("Biseccion", 0)
        self.cbMetodo.addItem("Falsa Posicion", 1)
        self.cbMetodo.addItem("Secante", 2)
        layoutDerecha.addRow(QLabelCustom("Metodo"), self.cbMetodo)

        self.layoutCajas.addLayout(layoutIzquierda, 0, 0)
        self.layoutCajas.addLayout(layoutDerecha, 0, 1)

    # for caja, posicion in self.cajas.items():
    #     self.layoutCajas.addWidget(caja, posicion[0], posicion[1], posicion[2], posicion[3])

    def __crearAreaTitulo(self):

        frameTitulo = QFrame()
        frameTitulo.setFixedHeight(80)
        frameTitulo.setStyleSheet("background-color: rgb(14, 49, 129);")

        layoutTitulo = QHBoxLayout()
        frameTitulo.setLayout(layoutTitulo)

        titulo = Etiqueta(texto="RootFinder", bold=True, font="Arial", font_size=16)
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setStyleSheet("color: white;")
        layoutTitulo.addWidget(titulo)

        self.layout_principal.addWidget(frameTitulo)

    def crearBotones(self):
        # Creamos el grid layout donde están estarán los botonesMenuInquilinos
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
            "pi": (6, 2),
            "^": (6, 3)
        }

        for texto_boton, posicion in botones.items():
            self.botones[texto_boton] = QPushButton(texto_boton)
            self.botones[texto_boton].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.botones[texto_boton].setMinimumSize(40, 50)
            self.botones[texto_boton].pressed.connect(lambda k=texto_boton: self.botonPulsado(k))
            # self.botones[texto_boton].setStyleSheet("QPushButton { border-radius: 10px;}")

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
                      Qt.Key.Key_X,
                      Qt.Key.Key_AsciiCircum,
                      Qt.Key.Key_Period,
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

    def botonPulsado(self, textoBoton: str):
        # try:
        if textoBoton == "C":
            self.limpiarCajas()
        elif textoBoton == "=":
            if self.leIteraciones.text() and self.eA.text():
                QMessageBox.critical(self, "Error",
                                     f"Ha ingresado las iteraciones y el error Absoluto, "
                                     f"porfavor solo ingrese los datos de alguno de estas dos variables",
                                     QMessageBox.StandardButton.Ok, QMessageBox.StandardButton.Ok)
            else:
                # Guardamos los datos que se van pidiendo en la calculadora
                self.datosOperacion.update(
                    {
                        0: self.entrada_texto.text(),
                        1: self.leIteraciones.text(),
                        2: self.leA.text(),
                        3: self.leB.text(),
                        4: self.eA.text()
                    }
                )
                self.ventanaResultados.show()
                #

                self.retornarResultadoOperacion(self.datosOperacion)

                #

                self.contadorHistorialOperaciones += 1

                # Guardamos la infomacion de la calculadora al historial
                self.historialOperaciones.update({self.contadorHistorialOperaciones: self.datosOperacion})
        elif textoBoton == "\u232B":
            self.eliminarUltimoCaracter()
        else:
            if self.entrada_texto.text() in ["Ocurrio un Error", "No puedes dividir por cero"]:
                self.entrada_texto.clear()
                self.entrada_texto.insert(textoBoton)
            else:
                self.entrada_texto.insert(textoBoton)

        # except LlenarCamposVaciosException as e:
        #     QMessageBox.critical(self, "Error", f"{e}", QMessageBox.StandardButton.Ok,
        #                          QMessageBox.StandardButton.Ok)
        # except Exception as e:
        #     QMessageBox.critical(self, "Error", f"{e}", QMessageBox.StandardButton.Ok,
        #                          QMessageBox.StandardButton.Ok)

    # except ZeroDivisionError:
    # self.entrada_texto.clear()
    # self.entrada_texto.insert("No puedes Dividir por Cero")
    # except Exception as e:
    # self.entrada_texto.clear()
    # self.entrada_texto.insert(f"Ocurrio un Error: {e}")

    def eliminarUltimoCaracter(self):
        texto = self.entrada_texto.text()
        self.entrada_texto.clear()
        self.entrada_texto.insert(texto[:-1])

    def limpiarCajas(self):
        self.entrada_texto.clear()
        self.leIteraciones.clear()
        self.eA.clear()
        self.leA.clear()
        self.leB.clear()

    def retornarResultadoOperacion(self, datosOperacion: dict):
        operacion: str = datosOperacion[0]

        operacion = (operacion.replace("sen", "math.sin")
                     .replace("tan", "math.tan")
                     .replace("cos", "math.cos")
                     .replace("e", "math.e")
                     .replace("^", "**"))

        iteraciones = datosOperacion[1]
        a: float = float(datosOperacion[2])
        b: float = float(datosOperacion[3])
        eaRequerido = datosOperacion[4]

        # Obtenemos el ID del metodo seleccionado
        idMetodoSeleccionado: int = self.cbMetodo.currentData()

        # Creamos una variable para almacenar el metodo seleccionado
        metodoSeleccionado = None

        # Creamos un diccionario para almacenar los valores retornados por los metodos
        resultado: dict = {}

        # Creamos una lista que almacene las cabezeras que tendra la tabla de resultados
        cabezeras: list = []

        if idMetodoSeleccionado == 0:
            # Metodo de Biseccion
            cabezeras = ["Iteracion", "a", "b", "c", "f(a)", "f(b)", "f(ci)", "f(a) * f(ci)", "f(b) * f(ci)", "Ea (%)"]
            metodoSeleccionado = MetodoBiseccion
        elif idMetodoSeleccionado == 1:
            # Metodo de Falsa Posicion
            cabezeras = ["Iteracion", "a", "b", "c", "f(a)", "f(b)", "f(ci)", "f(a) * f(ci)", "f(b) * f(ci)", "Ea (%)"]
            metodoSeleccionado = MetodoFalsaPosicion
        elif idMetodoSeleccionado == 2:
            # Metodo de la Secante
            cabezeras = ["Iteracion", "Xi-1", "Xi", "F(xi)", F"(xi-1)", "Ea (%)"]
            metodoSeleccionado = MetodoSecante

        if idMetodoSeleccionado == 0:
            # Resolvemos por metodo de Biseccion
            metodoSeleccionado = metodoSeleccionado(funcion=operacion, iteraciones=iteraciones, a=a, b=b,
                                                    eaRequerido=eaRequerido)

            if iteraciones != "":
                resultado = metodoSeleccionado.calcularResultadoIteraciones()
            elif eaRequerido != "":
                resultado = metodoSeleccionado.calcularResultadoErrorAbsoluto()

            self.ventanaResultados.tablaResultados.actualizarTablaResultados(resultado, cabezeras)

        elif idMetodoSeleccionado == 1:
            if iteraciones != "":
                # Resolvemos por metodo de falsa posicion
                metodoFalsaPosicion = MetodoFalsaPosicion(funcion=operacion, iteraciones=iteraciones, a=a, b=b,
                                                          eaRequerido=eaRequerido)

                self.ventanaResultados.tablaResultados.actualizarTablaResultados(
                    metodoFalsaPosicion.calcularResultadoIteraciones(), cabezeras
                )

            elif eaRequerido != "":
                # Resolvemos por metodo de falsa posicion
                metodoFalsaPosicion = MetodoFalsaPosicion(funcion=operacion, iteraciones=iteraciones, a=a, b=b,
                                                          eaRequerido=eaRequerido)

                self.ventanaResultados.tablaResultados.actualizarTablaResultados(
                    metodoFalsaPosicion.calcularResultadoErrorAbsoluto(), cabezeras
                )

        elif idMetodoSeleccionado == 2:
            # Resolvemos por metodo de la Secante
            metodoSeleccionado = metodoSeleccionado(funcion=operacion, iteraciones=iteraciones, a=a, b=b,
                                                    eaRequerido=eaRequerido)

            if iteraciones != "":
                resultado = metodoSeleccionado.calcularResultadoIteraciones()
            elif eaRequerido != "":
                resultado = metodoSeleccionado.calcularResultadoErrorAbsoluto()

            self.ventanaResultados.tablaResultados.actualizarTablaResultados(resultado, cabezeras)


class QLineEditCustom(QLineEdit):
    def __init__(self, text: str == "", placeHolderText: str == ""):
        super().__init__()

        self.text = text
        self.placeHolderText = placeHolderText

        self.setPlaceholderText(self.placeHolderText)
        self.setText(self.text)
        self.setFixedHeight(40)


class QLabelCustom(QLabel):
    def __init__(self, text: str == ""):
        super().__init__()

        self.text: str = text
        expand = QSizePolicy.Policy.Expanding

        self.setText(self.text)
        self.setSizePolicy(expand, expand)


if __name__ == '__main__':
    app = QApplication([])
    ventana = RootFinder()
    ventana.show()
    app.exec()
