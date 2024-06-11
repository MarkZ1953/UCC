from texttable import Texttable

# table = Texttable()


class CalculadoraNotasUCC:
    def __init__(self) -> None:
        self.notas = {}
        self.ejecutarCalculadora()
        
    def ejecutarCalculadora(self):
        while True:
            self.mostrarMenu()
            opcionMenu = int(input("Ingrese una opcion: "))
            
            if opcionMenu == 1:
                self.calcularNotas()
            if opcionMenu == 5:
                break 

    def calcularNotas(self):
        cantidadMaterias = int(input("Ingrese la cantidad de materias: "))
        promedio: float = 0
        sumaCreditos: int = 0
        sumaNotas: float = 0

        for i in range(cantidadMaterias):
            nombreMateria = input("Ingrese el nombre de la materia: ")
            creditosMateria = int(input("Ingrese los creditos de la materia: "))
            calificacionMateria = float(input("Ingrese la calificacion de la materia: "))
            notaMateria = int(creditosMateria) * float(calificacionMateria)

            sumaCreditos += creditosMateria
            sumaNotas += notaMateria

            self.notas[nombreMateria] = {
                "creditos": creditosMateria,
                "calificacion": calificacionMateria,
                "nota": notaMateria
            }

        promedio = sumaNotas / sumaCreditos

        self.mostrarTablaCalificaciones(self.notas)
        
        print(f"Su promedio es de: {round(promedio, 3)}")
    
    def mostrarTablaCalificaciones(self, notas):
        tablaCalificaciones = Texttable()
        tablaCalificaciones.add_row(["Nombre", "Creditos", "Calificacion", "Nota"])

        print(notas)
        
        for nombreMateria, detalles in notas.items():
            tablaCalificaciones.add_row([nombreMateria, detalles["creditos"], detalles["calificacion"], detalles["nota"]])

        print(tablaCalificaciones.draw())

    def guardarNotas(self):
        pass

    def actualizarNota(self):
        pass

    def mostrarMenu(self):
        print("Calculadora Notas UCC".center(50, "="))
        print("1. Calcular notas")
        print("2. Calcular promedio ponderado")
        print("3. Guardar notas")
        print("4. ")
        print("5. Salir")
        print("".center(50, "="))
