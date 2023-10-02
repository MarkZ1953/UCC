from Empleado import Empleado, decoradorProfesion


class Director(Empleado):
    def __init__(self, identificacion, nombre, edad, estadoCivil, salario, aniosExperiencia):
        super().__init__(identificacion, nombre, edad, estadoCivil, salario)
        self.__aniosExperiencia = aniosExperiencia

    @property
    def getAniosExperiencia(self):
        return self.__aniosExperiencia

    @decoradorProfesion("Director")
    def __str__(self):
        return (f"{super().__str__()}"
                f"\nLineas por Hora: {self.getAniosExperiencia}")


if __name__ == '__main__':
    director1 = Director(1029980054,
                         "Felipe Castro",
                         18,
                         "Soltero",
                         6_500_000,
                         10)

    print(director1)
