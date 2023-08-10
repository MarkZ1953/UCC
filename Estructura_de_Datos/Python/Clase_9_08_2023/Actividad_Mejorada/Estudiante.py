

class Estudiante:
    def __init__(self, codigo, nombres, apellidos):
        self.__codigo = codigo
        self.__nombres = nombres
        self.__apellidos = apellidos

    @property
    def nombres(self):
        return self.__nombres

    @property
    def codigo(self):
        return self.__codigo

    @property
    def apellidos(self):
        return self.__apellidos
