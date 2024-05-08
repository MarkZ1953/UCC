class Olimipadas:
    def __init__(self):
        self.valorN = 0
        self.arregloA = []
        self.arregloB = []

        while True:
            print("Ingrese una opcion (Con el indice numerico): ")
            print("1. Hacer prueba")
            print("2. Imprimir arreglos")
            print("3. Salir")

            opcion = int(input())

            if opcion == 1:
                self.arregloA.clear()
                self.arregloB.clear()

                self.cargarNumeros()

                if self.condicionArreglos():
                    print("Yes")
                else:
                    self.comprobarIntercambios()
            elif opcion == 2:
                self.imprimirArreglos()
            elif opcion == 3:
                break

    def cargarNumeros(self):
        self.valorN = int(input("Ingrese la cantidad de valores que desea ingresar: "))

        for i in range(self.valorN):
            numeroTemp = int(input(f"Ingrese el {i} numero de A: "))
            if numeroTemp > 0:
                self.arregloA.append(numeroTemp)
            else:
                print("Debes ingresar un numero mayor a 0")
                i -= 1

        for i in range(self.valorN):
            numeroTemp = int(input(f"Ingrese el {i} numero de B: "))
            if numeroTemp > 0:
                self.arregloB.append(numeroTemp)
            else:
                print("Debes ingresar un numero mayor a 0")
                i -= 1

    def obtenerNumeroMayorB(self):
        numeroMayorB = self.arregloB[0]
        posicionMayorB = 0

        for i in range(len(self.arregloB)):
            if numeroMayorB <= self.arregloB[i]:
                numeroMayorB = self.arregloB[i]
                posicionMayorB = i

        return numeroMayorB, posicionMayorB

    def obtenerNumeroMayorA(self):
        numeroMayorA = self.arregloA[0]
        posicionMayorA = 0

        for i in range(len(self.arregloB)):
            if numeroMayorA <= self.arregloA[i]:
                numeroMayorA = self.arregloA[i]
                posicionMayorA = i

        return numeroMayorA, posicionMayorA

    def condicionArreglos(self):
        numeroMayorA, posicionMayorA = self.obtenerNumeroMayorA()
        numeroMayorB, posicionMayorB = self.obtenerNumeroMayorB()

        if (len(self.arregloA) == posicionMayorA + 1) and (len(self.arregloB) == posicionMayorB + 1):
            return True

    def imprimirArreglos(self):
        print(self.arregloA, self.arregloB)

    def comprobarIntercambios(self):
        tempArregloA = []
        tempArregloB = []
        tempArregloA.extend(self.arregloA)
        tempArregloB.extend(self.arregloB)

        for k in range(self.valorN):
            tempValorA = self.arregloA[k]
            tempValorB = self.arregloB[k]

            tempArregloA.pop(k)
            tempArregloA.insert(k, tempValorB)

            tempArregloB.pop(k)
            tempArregloB.insert(k, tempValorA)

            numeroMayorA = self.arregloB[0]
            posicionMayorA = 0

            for i in range(len(self.arregloB)):
                if numeroMayorA <= tempArregloA[i]:
                    numeroMayorA = tempArregloA[i]
                    posicionMayorA = i

            numeroMayorB = self.arregloB[0]
            posicionMayorB = 0

            for j in range(len(self.arregloB)):
                if numeroMayorB <= tempArregloB[j]:
                    numeroMayorB = tempArregloB[j]
                    posicionMayorB = j

            # print(f"Posicion A: {posicionMayorA}")
            # print(f"Numero Mayor A: {numeroMayorA}")
            # print(f"Arreglo A: {tempArregloA}")
            # print("".center(20, "-"))
            # print(f"Posicion B: {posicionMayorB}")
            # print(f"Numero Mayor B: {numeroMayorB}")
            # print(f"Arreglo B: {tempArregloB}")

            if (len(tempArregloA) == posicionMayorA + 1) and (len(tempArregloB) == posicionMayorB + 1):
                print("Yes")
                self.arregloA = tempArregloA
                self.arregloB = tempArregloB
                break
            else:
                if self.valorN == k + 1:
                    print("No")


if __name__ == '__main__':
    app = Olimipadas()

    # print(f"El numero mayor de el Arreglo A es: {app.obtenerNumeroMayorA()}")
    # print(f"El numero mayor de el Arreglo B es: {app.obtenerNumeroMayorB()}")
