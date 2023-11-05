import locale
import socket


def menuPrincipal():
    print("MENU PRINCIPAL".center(50, "-"))
    print("1. Hacer una operacion basica (+, -, /, *)")
    print("2. Hallar raiz")
    print("3. Cerrar Conexion con Servidor")
    print("".center(50, "-"))
    opcion = int(input("Ingresa una opcion: "))
    return opcion


def iniciarCliente():
    locale.setlocale(locale.LC_NUMERIC, 'es_CO.UTF-8')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.228.236', 12345))

    while True:

        opcion = menuPrincipal()

        if opcion == 1:
            operacion = input("Ingresa una operacion: ")
            client_socket.send(f"M1:{operacion}".encode())

            response = client_socket.recv(1024).decode()
            print("Respuesta: ", locale.format_string("%d", float(response), grouping=True))
        elif opcion == 2:
            numeroRaiz = input("Ingresa un numero: ")
            client_socket.send(f"M2:{numeroRaiz}".encode())

            response = client_socket.recv(1024).decode()
            print("Respuesta: ", locale.format_string("%d", float(response), grouping=True))
        elif opcion == 3:
            break


if __name__ == '__main__':
    iniciarCliente()