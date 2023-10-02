import locale
from Empleado import Empleado, decoradorProfesion


class Programador(Empleado):
    locale.setlocale(locale.LC_ALL, 'es_CO.utf8')

    def __init__(self, identificacion, nombre, edad, estadoCivil, salario, lineasPorHora, lenguajeProgramacion):
        super().__init__(identificacion, nombre, edad, estadoCivil, salario)
        self.__lineasPorHora = lineasPorHora
        self.__lenguajeProgramacion = lenguajeProgramacion

    @property
    def getLineasPorHora(self):
        return self.__lineasPorHora

    @property
    def getLenguajeProgramacion(self):
        return self.__lenguajeProgramacion

    @decoradorProfesion("Programador")
    def __str__(self):
        return (f"{super().__str__()}"
                f"\nLineas por Hora: {locale.format_string('%d', self.getLineasPorHora, grouping=True)}"
                f"\nLenguaje de Programacion: {self.getLenguajeProgramacion}")


if __name__ == '__main__':
    programador1 = Programador(1029980054,
                               "Felipe Castro",
                               18,
                               "Soltero",
                               6_500_000,
                               1000,
                               "Python")

    print(programador1)
