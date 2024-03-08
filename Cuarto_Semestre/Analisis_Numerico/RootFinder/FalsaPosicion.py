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
    cActual = b - (fb * (a - b)) / (fa - fb)

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

# Imprimir la tabla
print(tabulate(data, headers=__headers, numalign="center", stralign="center"))

# Metodo de Falsa Posicion
