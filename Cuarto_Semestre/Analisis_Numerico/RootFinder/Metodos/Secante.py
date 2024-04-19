import math


class MetodoSecante:
    def __init__(self, funcion: str, iteraciones: int, a: float, b: float, eaRequerido):
        self.funcion: str = funcion
        self.iteraciones: int = iteraciones
        self.xim1: float = a
        self.xi: float = b
        self.eaRequerido = eaRequerido
        self.ea: float = 100
        self.cActual: float = 0
        self.contadorResultados = 0
        self.data = []
        self.resultados = {}

    def calcularFaFbFc(self, valor: float):
        return eval(self.funcion.replace("X", f"({valor})"))

    def calcularResultadoErrorAbsoluto(self):

        while self.ea >= float(self.eaRequerido):
            self.data = []

            # Calculamos fxi
            fxi = self.calcularFaFbFc(self.xi)

            # Calculamos fx_(i-1)
            fxim1 = self.calcularFaFbFc(self.xim1)

            # Calculamos xi+1
            self.xi = self.xi - (fxi * (self.xim1 - self.xi) / fxim1 - fxi)

            # Agregamos los valores a la lista
            self.data.append(str(self.xim1))
            self.data.append(str(self.xi))
            self.data.append(str(self.cActual))
            self.data.append(str(fxim1))
            self.data.append(str(fxi))

            try:
                self.ea = abs(((self.xim1 - self.xi) / self.xi) * 100)
            except Exception as e:
                pass

            self.data.append(f"{self.ea} %")

            self.resultados.update({self.contadorResultados: self.data})
            self.contadorResultados += 1

        return self.resultados

    def calcularResultadoIteraciones(self):

        # Calculamos fx_(i-1)
        fxim1 = self.calcularFaFbFc(self.xim1)

        for i in range(int(self.iteraciones)):
            self.data = []

            cAnterior = self.cActual

            xi = self.calcularFaFbFc(self.xi)

            # Calculamos f(a)
            fxim1 = self.calcularFaFbFc(self.xim1)

            fxi = self.calcularFaFbFc(self.xi)

            # Calculamos fi+1
            xi = xi - (fxi * (self.xim1 - self.xi) / fxim1 - fxi)

            # Ea = (a-c)/a * 100
            self.data.append(str(self.xim1))
            self.data.append(str(self.xi))
            self.data.append(str(self.cActual))
            self.data.append(str(fxim1))
            self.data.append(str(fxi))

            try:
                self.ea = abs((cAnterior - self.cActual) / self.cActual * 100)
            except Exception as e:
                pass

            self.data.append(f"{self.ea} %")

            self.resultados.update({self.contadorResultados: self.data})
            self.contadorResultados += 1

        return self.resultados
