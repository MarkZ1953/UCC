import sympy as sp
import math

# Define la variable simbólica
x = sp.Symbol('x')

# Define la función que quieres derivar
f = sp.sin(sp.sqrt(x)) - x

# Deriva la función con respecto a x
f_derivada = sp.diff(f, x)

# Imprime la función derivada
print("La derivada de la función es:", f_derivada)