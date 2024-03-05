import copy


def singleton(cls):
    instances = dict()

    def wrap(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)

        return instances[cls]

    return wrap


@singleton
class MultimediaResourceManager():
    def __init__(self):
        super().__init__()
        self.connection = False

    def connect(self, database):
        if not self.connection:
            # Código para conectarse a la base de datos
            self.connection = True
            print(f"Conexión establecida con {database}.")
        else:
            print("Ya estás conectado a la base de datos.")

    def disconnect(self):
        if self.connection:
            # Código para cerrar la conexión con la base de datos
            self.connection = False
            print("Conexión cerrada.")
        else:
            print("No estás conectado a la base de datos.")


# Uso del Singleton
resource_manager1 = MultimediaResourceManager()
resource_manager2 = MultimediaResourceManager()

print(resource_manager1 is resource_manager2)  # Salida: True

resource_manager1.connect("multimedia_db")
resource_manager1.connect("multimedia_db")
resource_manager1.connect("multimedia_db")

resource_manager1.disconnect()
resource_manager2.disconnect()
