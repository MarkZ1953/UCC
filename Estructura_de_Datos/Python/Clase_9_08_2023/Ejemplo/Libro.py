class Libro:
    def __init__(self, nombre, isbn, precio):
        self.__nombre = nombre
        self.__isbn = isbn
        self.__precio = precio

    @property
    def nombre(self):
        return self.__nombre

    @property
    def isbn(self):
        return self.__isbn

    @property
    def precio(self):
        return self.__precio
