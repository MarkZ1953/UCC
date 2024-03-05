class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = "Soy un Singleton"


# Uso del Singleton
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1.value)  # Salida: Soy un Singleton
print(singleton2.value)  # Salida: Soy un Singleton
print(singleton1 is singleton2)  # Salida: True
