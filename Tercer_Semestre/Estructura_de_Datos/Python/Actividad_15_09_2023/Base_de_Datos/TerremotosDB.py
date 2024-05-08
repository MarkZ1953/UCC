from ConexionDB import TerremotosDBFelipeCastro
from TerremotoFelipeCastro import TerremotoFelipeCastro


class InformacionTerremotos:
    REGISTRAR = ("INSERT INTO Terremotos (nombreTerremoto, fechaTerremoto, magnitudTerremoto, departamentoTerremoto,"
                 "noMuertosTerremoto, ayudaEstadoTerremoto) VALUES(?, ?, ?, ?, ?, ?)")
    SELECCIONARTODOS = "SELECT * FROM Terremotos"
    ELIMINARTERREMOTO = "DELETE FROM Terremotos WHERE idTerremoto = ?"
    BUSCARTERREMOTOPORID = "SELECT * FROM Terremotos WHERE idTerremoto = ?"

    @classmethod
    def registrarTerremoto(cls, terremoto):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.REGISTRAR, (terremoto.getNombre,
                                           terremoto.getFecha,
                                           terremoto.getMagnitud,
                                           terremoto.getDepartamento,
                                           terremoto.getNumeroMuertos,
                                           terremoto.getAyudaEstado))

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
                                                        terremoto[5],
                                                        terremoto[6]))

            return terremotos

    @classmethod
    def eliminarTerremoto(cls, idTerremoto):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.ELIMINARTERREMOTO, (idTerremoto,))

    @classmethod
    def seleccionarTerremotoPorId(cls, idTerremoto):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.BUSCARTERREMOTOPORID, (idTerremoto,))
            terremoto = cursor.fetchone()

            return TerremotoFelipeCastro(terremoto[0],
                                         terremoto[1],
                                         terremoto[2],
                                         terremoto[3],
                                         terremoto[4],
                                         terremoto[5],
                                         terremoto[6])

    @classmethod
    def seleccionarTodosLosTerremotos(cls):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.SELECCIONARTODOS)
            return cursor.fetchall()
