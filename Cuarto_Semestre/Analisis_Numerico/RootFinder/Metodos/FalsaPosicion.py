# Metodo de Biseccion

from tabulate import tabulate
import math

iteraciones: int = int(input("Ingrese la cantidad de Iteraciones: "))
a: float = float(input("Ingrese el valor de a: "))
b: float = float(input("Ingrese el valor de b: "))
funcion: str = input("Ingrese la funcion: ")
fafc = ""
fbfc = ""
ea: float = 100
cant: float = 0

cActual: float = 0

# Datos de ejemplo

# 5*x**3-5*x**2+6*x-2
# x**4+3*x**3-2

data = []

for i in range(iteraciones):


    # Calculamos f(a)
    fa = eval(funcion.replace("x", f"({a})"))

    # Calculamos f(b)
    fb = eval(funcion.replace("x", f"({b})"))

    cAnterior = cActual

    # Calculamos ci / C Actual


    # Calculamos f(ci)
    fc = eval(funcion.replace("x", f"({cActual})"))

    # Calculamos Ea

    # Ea = (a-c)/a * 100
    data.append(
        [
            str(i + 1).ljust(10),
            str(a),
            str(b),
            str(cActual),
            str(fa),
            str(fb),
            str(fc)
        ]
    )

    # Hallamos f(a) * f(ci)

    if fa * fc < 0:
        b = cActual
        fafc = "-"
        fbfc = "+"

    # Hallamos f(b) * f(ci)

    if fb * fc < 0:
        a = cActual
        fbfc = "-"
        fafc = "+"

    try:
        # Cuando fb * fc son negativos entonces el anterior es
        ea = abs((cAnterior - cActual) / cActual * 100)

    except Exception as e:
        pass

    data[i].append(fafc.ljust(1))
    data[i].append(fbfc.ljust(1))
    data[i].append(f"{ea} %")

__headers = ["Iteracion", "a", "b", "c", "f(a)", "f(b)", "f(ci)", "f(a) * f(ci)", "f(b) * f(ci)", "Ea (%)"]

import math


class MetodoFalsaPosicion:
    def __init__(self, funcion: str, iteraciones: int, a: float, b: float):
        self.funcion: str = funcion
        self.iteraciones: int = iteraciones
        self.a: float = a
        self.b: float = b
        self.fafc = ""
        self.fbfc = ""
        self.ea: float = 100
        self.cActual: float = 0
        self.contadorResultados = 0
        self.data = []
        self.resultados = {}

    def calcularFaFbFc(self, valor: float):
        return eval(self.funcion.replace("X", f"({valor})"))

    def calcularResultado(self):
        for i in range(self.iteraciones):
            self.data = []

            cAnterior = self.cActual

            # Calculamos f(a)
            fa = self.calcularFaFbFc(self.a)

            # Calculamos f(b)
            fb = self.calcularFaFbFc(self.b)

            # Calculamos ci
            self.cActual = b - (fb * (a - b)) / (fa - fb)

            # Calculamos f(ci)
            fc = self.calcularFaFbFc(self.cActual)

            # Calculamos Ea

            # Ea = (a-c)/a * 100
            self.data.append(str(self.a))
            self.data.append(str(self.b))
            self.data.append(str(self.cActual))
            self.data.append(str(fa))
            self.data.append(str(fb))
            self.data.append(str(fc))

            # Hallamos f(a) * f(ci)

            print(f"F(a): {fa}"
                  f"\nF(b): {fb}"
                  f"\nF(c): {fc}")

            if fa * fc < 0:
                self.b = self.cActual
                self.fafc = "-"
                self.fbfc = "+"

            # Hallamos f(ci) * f(b)

            if fb * fc < 0:
                self.a = self.cActual
                self.fbfc = "-"
                self.fafc = "+"

            try:
                self.ea = abs((cAnterior - self.cActual) / self.cActual * 100)
            except Exception as e:
                pass

            self.data.append(self.fafc.ljust(1))
            self.data.append(self.fbfc.ljust(1))
            self.data.append(f"{self.ea} %")

            self.resultados.update({self.contadorResultados: self.data})
            self.contadorResultados += 1

        return self.resultados

