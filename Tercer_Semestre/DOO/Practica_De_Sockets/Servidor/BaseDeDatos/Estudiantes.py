from ConexionDB import ColegioDB


class EstudianteDB:
    _SELECCIONARXID = "SELECT * FROM estudiantes WHERE idEstudiante = ?"
    _INSERTAR = ("INSERT INTO estudiantes (nombres, apellidos, fechaNacimiento, sexo, telefono, correoElectronico) "
                 "VALUES(?, ?, ?, ?, ?, ?)")
    _ELIMINAR = "DELETE FROM estudiantes WHERE idEstudiante = ?"
    _ACTUALIZAR = ("UPDATE estudiantes SET nombres = ?, apellidos = ?, telefono = ?, correoElectronico = ? WHERE "
                   "idEstudiante = ?")
    _SELECCIONARTODOS = "SELECT * FROM estudiantes"
    _SELECCIONARALGUNOSDATOS = ("SELECT nombres, apellidos, telefono, correoElectronico FROM estudiantes WHERE "
                                "idEstudiante = ?")

    @classmethod
    def seleccionarEstudianteId(cls, idEstudiante):
        with ColegioDB() as cursor:
            cursor.execute(cls._SELECCIONARXID, (idEstudiante,))
            return cursor.fetchone()

    @classmethod
    def ingresarEstudiante(cls, nombres, apellidos, edad, sexo, telefono, correoElectronico):
        with ColegioDB() as cursor:
            cursor.execute(cls._INSERTAR, (nombres, apellidos, edad, sexo, telefono, correoElectronico))

    @classmethod
    def actualizarEstudiante(cls, nombres, apellidos, telefono, correoElectronico, idEstudiante):
        with ColegioDB() as cursor:
            cursor.execute(cls._ACTUALIZAR, (nombres, apellidos, telefono, correoElectronico, idEstudiante))

    @classmethod
    def eliminarEstudiante(cls, idEstudiante):
        with ColegioDB() as cursor:
            cursor.execute(cls._ELIMINAR, (idEstudiante,))

    @classmethod
    def seleccionarTodosLosEstudiantes(cls):
        with ColegioDB() as cursor:
            cursor.execute(cls._SELECCIONARTODOS)
            return cursor.fetchall()

    @classmethod
    def seleccionarAlgunosDatos(cls, idEstudiante):
        with ColegioDB() as cursor:
            cursor.execute(cls._SELECCIONARALGUNOSDATOS, (idEstudiante,))
            return cursor.fetchone()


if __name__ == '__main__':
    colegioDB = EstudianteDB()
    colegioDB.seleccionarEstudianteId(1)
