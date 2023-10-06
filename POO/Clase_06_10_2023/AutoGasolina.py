from Auto import Auto


class AutoGasolina(Auto):
    def __init__(self, modelo, marca, velocidadMaxima, tipoMotor, cantidadCombustible, consumo):
        super().__init__(modelo, marca, velocidadMaxima, tipoMotor, consumo)
        self.__cantidadCombustible = cantidadCombustible
        self.__combustible = cantidadCombustible

    @property
    def cantidadCombustible(self):
        return self.__cantidadCombustible

    @cantidadCombustible.setter
    def cantidadCombustible(self, valor):
        self.__cantidadCombustible = valor

    @property
    def combustible(self):
        return self.__combustible

    @combustible.setter
    def combustible(self, valor):
        self.__combustible = valor

    def informacionCombustible(self):
        print(f"La bateria actual de la bateria es: {self.combustible} L")

    def comprobarGasolina(self, cantidad):
        if self.combustible > (cantidad * self.consumo):
            return True
        else:
            return False

    def acelerar(self, cantidad: int):
        # Se comprueba si el carro esta encendido o apagado
        if self.estado:
            # Se comprueba si la cantidad de bateria que consume por la aceleracion previamente obtenida, es menor
            # a la capacidad de la bateria actual del auto, si es suficiente hara lo que sigue.
            if self.comprobarGasolina(cantidad):
                # Comprueba si la aceleracion mas la velocidad actual es mayor a la velocidad maxima del auto
                if cantidad + self.velocidad > self.velocidadMaxima:
                    self.combustible = self.combustible - (cantidad * self.consumo)
                    self.velocidad = self.velocidadMaxima
                    print(f"Se ha querido acelerar mas de la velocidad maxima del auto con modelo {self.modelo}, la "
                          f"velocidad que lleva el carro ahora es de: {self.velocidad} km/h")
                elif cantidad <= self.velocidadMaxima:
                    self.velocidad += cantidad
                    self.combustible = self.combustible - (cantidad * self.consumo)
                    print(f"La velocidad del auto con modelo {self.modelo} ahora es de: {self.velocidad} km/h")
            else:
                # Si la capacidad de bateria no es suficiente, se mantendra la velocidad actual y no se haran cambios.
                print("La capacidad de la bateria es insuficiente para poder acelerar, no se hara ningun cambio en"
                      "la velocidad del auto ni la bateria.")
        else:
            # Si la variable "estado" es False, significara que el carro se encuentra apagado
            print("El carro no se puede acelerar ya que se encuentra apagado")


if __name__ == '__main__':
    autoGasolina1 = AutoGasolina("Sedan 2023",
                                 "Toyota",
                                 200,
                                 "Motor Gasolina",
                                 50,
                                 0.015)
