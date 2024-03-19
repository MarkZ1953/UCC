from tabulate import tabulate
import math


class MetodoBiseccion:
    def __init__(self, funcion: str, iteraciones: int,  a: float, b: float):
        self.funcion: str = funcion
        self.iteraciones: int = iteraciones
        self.a: float = a
        self.b: float = b

fafc = ""
fbfc = ""
ea: float = 100

cActual: float = 0

data = []

for i in range(iteraciones):
    cAnterior = cActual

    # Calculamos ci
    cActual = (a + b) / 2

    # Calculamos f(a)
    fa = eval(funcion.replace("x", f"({a})"))

    # Calculamos f(b)
    fb = eval(funcion.replace("x", f"({b})"))

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

    # Hallamos f(ci) * f(b)

    if fb * fc < 0:
        a = cActual
        fbfc = "-"
        fafc = "+"

    try:
        ea = abs((cAnterior - cActual) / cActual * 100)
    except Exception as e:
        pass

    data[i].append(fafc.ljust(1))
    data[i].append(fbfc.ljust(1))
    data[i].append(f"{ea} %")
