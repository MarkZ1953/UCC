import locale
from Estructura_de_Datos.Clase_9_08_2023.Actividad.Estudiante import Estudiante


class Curso:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        self.notas = []
        self.sumaNotas = 0
        self.promedioNotas = 0
        self.notaMayor = 0
        self.notaMenor = 0
        self.estudiantesAprobados = 0
        self.curvaNotas = []

    def cargarEstudiante(self):
        dato = Estudiante(832193, "David Felipe", "Castro Lopez", "Estructura_de_Datos", 4.0)
        self.notas.append(dato)

        dato = Estudiante(818548, "Sergio Andres", "Arboleda Salinas", "Estructura_de_Datos", 2.0)
        self.notas.append(dato)

        dato = Estudiante(123456, "Carlitos Andres", "Arboleda Salinas", "Estructura_de_Datos", 3.7)
        self.notas.append(dato)

    def imprimirCurso(self):
        for libro in self.notas:
            print("Especificaciones del Libro".center(50, "-"))
            print(f"Nombre: {libro.nombre}"
                  f"\nIsbn: {libro.isbn}"
                  f"\nPrecio: {locale.currency(libro.precio, grouping=True)}")
            print("".center(50, "-"))

    def retornarPromedioNotas(self):
        for estudiante in self.notas:
            self.sumaNotas += estudiante.nota
        print(f"El promedio del curso es: {round(self.sumaNotas/len(self.notas), 2)}")

    def retornarEstudiantesAprobados(self):
        for estudiante in self.notas:
            if estudiante.nota >= 3:
                self.estudiantesAprobados += 1
        print(f"Aprobaron {self.estudiantesAprobados} estudiantes")

    def retornarNotaMenorYMayor(self):
        self.notaMayor = self.notas[0].nota
        self.notaMenor = self.notas[0].nota

        for estudiante in self.notas:
            if self.notaMayor < estudiante.nota:
                self.notaMayor = estudiante.nota
            if self.notaMenor > estudiante.nota:
                self.notaMenor = estudiante.nota

        print(f"La Nota mayor es: {self.notaMayor} | La Nota menor es: {self.notaMenor}")

    def retornarCurva(self):
        for estudiante in self.notas:
            self.curvaNotas.append(estudiante.nota)

        i = 0

        for nota in self.curvaNotas:
            if nota < 2:
                self.curvaNotas[i] = nota + 0.5
            elif 2.0 >= nota <= 3.5:
                self.curvaNotas[i] = nota + 0.7
            elif 3.5 < nota <= 5:
                if nota + 1 > 5:
                    self.curvaNotas[i] = 5.0
                else:
                    self.curvaNotas[i] = nota + 1.0

            i += 1

        print(f"Las notas de los estudiantes con curva son: {self.curvaNotas}")


if __name__ == '__main__':
    Curso = Curso()
    Curso.cargarEstudiante()
    # Curso.imprimirCurso()
    Curso.retornarPromedioNotas()
    Curso.retornarNotaMenorYMayor()
    Curso.retornarEstudiantesAprobados()
    Curso.retornarCurva()
