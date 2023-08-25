# Metodo	Tipo	Atributos	Resultados	Comprobaciones
# CONSTRUCTOR	???	Ninguno	Inicializar cadenas en "", numeros en 0 y booleano en falso

# desacelerar	público	Velocidad	Disminuye la velocidad	comprueba la velocidad respecto a la minima
# viaje	público	Tiempo y Velocidad	disminuye la cantidad de combustible segun el consumo si puede completar el viaje	comprueba el estado y cantidad de combustible
# mostrar la información del carro	público	Ninguno
# Si la salida de alguno de los metodos no cumple con la comprobación se debe generar un ERROR en el Metodo, así si el carro esta apagado y se acelera debe devolver ERROR ACELERAR

class Carro:
    def __init__(self, modelo: str, color: str, velocidadMaxima: float, velocidad: float, combustibleMaximo: int,
                 combustible: int, estado: bool, consumo: float):
        self.__modelo = modelo
        self.__color = color
        self.__velocidadMaxima = velocidadMaxima
        self.__velocidad = velocidad
        self.__combustibleMaximo = combustibleMaximo
        self.__combustible = combustible
        self.__estado = estado
        self.__consumo = consumo

    @property
    def getModelo(self):
        return self.__modelo

    @property
    def getColor(self):
        return self.__color

    @property
    def getVelocidadMaxima(self):
        return self.__velocidadMaxima

    @property
    def getVelocidad(self):
        return self.__velocidad

    @property
    def getCombustibleMaximo(self):
        return self.__combustibleMaximo

    @property
    def getCombustible(self):
        return self.__combustible

    @property
    def getEstado(self):
        return self.__estado

    @getEstado.setter
    def setEstado(self, estado):
        self.__estado = estado

    @property
    def getConsumo(self):
        return self.__consumo

    def apagar(self):
        if self.getEstado:
            if self.getVelocidad == 0:
                self.setEstado = False
                print("El auto se ha apagado.")
            else:
                self.__velocidad = 0.0
                self.setEstado = False
                print("El carro se ha frenado con freno de mano, ahora la velocidad es de 0 km/h.")
        elif not self.getEstado:
            print("El auto ya se encuentra apagado.")

    def encender(self):
        if self.getEstado:
            print("El auto ya se encuentra encendido.")
        else:
            self.setEstado = True
            print("El auto se ha encendido.")

    def acelerar(self, aceleracion: float):
        if self.getEstado:
            if self.getVelocidad + aceleracion <= self.getVelocidadMaxima:
                self.__velocidad += aceleracion
                print(f"El auto ha acelerado {aceleracion} km/h, ahora su velocidad es de {self.getVelocidad} km/h")
            else:
                print(f"El auto no puede acelerar mas de {self.getVelocidadMaxima} km/h")
        else:
            print("El auto esta apagado, no se puede acelerar.")

    def desacelerar(self, desaceleracion: float):
        if self.getEstado:
            if self.getVelocidad - abs(desaceleracion) >= 0:
                self.__velocidad -= desaceleracion
                print(f"El auto ha desacelerado {abs(desaceleracion)} km/h, ahora su velocidad es "
                      f"de {self.getVelocidad} km/h")
            else:
                print(f"El auto no puede desacelerar menos de 0 km/h")
        else:
            print("El auto esta apagado, no se puede desacelerar.")

    def repostar(self, combustible):
        if self.getEstado and self.getVelocidad < 0:
            print("No se ha podido repostar el auto, ya que se encuentra en movimiento o esta encendido.")
        else:
            print(f"Se han respostado {combustible}, ahora el carro tiene "
                  f"{self.getCombustible + combustible}/{self.getCombustibleMaximo}")

    def viaje(self, tiempoRecorrido: float):
        distanciaRecorrida = tiempoRecorrido * self.getVelocidad
        consumoGasolina = distanciaRecorrida / self.getConsumo
        print(f"El auto a una velocidad de {self.getVelocidad} km/h en {tiempoRecorrido} horas ha consumido "
              f"{consumoGasolina} galones")

    def obtenerInformacionCarro(self):
        return (f"Modelo: {self.getModelo}"
                f"\nColor: {self.getColor}"
                f"\nVelocidad Maxima: {self.getVelocidadMaxima}"
                f"\nVelocidad: {self.getVelocidad}"
                f"\nCombustible Maximo: {self.getCombustibleMaximo}"
                f"\nCombustible: {self.getCombustible}"
                f"\nEstado: {self.getEstado}"
                f"\nConsumo: {self.getConsumo}")


if __name__ == '__main__':
    carro = Carro("Yaris Cross", "Gris", 280,
                  0, 14, 8,
                  False, 0.05)
    carro.apagar()
    carro.encender()
    carro.acelerar(300)
    carro.acelerar(100)
    print(carro.obtenerInformacionCarro())
    carro.apagar()
    carro.acelerar(100)
