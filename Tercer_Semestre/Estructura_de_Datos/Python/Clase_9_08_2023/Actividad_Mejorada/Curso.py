import locale

from Estructura_de_Datos.Clase_9_08_2023.Actividad_Mejorada.Estudiante import Estudiante


class Curso:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        self.notas = {}
        self.estudiantes = {}

        self.sumaNotas = 0
        self.promedioNotas = 0

        # Definimos las variables para almacenar la nota mayor y menos del curso.
        self.notaMayor = 0
        self.notaMenor = 0

        self.estudiantesAprobados = 0
        self.curvaNotas = []

        while True:
            print("Sistema de Control de Estudiantes".center(80, "-"))
            print("1. Ingresar Estudiante"
                  "\n2. Eliminar Estudiante"
                  "\n3. Buscar Estudiante"
                  "\n4. Ingresar Nota"
                  "\n5. Obtener Promedio del Curso"
                  "\n6. Obtener Estudiantes Aprobados y Reprobados"
                  "\n7. Obtener la Nota Mayor y Menor de un Curso"
                  "\n8. Salir")

            eleccion = input("Ingrese una de las opciones con el indice numerico: ")

            if eleccion.isdigit():
                if int(eleccion) == 1:
                    self.ingresarEstudiante()
                elif int(eleccion) == 2:
                    pass
                elif int(eleccion) == 3:
                    self.buscarEstudiante()
                elif int(eleccion) == 4:
                    pass
                elif int(eleccion) == 5:
                    pass
                elif int(eleccion) == 6:
                    pass
                elif int(eleccion) == 7:
                    pass
                elif int(eleccion) == 8:
                    pass
                elif int(eleccion) == 9:
                    print("Saliendo...")
                    break
            else:
                print("ERROR".center(50, "*"))
                print("Debes ingresar un numero, vuelve a intentarlo.")
                print("".center(50, "*"))

    def ingresarEstudiante(self):
        codigo = int(input("Ingrese los Nombres del Estudiante: "))
        nombres = input("Ingrese los Nombres del Estudiante: ")
        apellidos = input("Ingrese los Nombres del Estudiante: ")

        # Creamos un estudiante de la clase Estudiante
        estudiante = Estudiante(codigo, nombres, apellidos)

        # Asociamos en un diccionario el codigo del estudiante con el objeto estudiante
        self.estudiantes[codigo] = estudiante

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
        print(f"El promedio del curso es: {round(self.sumaNotas / len(self.notas), 2)}")

    def buscarEstudiante(self):
        codigo = int(input("Ingrese el Codigo del Estudiante: "))
        print("Informacion del Estudiante".center(50, "-"))
        print(f"Codigo: {self.estudiantes[codigo].codigo}"
              f"\nNombres: {self.estudiantes[codigo].nombres}"
              f"\nApellidos: {self.estudiantes[codigo].apellidos}")
        print("".center(50, "-"))

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
    # Curso.cargarEstudiante()
    # # Curso.imprimirCurso()
    # Curso.retornarPromedioNotas()
    # Curso.retornarNotaMenorYMayor()
    # Curso.retornarEstudiantesAprobados()
    # Curso.retornarCurva()

# Hacer un menu
# Hacer que se puedan agregar la cantidad de estudiantes que se deseen
