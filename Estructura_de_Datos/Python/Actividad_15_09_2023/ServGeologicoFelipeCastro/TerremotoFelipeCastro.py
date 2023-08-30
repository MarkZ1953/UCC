class TerremotoFelipeCastro:
    def __init__(self, ciudadTerremoto, fechaOcurrencia, magnitudTerremoto, departamentoTerremoto, numeroMuertosAprox):
        self.__ciudadTerremoto = ciudadTerremoto
        self.__fechaOcurrencia = fechaOcurrencia
        self.__magnitudTerremoto = magnitudTerremoto
        self.__departamentoOcurrencia = departamentoTerremoto
        self.__numeroMuertosAprox = numeroMuertosAprox

    def listarTerremotosFelipeCastro(self):
        pass

    def ordenarTerremotosPorNombreFelipeCastro(self):
        pass


if __name__ == '__main__':
    appTerremotoFelipeCastro = TerremotoFelipeCastro("Caos", "30/08/2023",
                                                     5.6, "Meta",
                                                     10)
    appTerremotoFelipeCastro.registrarTerremotoFelipeCastro()
