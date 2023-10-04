# Supongamos que estamos desarrollando un videojuego de carreras de autos y queremos modelar la estructura de clases
# para representar diferentes tipos de autos. Cada auto tiene un modelo, una marca, una velocidad máxima y un tipo de
# motor (gasolina o eléctrico). Queremos implementar la jerarquía de clases utilizando herencia simple.
#
# Instrucciones del ejercicio​
#

from AutoElectrico import AutoElectrico
from AutoGasolina import AutoGasolina

# Para la clase AutoGasolina, este método
# debe decrementar la cantidad de combustible en función de la cantidad de aceleración y la eficiencia del auto. Si
# la cantidad de combustible es menor que la cantidad necesaria para la aceleración, la velocidad actual no debe
# aumentar y se debe imprimir un mensaje de error. Para la clase AutoElectrico, este método debe decrementar la carga
# de la batería en función de la cantidad de aceleración y la eficiencia del auto. Si la carga de la batería es menor
# que la cantidad necesaria para la aceleración, la velocidad actual no debe aumentar y se debe imprimir un mensaje
# de error.​

# •Crea una clase Carrera que tenga un método iniciar que tome dos objetos Auto como parámetros y simule una carrera
# entre ellos. La carrera debe consistir en una serie de iteraciones donde cada auto acelera una cantidad aleatoria
# de km/h entre 0 y su velocidad máxima. El auto que llegue a una velocidad mayor o igual a su velocidad máxima gana
# la carrera. Si los dos autos alcanzan su velocidad máxima al mismo tiempo, la carrera debe terminar en empate.
# Imprime un mensaje indicando el resultado de la carrera.


# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


class Carrera():
    def iniciarCarrera(self):
        autoGasolina = AutoGasolina(modelo="")
        autoElectrico = AutoElectrico()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass
