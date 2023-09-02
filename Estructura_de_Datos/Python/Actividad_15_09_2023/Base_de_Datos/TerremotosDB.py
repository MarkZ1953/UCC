from ConexionDB import TerremotosDBFelipeCastro


class InformacionTerremotos:
    REGISTRAR = ("INSERT INTO Terremotos (ciudad, fecha, magnitud, departamento, noMuertos) "
                 "VALUES(?, ?, ?, ?, ?)")
    SELECCIONARTODOS = "SELECT * FROM Terremotos"

    @classmethod
    def registrarTerremoto(cls, ciudad, fecha, magnitud, departamento, noMuertos):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.REGISTRAR, (ciudad, fecha, magnitud, departamento, noMuertos))

    @classmethod
    def seleccionarTodosLosTerremotos(cls):
        with TerremotosDBFelipeCastro() as cursor:
            cursor.execute(cls.SELECCIONARTODOS)
            return cursor.fetchall()


if __name__ == '__main__':
    db = InformacionTerremotos()
    db.registrarTerremoto("Villavicencio", "30/08/2023", 5.6, "Meta", 3)
