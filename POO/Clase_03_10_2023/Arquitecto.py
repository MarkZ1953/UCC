from Empleado import Empleado, decoradorProfesion


class Arquitecto(Empleado):
    def __init__(self, identificacion, nombre, edad, estadoCivil, salario, numParticipacionProyectos):
        super().__init__(identificacion, nombre, edad, estadoCivil, salario)
        self.__numParticipacionProyectos = numParticipacionProyectos

    @property
    def getnumParticipacionProyectos(self):
        return self.__numParticipacionProyectos

    @decoradorProfesion("Arquitecto")
    def __str__(self):
        return (f"{super().__str__()}"
                f"\nNumero de participaciones en proyectos: {self.getnumParticipacionProyectos}")


if __name__ == '__main__':
    arquitecto1 = Arquitecto(1029980054,
                             "Felipe Castro",
                             18,
                             "Soltero",
                             6_500_000,
                             1_000)

    print(arquitecto1)
