class Vehicle:
    def drive(self):
        pass


class Car(Vehicle):
    def drive(self):
        print("Conduciendo un automóvil.")


class Truck(Vehicle):
    def drive(self):
        print("Conduciendo un camión.")


class VehicleFactory:
    def create_vehicle(self, vehicle_type):
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        else:
            raise ValueError("Tipo de vehículo desconocido")


if __name__ == '__main__':
    # Uso del Factory Method
    factory = VehicleFactory()
    car = factory.create_vehicle("car")
    truck = factory.create_vehicle("truck")

    car.drive()  # Salida: Conduciendo un automóvil.
    truck.drive()  # Salida: Conduciendo un camión.
