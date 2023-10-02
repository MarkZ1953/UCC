import socket

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto en el que el servidor escuchará
server_address = ('127.0.0.1', 12345)  # Cambia 'localhost' por la dirección IP del servidor si es necesario
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(5)  # Acepta hasta 5 conexiones entrantes

# Esperar a que un cliente se conecte

print("El servidor está esperando conexiones...")
client_socket, client_address = server_socket.accept()
print(f"Se ha establecido una conexión con {client_address}")

try:
    while True:
        data_from_client = client_socket.recv(1024).decode()
        datos = data_from_client.split(";")
        opcion = datos[0]
        dato2 = datos[1]

        if opcion == "1":
            client_socket.send("Se ha agregado correctamente el estudiante".encode())
        elif opcion == "2":
            client_socket.send("Se ha eliminado correctamente el estudiante".encode())
        elif opcion == "3":
            client_socket.send("Apagando el servidor...".encode())
            server_socket.close()
            break
except Exception as e:
    print(f"{e}")
