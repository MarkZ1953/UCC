from Auto import Auto


class AutoGasolina(Auto):
    def __init__(self, modelo, marca, velocidadMaxima, tipoMotor, cantidadCombustible):
        super().__init__(modelo, marca, velocidadMaxima, tipoMotor)
