from sympy import sqrt, Symbol, sin, cos, tan, diff, euler, acos, acsc, atan, asin, pi


class MetodoNewtonRaphson:
    def __init__(self, funcion: str, iteraciones: int, a: float, eaRequerido):
        self.funcion: str = funcion
        self.iteraciones: int = iteraciones
        self.xi: float = a
        self.xia: float = 0
        self.fafc = ""
        self.fbfc = ""
        self.eaRequerido = eaRequerido
        self.ea: float = 100
        self.cActual: float = 0
        self.contadorResultados = 0
        self.data = []
        self.resultados = {}
        self.funcionDerivada = self.calcularDerivada(self.funcion)

    @staticmethod
    def calcularDerivada(funcion: str):
        # Definir la variable y la función
        x = Symbol('X')

        # Calculamos la derivada
        derivada = diff(funcion, x)

        print(derivada)
        return str(derivada).strip()

    def calcularFuncion(self, valor: float):
        return eval(self.funcion.replace("X", f"({valor})"))

    def calcularFuncionDerivada(self, valor: float):
        return eval(self.funcionDerivada.replace("X", f"({valor})"))

    def calcularResultadoErrorAbsoluto(self):

        while True:
            self.data = []

            # Calculamos F(xi)
            fxi = self.calcularFuncion(self.xi)

            # Calculamos F'(xi)
            fpxi = self.calcularFuncionDerivada(self.xi)

            # Guardamos los datos
            self.data.append(str(self.xi))
            self.data.append(str(fxi))
            self.data.append(str(fpxi))

            try:
                # Calculamos el Ea
                self.ea = abs((self.xia - self.xi) / self.xi * 100)
            except Exception as e:
                pass

            # Obtenemos el valor anterior de Xi
            self.xia = self.xi

            # Calculamos Xi+1
            self.xi = self.xi - (fxi/fpxi)

            # Guardamos los datos
            self.data.append(f"{self.ea} %")
            self.resultados.update({self.contadorResultados: self.data})

            self.contadorResultados += 1

            if self.ea <= float(self.eaRequerido):
                break

        return self.resultados

    def calcularResultadoIteraciones(self):
        for i in range(int(self.iteraciones)):
            self.data = []

            # Calculamos F(xi)
            fxi = self.calcularFuncion(self.xi)

            # Calculamos F'(xi)
            fpxi = self.calcularFuncionDerivada(self.xi)

            # Guardamos los datos
            self.data.append(str(self.xi))
            self.data.append(str(fxi))
            self.data.append(str(fpxi))

            try:
                # Calculamos el Ea
                print(f"{self.xia} - {self.xi} / {self.xi}")
                self.ea = abs((self.xia - self.xi) / self.xi * 100)
            except Exception as e:
                pass

            # Obtenemos el valor anterior de Xi
            self.xia = self.xi

            # Calculamos Xi+1
            self.xi = self.xi - (fxi / fpxi)

            # Guardamos los datos
            self.data.append(f"{self.ea} %")
            self.resultados.update({self.contadorResultados: self.data})

            self.contadorResultados += 1

        return self.resultados
