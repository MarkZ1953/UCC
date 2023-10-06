from enum import auto

from Auto import Auto


class AutoElectrico(Auto):
    def __init__(self, modelo, marca, velocidadMaxima, tipoMotor, capacidadBateria, consumo):
        super().__init__(modelo, marca, velocidadMaxima, tipoMotor, consumo)
        self.__capacidadBateria = capacidadBateria  # La capacidad de la bateria
        self.__bateria = capacidadBateria  # La cantidad de bateria que tiene el auto, se inicializa en la carga maxima

    @property
    def capacidadBateria(self):
        return self.__capacidadBateria

    @capacidadBateria.setter
    def capacidadBateria(self, valor):
        self.__capacidadBateria = valor

    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, valor):
        self.__bateria = valor

    def informacionCombustible(self):
        print(f"La bateria actual de la bateria es: {self.bateria} kWh")

    def comprobarBateria(self, cantidad):
        if self.bateria > (cantidad * self.consumo):
            return True
        else:
            return False

    def acelerar(self, cantidad: int):
        # Se comprueba si el carro esta encendido o apagado
        if self.estado:
            # Se comprueba si la cantidad de bateria que consume por la aceleracion previamente obtenida, es menor
            # a la capacidad de la bateria actual del auto, si es suficiente hara lo que sigue.
            if self.comprobarBateria(cantidad):
                # Comprueba si la aceleracion mas la velocidad actual es mayor a la velocidad maxima del auto
                if cantidad + self.velocidad > self.velocidadMaxima:
                    self.bateria = self.bateria - (cantidad * self.consumo)
                    self.velocidad = self.velocidadMaxima
                    print(f"Se ha querido acelerar mas de la velocidad maxima del auto con modelo {self.modelo}, la "
                          f"velocidad que lleva el carro ahora es de: {self.velocidad} km/h")
                elif cantidad <= self.velocidadMaxima:
                    self.velocidad += cantidad
                    self.bateria = self.bateria - (cantidad * self.consumo)
                    print(f"La velocidad del auto con modelo {self.modelo} ahora es de: {self.velocidad} km/h")
            else:
                # Si la capacidad de bateria no es suficiente, se mantendra la velocidad actual y no se haran cambios.
                print("La capacidad de la bateria es insuficiente para poder acelerar, no se hara ningun cambio en"
                      "la velocidad del auto ni la bateria.")
        else:
            # Si la variable "estado" es False, significara que el carro se encuentra apagado
            print("El carro no se puede acelerar ya que se encuentra apagado")


if __name__ == '__main__':
    autoElectrico1 = AutoElectrico("EV1 2023",
                                   "Tesla",
                                   220,
                                   "Electrico",
                                   80,
                                   0.025)

    autoElectrico1.encender()
    autoElectrico1.acelerar(220)
    autoElectrico1.informacionCombustible()
    autoElectrico1.acelerar(100)
    autoElectrico1.informacionCombustible()
