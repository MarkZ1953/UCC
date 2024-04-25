from sympy import sqrt, Symbol, sin, cos, tan, diff
import math

# Define la variable simbólica
x = Symbol('x')

# Define la función que quieres derivar
f = sin(sqrt(x)) - x

# Deriva la función con respecto a x
f_derivada = diff(f, x)

# Imprime la función derivada
print("La derivada de la función es:", f_derivada)