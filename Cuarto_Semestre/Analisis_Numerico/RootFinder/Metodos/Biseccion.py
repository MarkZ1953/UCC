import math


class MetodoBiseccion:
    def __init__(self, funcion: str, iteraciones: int, a: float, b: float, eaRequerido):
        self.funcion: str = funcion
        self.iteraciones: int = iteraciones
        self.a: float = a
        self.b: float = b
        self.fafc = ""
        self.fbfc = ""
        self.eaRequerido = eaRequerido
        self.ea: float = 100
        self.cActual: float = 0
        self.contadorResultados = 0
        self.data = []
        self.resultados = {}

    def calcularFaFbFc(self, valor: float):
        return eval(self.funcion.replace("X", f"({valor})"))

    def calcularResultadoErrorAbsoluto(self):

        while True:
            self.data = []

            cAnterior = self.cActual

            # Calculamos ci
            self.cActual = (self.a + self.b) / 2

            # Calculamos f(a)
            fa = self.calcularFaFbFc(self.a)

            # Calculamos f(b)
            fb = self.calcularFaFbFc(self.b)

            # Calculamos f(ci)
            fc = self.calcularFaFbFc(self.cActual)

            # Ea = (a-c)/a * 100
            self.data.append(str(self.a))
            self.data.append(str(self.b))
            self.data.append(str(self.cActual))
            self.data.append(str(fa))
            self.data.append(str(fb))
            self.data.append(str(fc))

            # Hallamos f(a) * f(ci)
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

            if self.ea <= float(self.eaRequerido):
                break

        return self.resultados

    def calcularResultadoIteraciones(self):
        for i in range(int(self.iteraciones)):
            self.data = []

            cAnterior = self.cActual

            # Calculamos ci
            self.cActual = (self.a + self.b) / 2

            # Calculamos f(a)
            fa = self.calcularFaFbFc(self.a)

            # Calculamos f(b)
            fb = self.calcularFaFbFc(self.b)

            # Calculamos f(ci)
            fc = self.calcularFaFbFc(self.cActual)

            # Ea = (a-c)/a * 100
            self.data.append(str(self.a))
            self.data.append(str(self.b))
            self.data.append(str(self.cActual))
            self.data.append(str(fa))
            self.data.append(str(fb))
            self.data.append(str(fc))

            # Hallamos f(a) * f(ci)
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
