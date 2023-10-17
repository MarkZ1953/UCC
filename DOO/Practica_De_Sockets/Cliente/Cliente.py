import ast
import socket
from datetime import datetime

# Crear un socket del cliente
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto del servidor al que se conectará el cliente
server_address = ('192.168.100.12', 12345)  # Cambia 'localhost' por la dirección IP del servidor si es necesario


def calcularEdad(fechaNacimiento):
    fecha_nacimiento = datetime.strptime(f'{fechaNacimiento}', '%d/%m/%Y')
    fecha_actual = datetime.now()
    edad = fecha_actual.year - fecha_nacimiento.year - (
            (fecha_actual.month, fecha_actual.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    return edad


def mostrarMenuEstudiantes():
    print("ESTUDIANTES".center(50, "-"))
    print("1. Ingresar un estudiante")
    print("2. Actualizar informacion de un estudiante")
    print("3. Seleccionar un estudiante")
    print("4. Seleccionar todos los estudiantes")
    print("5. Eliminar un estudiante")
    print("6. Volver al menu principal")
    print("".center(50, "-"))
    opcion = int(input("Ingrese una opcion (Estudiante): "))
    return opcion


def mostrarMenuNotas():
    print("NOTAS".center(50, "-"))
    print("1. Ingresar nota a un estudiante")
    print("2. Actualizar nota de un estudiante")
    print("3. Seleccionar notas de un estudiante")
    print("4. Eliminar nota de un estudiante")
    print("5. Volver al menu principal")
    opcion = int(input("Ingrese una opcion (Notas): "))
    print("".center(50, "-"))
    return opcion


def mostrarMenuPrincipal():
    print("MENU PRINCIPAL".center(50, "-"))
    print("1. Estudiantes \n"
          "2. Calificaciones \n"
          "3. Salir")
    print("".center(50, "-"))
    opcion = int(input("Ingrese una opcion (Menu Principal): "))
    return opcion


try:
    # Conectar al servidor
    client_socket.connect(server_address)

    while True:
        datos = []
        opcion = mostrarMenuPrincipal()

        if opcion == 1:
            opcionEstudiantes = mostrarMenuEstudiantes()

            if opcionEstudiantes == 1:
                nombreEstudiante = input("Ingrese los nombres del estudiante: ")
                datos.append(nombreEstudiante)

                apellidosEstudiante = input("Ingrese los apellidos del estudiante: ")
                datos.append(apellidosEstudiante)

                fechaNacimiento = input("Ingrese la fecha de nacimiento del estudiante: ")
                datos.append(fechaNacimiento)

                sexo = input("Ingrese el sexo del estudiante: ")
                datos.append(sexo)

                telefono = int(input("Ingrese el numero telefonico del estudiante: "))
                datos.append(telefono)

                correoElectronico = input("Ingrese el correo electronico del estudiante: ")
                datos.append(correoElectronico)

                client_socket.send(f"E1;{datos}".encode())

                print("".center(50, "-"))
                respuestaServidor = client_socket.recv(1024).decode()
                print(respuestaServidor)
            elif opcionEstudiantes == 2:
                nombreDatos = ["nombres", "apellidos", "telefono", "correo electronico"]
                idEstudiante = int(input("Ingresa el Id del Estudiante: "))
                datos.append(idEstudiante)

                for i in range(len(nombreDatos)):
                    opcion = input(f"¿Desea actualizar {nombreDatos[i]}? (y/n):")
                    if opcion.lower() == "y":
                        dato = input(f"Ingrese {nombreDatos[i]}: ")
                        datos.append(dato)
                    else:
                        datos.append(None)

                client_socket.send(f"E2;{datos}".encode())

                print("".center(50, "-"))
                respuestaServidor = client_socket.recv(1024).decode()
                print(respuestaServidor)
            elif opcionEstudiantes == 3:
                print("".center(50, "-"))
                idEstudiante = int(input("Ingresa el Id del Estudiante: "))
                datos.append(idEstudiante)
                client_socket.send(f"E3;{datos}".encode())

                print("".center(50, "-"))
                respuestaServidor = client_socket.recv(1024).decode()
                informacionEstudiante = ast.literal_eval(respuestaServidor)

                print((f"Id Estudiante: {informacionEstudiante[0]} \n"
                       f"Nombres: {informacionEstudiante[1]} \n"
                       f"Apellidos: {informacionEstudiante[2]} \n"
                       f"Edad: {calcularEdad(informacionEstudiante[3])} \n"
                       f"Sexo: {informacionEstudiante[4]} \n"
                       f"Telefono: {informacionEstudiante[5]} \n"
                       f"Correo: {informacionEstudiante[6]}"))

            elif opcionEstudiantes == 4:
                client_socket.send(f"E4;{datos}".encode())
                respuestaServidor = client_socket.recv(1024).decode()
                print("".center(50, "-"))

                for estudiante in ast.literal_eval(respuestaServidor):
                    print("\n"
                          f"Id Estudiante: {estudiante[0]} \n"
                          f"Nombres: {estudiante[1]} \n"
                          f"Apellidos: {estudiante[2]} \n"
                          f"Edad: {calcularEdad(estudiante[3])} \n"
                          f"Sexo: {estudiante[4]} \n"
                          f"Telefono: {estudiante[5]} \n"
                          f"Correo: {estudiante[6]}")

                print("")
            elif opcionEstudiantes == 5:
                idEstudiante = int(input("Ingresa el Id del Estudiante: "))
                datos.append(idEstudiante)
                client_socket.send(f"E5;{datos}".encode())

                print("".center(50, "-"))
                respuestaServidor = client_socket.recv(1024).decode()
                print(respuestaServidor)
            elif opcionEstudiantes == 6:
                print("".center(50, "-"))
                print("Volviendo al Menu Principal...")

        elif opcion == 2:
            client_socket.send(f"M2;{None}".encode())
            print("".center(50, "-"))
            respuestaServidor = client_socket.recv(1024).decode()
            print(respuestaServidor)
        elif opcion == 3:
            client_socket.send(f"M3;{None}".encode())

            print("".center(50, "-"))
            respuestaServidor = client_socket.recv(1024).decode()
            print(respuestaServidor)
            break

except Exception as e:
    print(f"{e}")

finally:
    # Cerrar la conexión del cliente
    client_socket.close()
