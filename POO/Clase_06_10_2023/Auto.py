from abc import ABC, abstractmethod


class Auto(ABC):
    def __init__(self, modelo, marca, velocidadMaxima, tipoMotor, consumo):
        self.__modelo = modelo
        self.__marca = marca
        self.__velocidadMaxima = velocidadMaxima
        self.__tipoMotor = tipoMotor
        self.__estado = False
        self.__velocidad = 0
        self.__consumo = consumo

    @property
    def consumo(self):
        return self.__consumo

    @property
    def modelo(self):
        return self.__modelo

    @property
    def marca(self):
        return self.__marca

    @property
    def velocidadMaxima(self):
        return self.__velocidadMaxima

    @property
    def tipoMotor(self):
        return self.__tipoMotor

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, valor):
        self.__estado = valor

    @property
    def velocidad(self):
        return self.__velocidad

    @velocidad.setter
    def velocidad(self, velocidad: int):
        self.__velocidad = velocidad

    @abstractmethod
    def acelerar(self, cantidad: int):
        pass

    @abstractmethod
    def informacionCombustible(self):
        pass

    def encender(self):
        if self.estado:
            print("El auto ya se encuentra encendido")
        else:
            self.__estado = True
            print("El auto se encendio")

    def apagar(self):
        if self.velocidad == 0:
            if not self.estado:
                print("El auto ya se encuentra apagado")
            else:
                self.__estado = False
                print("El auto se apago correctamente")
        else:
            print("El auto no se puede apagar ya se que encuentra en movimiento")
            opcion = input("¿Desea que el auto frene y la velocidad del auto ahora sea 0 km/h? (y/n): ")
            if opcion.lower() == "y":
                self.velocidad = 0
            elif opcion.lower() == "n":
                print(f"La velocidad del auto se mantiene en: {self.velocidad} km/h")
            else:
                print("Debe ingresar una opcion valida")
                self.apagar()

    def __str__(self):
        pass
