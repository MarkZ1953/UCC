class Olimipadas:
    def __init__(self):
        self.casos = []
        self.arregloA = []
        self.arregloB = []
        valorN = 0

        self.casos = self.formal()

        contador = 0

        for i in range(len(self.casos)):

            if contador == 0:
                valorN = int(self.casos[i])
                contador += 1
            elif contador == 1:
                self.arregloA = self.casos[i].split()
                contador += 1
            elif contador == 2:
                self.arregloB = self.casos[i].split()
                contador += 1

            if contador == 3:
                if self.condicionArreglos():
                    print("Yes")
                else:
                    self.comprobarIntercambios(valorN)

                self.arregloA.clear()
                self.arregloB.clear()
                contador = 0

        # while True:
        #     print("Ingrese una opcion (Con el indice numerico): ")
        #     print("1. Hacer prueba")
        #     print("2. Imprimir arreglos")
        #     print("3. Salir")
        #
        #     opcion = int(input())
        #
        #     if opcion == 1:

        #
        #         # self.cargarNumeros()
        #
        #
        #
        #     elif opcion == 2:
        #         self.imprimirArreglos()
        #     elif opcion == 3:
        #         break

    # def cargarNumeros(self):
    #     self.valorN = int(input("Ingrese la cantidad de valores que desea ingresar: "))
    #
    #     for i in range(self.valorN):
    #         numeroTemp = int(input(f"Ingrese el {i} numero de A: "))
    #         if numeroTemp > 0:
    #             self.arregloA.append(numeroTemp)
    #         else:
    #             print("Debes ingresar un numero mayor a 0")
    #             i -= 1
    #
    #     for i in range(self.valorN):
    #         numeroTemp = int(input(f"Ingrese el {i} numero de B: "))
    #         if numeroTemp > 0:
    #             self.arregloB.append(numeroTemp)
    #         else:
    #             print("Debes ingresar un numero mayor a 0")
    #             i -= 1

    def obtenerNumeroMayorB(self):
        numeroMayorB = int(self.arregloB[0])
        posicionMayorB = 0

        for i in range(len(self.arregloB)):
            if numeroMayorB <= int(self.arregloB[i]):
                numeroMayorB = int(self.arregloB[i])
                posicionMayorB = i

        return numeroMayorB, posicionMayorB

    def obtenerNumeroMayorA(self):
        numeroMayorA = int(self.arregloA[0])
        posicionMayorA = 0

        for i in range(len(self.arregloB)):
            if numeroMayorA <= int(self.arregloA[i]):
                numeroMayorA = int(self.arregloA[i])
                posicionMayorA = i

        return numeroMayorA, posicionMayorA

    def condicionArreglos(self):
        numeroMayorA, posicionMayorA = self.obtenerNumeroMayorA()
        numeroMayorB, posicionMayorB = self.obtenerNumeroMayorB()

        if (len(self.arregloA) == posicionMayorA + 1) and (len(self.arregloB) == posicionMayorB + 1):
            return True

    def imprimirArreglos(self):
        print(self.arregloA, self.arregloB)

    def comprobarIntercambios(self, valorN):
        tempArregloA = []
        tempArregloB = []
        tempArregloA.extend(self.arregloA)
        tempArregloB.extend(self.arregloB)

        for k in range(valorN):
            tempValorA = int(self.arregloA[k])
            tempValorB = int(self.arregloB[k])

            tempArregloA.pop(k)
            tempArregloA.insert(k, tempValorB)

            tempArregloB.pop(k)
            tempArregloB.insert(k, tempValorA)

            numeroMayorA = int(self.arregloB[0])
            posicionMayorA = 0

            for i in range(len(self.arregloB)):
                if numeroMayorA <= int(tempArregloA[i]):
                    numeroMayorA = int(tempArregloA[i])
                    posicionMayorA = i

            numeroMayorB = int(self.arregloB[0])
            posicionMayorB = 0

            for j in range(len(self.arregloB)):
                if numeroMayorB <= int(tempArregloB[j]):
                    numeroMayorB = int(tempArregloB[j])
                    posicionMayorB = j

            if (len(tempArregloA) == posicionMayorA + 1) and (len(tempArregloB) == posicionMayorB + 1):
                print("Yes")
                self.arregloA = tempArregloA
                self.arregloB = tempArregloB
                break
            else:
                if valorN == k + 1:
                    print("No")

    def formal(self):
        with open("TestCases/test_cases3.txt") as fp:
            lines = [line.rstrip() for line in fp]
            del lines[0]
            return lines


if __name__ == '__main__':
    app = Olimipadas()

    # print(f"El numero mayor de el Arreglo A es: {app.obtenerNumeroMayorA()}")
    # print(f"El numero mayor de el Arreglo B es: {app.obtenerNumeroMayorB()}")
