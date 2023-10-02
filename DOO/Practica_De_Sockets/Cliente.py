import socket

# Crear un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto del servidor al que se conectará el cliente
server_address = ('127.0.0.1', 12345)  # Cambia 'localhost' por la dirección IP del servidor si es necesario

# Conectar al servidor
client_socket.connect(server_address)

message_to_server = "Hola, servidor"
client_socket.send(message_to_server.encode())

