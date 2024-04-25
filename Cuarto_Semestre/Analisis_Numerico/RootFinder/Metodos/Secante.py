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

        while True:
            self.data = []

            self.data.append(str(self.xim1))
            self.data.append(str(self.xi))

            # Calculamos fxi
            fxi = self.calcularFaFbFc(self.xi)

            # Calculamos fx_(i-1)
            fxim1 = self.calcularFaFbFc(self.xim1)

            # Agregamos los valores a la lista
            self.data.append(str(fxi))
            self.data.append(str(fxim1))

            try:
                self.ea = abs(((self.xim1 - self.xi) / self.xi) * 100)
            except Exception as e:
                pass

            self.data.append(f"{self.ea} %")
            self.resultados.update({self.contadorResultados: self.data})

            if self.ea <= float(self.eaRequerido):
                break

            xitemp = self.xi

            # Calculamos xi+1
            self.xi = self.xi - (fxi * (self.xim1 - self.xi) / (fxim1 - fxi))

            self.xim1 = xitemp

            self.contadorResultados += 1

        return self.resultados

    def calcularResultadoIteraciones(self):

        for i in range(int(self.iteraciones)):
            self.data = []

            self.data.append(str(self.xim1))
            self.data.append(str(self.xi))

            # Calculamos fxi
            fxi = self.calcularFaFbFc(self.xi)

            # Calculamos fx_(i-1)
            fxim1 = self.calcularFaFbFc(self.xim1)

            # Agregamos los valores a la lista
            self.data.append(str(fxi))
            self.data.append(str(fxim1))

            try:
                self.ea = abs(((self.xim1 - self.xi) / self.xi) * 100)
            except Exception as e:
                pass

            self.data.append(f"{self.ea} %")
            self.resultados.update({self.contadorResultados: self.data})

            if self.ea == 0:
                break

            xitemp = self.xi

            # Calculamos xi+1
            self.xi = self.xi - (fxi * (self.xim1 - self.xi) / (fxim1 - fxi))

            self.xim1 = xitemp

            self.contadorResultados += 1

        return self.resultados
