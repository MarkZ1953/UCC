class Estudiante:
    def __init__(self, codigo, nombres, apellidos, asignatura, nota):
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos
        self.__asignatura = asignatura
        self.__nota = nota

    @property
    def nombres(self):
        return self.__nombres

    @property
    def codigo(self):
        return self.__codigo

    @property
    def asignatura(self):
        return self.__asignatura

    @property
    def nota(self):
        return self.__nota

    @property
    def apellidos(self):
        return self.__apellidos
