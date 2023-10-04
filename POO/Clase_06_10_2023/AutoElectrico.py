from Auto import Auto


class AutoElectrico(Auto):
    def __init__(self, modelo, marca, velocidadMaxima, tipoMotor, capacidadBateria):
        super().__init__(modelo, marca, velocidadMaxima, tipoMotor)
        self.__capacidadBateria = capacidadBateria

    @property
    def capacidadBateria(self):
        return self.__capacidadBateria

    def acelerar(self, cantidad: int):
        if self.estado:
            if cantidad + self.velocidad > self.velocidadMaxima:
                self.velocidad = self.velocidadMaxima
                print("Se ha querido acelerar mas de la velocidad maxima del auto, la velocidad que lleva el "
                      f"carro ahora es de: {self.velocidad} km/h")
            elif cantidad <= self.velocidadMaxima:
                self.velocidad += cantidad
                print(f"La velocidad del auto ahora es de: {self.velocidad} km/h")
        else:
            print("El carro no se puede acelerar ya que se encuentra apagado")


if __name__ == '__main__':
    autoElectrico1 = AutoElectrico("EV1 2023",
                                   "Tesla",
                                   220,
                                   "Electrico",
                                   80)

    autoElectrico1.encender()
    autoElectrico1.acelerar(220)
    autoElectrico1.apagar()
    print(autoElectrico1.velocidad)
