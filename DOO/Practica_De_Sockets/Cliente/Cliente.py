import socket

# Crear un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto del servidor al que se conectará el cliente
server_address = ('127.0.0.1', 12345)  # Cambia 'localhost' por la dirección IP del servidor si es necesario

try:
    # Conectar al servidor
    client_socket.connect(server_address)

    while True:
        datos = []
        print("MENU".center(30, "-"))
        print("1. Ingresar un estudiante")
        print("2. Eliminar un estudiante")
        print("3. Salir")
        print("".center(30, "-"))

        opcion = int(input("Ingresa una opcion: "))

        if opcion == 1:
            datos.append("Felipe")
            datos.append("Castro")
            datos.append(18)
            client_socket.send(f"1;{datos}".encode())
        elif opcion == 2:
            client_socket.send(f"2;{datos}".encode())
        elif opcion == 3:
            client_socket.send(f"3;{None}".encode())
            data_from_server = client_socket.recv(1024).decode()
            print(f"El servidor dice: {data_from_server}")
            break

        data_from_server = client_socket.recv(1024).decode()
        print(f"El servidor dice: {data_from_server}")

except Exception as e:
    print(f"{e}")

finally:
    # Cerrar la conexión del cliente
    client_socket.close()
