class MultimediaResourceManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.connection = None
        self.connected = False

    def connect(self, database):
        if not self.connected:
            # Código para conectarse a la base de datos
            self.connection = f"Conexión establecida con {database}"
            self.connected = True
            print("Conexión establecida.")
        else:
            print("Ya estás conectado a la base de datos.")

    def disconnect(self):
        if self.connected:
            # Código para cerrar la conexión con la base de datos
            self.connection = None
            self.connected = False
            print("Conexión cerrada.")
        else:
            print("No estás conectado a la base de datos.")


if __name__ == '__main__':
    # Uso del Singleton
    resource_manager1 = MultimediaResourceManager()
    resource_manager2 = MultimediaResourceManager()

    print(resource_manager1 is resource_manager2)  # Salida: True

    resource_manager1.connect("multimedia_db")
    resource_manager2.connect("another_db")

    resource_manager1.disconnect()
    resource_manager2.disconnect()
