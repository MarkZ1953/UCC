import locale


def decoradorProfesion(profesion=""):
    def decorador(funcion):
        print(f"{profesion}".center(50, "-"))
        resultado = funcion
        return resultado

    return decorador


class Empleado:
    locale.setlocale(locale.LC_ALL, 'es_CO.utf8')

    def __init__(self, identificacion, nombre, edad, estadoCivil, salario):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__edad = edad
        self.__estadoCivil = estadoCivil
        self.__salario = salario

    @property
    def getIdentificacion(self):
        return self.__identificacion

    @property
    def getNombre(self):
        return self.__nombre

    @property
    def getEdad(self):
        return self.__edad

    @property
    def getEstadoCivil(self):
        return self.__estadoCivil

    @property
    def getSalario(self):
        return self.__salario

    def __str__(self):
        return (f"Identificacion: {locale.format_string('%d', self.getIdentificacion, grouping=True)}"
                f"\nNombre: {self.getNombre}"
                f"\nEdad: {self.getEdad}"
                f"\nEstado Civil: {self.getEstadoCivil}"
                f"\nSalario: {locale.currency(self.getSalario, symbol=True, grouping=True)}")


if __name__ == '__main__':
    empleado1 = Empleado(1029980054,
                         "Felipe Castro",
                         18,
                         "Soltero",
                         6_500_000)

    print(empleado1)
