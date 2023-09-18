from ConexionDB import TerremotosDBFelipeCastro
from TerremotoFelipeCastro import TerremotoFelipeCastro


class InformacionTerremotos:
    REGISTRAR = ("INSERT INTO Terremotos (nombreTerremoto, fechaTerremoto, magnitudTerremoto, departamentoTerremoto,"
                 "noMuertosTerremoto) VALUES(?, ?, ?, ?, ?)")
    SELECCIONARTODOS = "SELECT * FROM Terremotos"

    @classmethod
    def registrarTerremoto(cls, terremoto):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.REGISTRAR, (terremoto.getNombre,
                                           terremoto.getFecha,
                                           terremoto.getMagnitud,
                                           terremoto.getDepartamento,
                                           terremoto.getNumeroMuertos))

    @classmethod
    def seleccionarTodosLosTerremotosObj(cls):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.SELECCIONARTODOS)
            terremotos = []

            for terremoto in cursor.fetchall():
                terremotos.append(TerremotoFelipeCastro(terremoto[0],
                                                        terremoto[1],
                                                        terremoto[2],
                                                        terremoto[3],
                                                        terremoto[4],
                                                        terremoto[5]))

            return terremotos

    @classmethod
    def seleccionarTodosLosTerremotos(cls):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.SELECCIONARTODOS)
            return cursor.fetchall()
