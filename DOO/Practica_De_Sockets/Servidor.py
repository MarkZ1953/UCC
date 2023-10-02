import socket

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto en el que el servidor escuchará
server_address = ('127.0.0.1', 12345)  # Cambia 'localhost' por la dirección IP del servidor si es necesario
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(5)  # Acepta hasta 5 conexiones entrantes

print("El servidor está esperando conexiones...")

# Esperar a que un cliente se conecte
client_socket, client_address = server_socket.accept()

print(f"Se ha establecido una conexión con {client_address}")

data_from_client = client_socket.recv(1024).decode()
print(f"El cliente dice: {data_from_client}")

