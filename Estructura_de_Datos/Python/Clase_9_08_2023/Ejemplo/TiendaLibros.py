import locale
from Clase_9_08_2023.Ejemplo.Libro import Libro


class TiendaLibros:
    def __init__(self):
        locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
        self.catalogo = []
        self.valorTotal = 0

    def cargarLibros(self):
        dato = Libro("Harry Potter", "0011", 20_000)
        self.catalogo.append(dato)

        dato = Libro("Caballo de Troya", "0022", 15_000)
        self.catalogo.append(dato)

        dato = Libro("El señor de los anillos", "0033", 20_000)
        self.catalogo.append(dato)

        dato = Libro("Huevo del Cuco", "0044", 15_000)
        self.catalogo.append(dato)

        dato = Libro("Ready Player One", "0055", 20_000)
        self.catalogo.append(dato)

    def imprimirLibros(self):
        for libro in self.catalogo:
            print("Especificaciones del Libro".center(50, "-"))
            print(f"Nombre: {libro.nombre}"
                  f"\nIsbn: {libro.isbn}"
                  f"\nPrecio: {locale.currency(libro.precio, grouping=True)}")
            print("".center(50, "-"))

    def valorTotalLibros(self):
        for libro in self.catalogo:
            self.valorTotal += libro.precio
        print(f"El precio total de todos los libro es: {locale.currency(self.valorTotal, grouping=True)}")


if __name__ == '__main__':
    tiendaLibros = TiendaLibros()
    tiendaLibros.cargarLibros()
    tiendaLibros.imprimirLibros()
    tiendaLibros.valorTotalLibros()
