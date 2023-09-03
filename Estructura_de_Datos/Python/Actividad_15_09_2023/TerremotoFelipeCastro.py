class TerremotoFelipeCastro:
    def __init__(self, nombreTerremoto, fechaOcurrencia, magnitudTerremoto, departamentoTerremoto, numeroMuertosAprox):
        self.__nombreTerremoto = nombreTerremoto
        self.__fechaOcurrencia = fechaOcurrencia
        self.__magnitudTerremoto = magnitudTerremoto
        self.__departamentoOcurrencia = departamentoTerremoto
        self.__numeroMuertosAprox = numeroMuertosAprox

    def ordenarTerremotosPorNombreFelipeCastro(self):
        pass

    def ordenarPorNumeroDeMuertosFelipeCastro(self):
        pass

    def buscarTerremotoEspecificoFelipeCastro(self):
        pass

    def registrarTerremotoFelipeCastro(self):
        pass

    def buscarTerremotoPorNombreFelipeCastro(self):
        pass

    def buscarTerremotoPorNumeroDeMuertosFelipeCastro(self):
        pass

    def buscarTerremotoConMenosMuertos(self):
        pass

    def buscarTerremotoConMayorMagnitud(self):
        pass

    @property
    def getNombre(self):
        return self.__nombreTerremoto

    @property
    def getFecha(self):
        return self.__fechaOcurrencia

    @property
    def getMagnitud(self):
        return self.__magnitudTerremoto

    @property
    def getDepartamento(self):
        return self.__departamentoOcurrencia

    @property
    def getNumeroMuertos(self):
        return self.__numeroMuertosAprox

    def __str__(self):
        return (f"Ciudad: {self.__nombreTerremoto}"
                f"\nFecha: {self.__fechaOcurrencia}"
                f"\nMagnitud: {self.__magnitudTerremoto}"
                f"\nDepartamento: {self.__departamentoOcurrencia}"
                f"\nNumeroMuertos: {self.__numeroMuertosAprox}")
