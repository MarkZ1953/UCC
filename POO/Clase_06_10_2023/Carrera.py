from AutoElectrico import AutoElectrico
from AutoGasolina import AutoGasolina
import random


# •Crea una clase Carrera que tenga un método iniciar que tome dos objetos Auto como parámetros y simule
# una carrera entre ellos. La carrera debe consistir en una serie de iteraciones donde cada auto acelera una cantidad
# aleatoria de km/h entre 0 y su velocidad máxima. El auto que llegue a una velocidad mayor o igual a su velocidad
# máxima gana la carrera. Si los dos autos alcanzan su velocidad máxima al mismo tiempo, la carrera debe terminar en
# empate. Imprime un mensaje indicando el resultado de la carrera.
# 250 < 100 and 100 < 250
class Carrera:
    def iniciarCarrera(self, autoGasolina, autoElectrico):
        autoGasolina.estado = True
        autoElectrico.estado = True

        print("Los autos se encendieron y arrancaron")

        while True:
            tempAceleracionAutoElectrico = random.randint(0, autoElectrico.capacidadBateria)
            tempAceleracionAutoGasolina = random.randint(0, autoGasolina.cantidadCombustible)
            autoElectrico.acelerar(tempAceleracionAutoElectrico)
            autoGasolina.acelerar(tempAceleracionAutoGasolina)

            if (autoElectrico.comprobarBateria(tempAceleracionAutoElectrico) and
                    autoGasolina.comprobarGasolina(tempAceleracionAutoGasolina)):

                if autoElectrico.velocidad == autoElectrico.velocidadMaxima:
                    print(f"El auto con el modelo: {autoElectrico.modelo} llego a la meta de primeras.")
                    break
                elif autoGasolina.velocidad == autoGasolina.velocidadMaxima:
                    print(f"El auto con el modelo: {autoGasolina.modelo} llego a la meta de primeras.")
                    break
                elif ((autoElectrico.velocidad/autoElectrico.velocidadMaxima) * 100 ==
                      (autoGasolina.velocidad/autoGasolina.velocidadMaxima) * 100):
                    print("Se genero un empate en la carrera de los dos autos")
                    break
            else:
                if autoElectrico.velocidad > autoGasolina.velocidad:
                    print(f"El auto con el modelo: {autoElectrico.modelo} llego a la meta de primeras.")
                    break
                elif autoGasolina.velocidad > autoElectrico.velocidad:
                    print(f"El auto con el modelo: {autoGasolina.modelo} llego a la meta de primeras.")
                    break


if __name__ == '__main__':
    autoElectrico1 = AutoElectrico("EV1 2023",
                                   "Tesla",
                                   220,
                                   "Electrico",
                                   80,
                                   0.2)

    autoGasolina1 = AutoGasolina("Sedan 2023",
                                 "Toyota",
                                 200,
                                 "Motor Gasolina",
                                 50,
                                 0.01)

    Carrera().iniciarCarrera(autoGasolina1, autoElectrico1)
