import socket
import threading
from math import sqrt


class Servidor:

    def manejoCliente(self, client_socket, address):
        while True:
            request = client_socket.recv(1024)

            if not request:
                print(f"Cliente {address} desconectado.")
                break
            datos = request.decode().split(":")
            opcion = datos[0]

            if opcion == "M1":
                operacion = eval(datos[1])
                client_socket.send(str(operacion).encode())
            elif opcion == "M2":
                operacion = sqrt(float(datos[1]))
                client_socket.send(str(operacion).encode())

        client_socket.close()

    def iniciarServidor(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('192.168.228.236', 12345))
        server_socket.listen(5)

        try:
            while True:
                client, address = server_socket.accept()
                client_handler = threading.Thread(target=self.manejoCliente, args=(client, address))
                client_handler.start()
        except Exception as e:
            print(e)
        finally:
            server_socket.close()


if __name__ == '__main__':
    servidor = Servidor()
    servidor.iniciarServidor()