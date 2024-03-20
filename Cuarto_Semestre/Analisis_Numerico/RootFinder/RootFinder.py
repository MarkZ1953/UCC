from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QGridLayout, QPushButton, QWidget, QVBoxLayout, QLineEdit, \
    QSizePolicy, QApplication, QLabel, QHBoxLayout, QComboBox

from Metodos.Biseccion import MetodoBiseccion
from Componentes.TablaResultados import TablaResultados
from Metodos.FalsaPosicion import MetodoFalsaPosicion


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

        self.layoutOpciones = QHBoxLayout()

        self.layoutCalculadora = QVBoxLayout()
        self.layoutTabla = QVBoxLayout()
        self.layoutTabla.addWidget(self.tablaResultados)

        # self.layout_principal.addLayout(self.layoutCalculadora)
        self.layout_principal.addLayout(self.layoutCalculadora)
        self.layout_principal.addLayout(self.layoutTabla)

        # Llamamos al metodo que crea la entrada de texto
        self.crearEntradaDeTexto()

        # Creamos los botonesMenuInquilinos
        self.crearBotones()

        # Agregamos el QGridLayout al layout principal
        self.layoutCalculadora.addLayout(self.layoutOpciones)
        self.layoutCalculadora.addWidget(self.entrada_texto)
        self.layoutCalculadora.addLayout(self.grid_layout)

        # canvas = FigureCanvas(plt.figure())
        # self.layout_principal.addWidget(canvas)

        # Dibujar ecuación en la figura
        # ax = canvas.figure.add_subplot(111)
        # ax.text(0.5, 0.5, r'$\frac{a}{b} + \frac{c}{d} = \frac{ad + bc}{bd}$', fontsize=20, ha='center')
        # ax.axis('off')

        self.layoutOpciones.addWidget(self.peticiones)
        self.layoutOpciones.addWidget(self.cbMetodo)

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

        self.cbMetodo = QComboBox()
        self.cbMetodo.addItem("Biseccion", 0)
        self.cbMetodo.addItem("Falsa Posicion", 1)

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
            "pi": (6, 2),
            "^": (6, 3)
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

        peticiones = {
            0: "Ingrese la funcion",
            1: "Ingrese la cantidad de iteraciones",
            2: "Ingrese el valor de A",
            3: "Ingrese el valor de B",
            4: "Ingrese el error porcentual al que desea llegar"
        }

        # try:
        if textoBoton == "C":
            self.entrada_texto.clear()
        elif textoBoton == "=":
            if self.contadorPeticiones < 4:
                self.contadorPeticiones += 1
                self.peticiones.setText(peticiones[self.contadorPeticiones])
                # Guardamos los datos que se van pidiendo en la calculadora
                self.datosOperacion.update({self.contadorPeticiones - 1: self.entrada_texto.text()})
                self.entrada_texto.clear()
            else:
                self.retornarResultadoOperacion(self.datosOperacion)
                self.entrada_texto.clear()
                self.contadorHistorialOperaciones += 1
                self.historialOperaciones.update({self.contadorHistorialOperaciones: self.datosOperacion})
        elif textoBoton == "\u232B":
            self.eliminarUltimoCaracter()
        else:
            if self.entrada_texto.text() in ["Ocurrio un Error", "No puedes dividir por cero"]:
                self.entrada_texto.clear()
                self.entrada_texto.insert(textoBoton)
            else:
                self.entrada_texto.insert(textoBoton)

    # except ZeroDivisionError:
    # self.entrada_texto.clear()
    # self.entrada_texto.insert("No puedes Dividir por Cero")
    # except Exception as e:
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
                     .replace("e", "math.e")
                     .replace("^", "**"))

        iteraciones: int = int(datosOperacion[1])
        a: float = float(datosOperacion[2])
        b: float = float(datosOperacion[3])

        if self.cbMetodo.currentData() == 0:
            # Resolvemos por metodo de biseccion
            metodoBiseccion = MetodoBiseccion(funcion=operacion, iteraciones=iteraciones, a=a, b=b)
            self.tablaResultados.actualizarTablaResultados(metodoBiseccion.calcularResultado())

        elif self.cbMetodo.currentData() == 1:
            # Resolvemos por metodo de falsa posicion
            metodoFalsaPosicion = MetodoFalsaPosicion(funcion=operacion, iteraciones=iteraciones, a=a, b=b)
            self.tablaResultados.actualizarTablaResultados(metodoFalsaPosicion.calcularResultado())


if __name__ == '__main__':
    app = QApplication([])
    ventana = Calculadora()
    ventana.show()
    app.exec()
