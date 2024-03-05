class Shape:
    def draw(self):
        pass


class Rectangle(Shape):
    def draw(self):
        print("Dibujando un rectángulo")


class Circle(Shape):
    def draw(self):
        print("Dibujando un círculo")


class ShapeFactory:
    def get_shape(self, shape_type):
        pass


class RoundedShapeFactory(ShapeFactory):
    def get_shape(self, shape_type):
        if shape_type == "rectangle":
            return RoundedRectangle()
        elif shape_type == "circle":
            return RoundedCircle()
        else:
            raise ValueError("Tipo de forma desconocido")


class RoundedRectangle(Rectangle):
    def draw(self):
        print("Dibujando un rectángulo redondeado")


class RoundedCircle(Circle):
    def draw(self):
        print("Dibujando un círculo redondeado")


# Uso del Abstract Factory
abstract_factory = RoundedShapeFactory()
rounded_rectangle = abstract_factory.get_shape("rectangle")
rounded_circle = abstract_factory.get_shape("circle")

rounded_rectangle.draw()  # Salida: Dibujando un rectángulo redondeado
rounded_circle.draw()  # Salida: Dibujando un círculo redondeado
