import ast
import socket

from BaseDeDatos.Estudiantes import EstudianteDB

# Crear un socket del servidor
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Definir la dirección y el puerto en el que el servidor escuchará
server_address = ('10.13.128.231', 12345)  # Cambia 'localhost' por la dirección IP del servidor si es necesario
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

        # Separa los datos para poder tratarlos y los convierte en una lista
        datos = data_from_client.split(";")

        # Opcion que se va a ejecutar
        opcion = datos[0]

        # Transformamos la lista que venia en String a List
        listaDatos = ast.literal_eval(datos[1])

        if opcion == "E1":
            EstudianteDB.ingresarEstudiante(
                nombres=listaDatos[0],
                apellidos=listaDatos[1],
                edad=listaDatos[2],
                sexo=listaDatos[3],
                telefono=listaDatos[4],
                correoElectronico=listaDatos[5]
            )
            client_socket.send("El estudiante se ha agregado correctamente".encode())
        elif opcion == "E2":
            datosEstudianteAntiguos = EstudianteDB.seleccionarAlgunosDatos(listaDatos[0])
            datosNuevos = []
            contador = 0

            for i in range(len(listaDatos)):
                if listaDatos[i] is not None:
                    datosNuevos.append(listaDatos[i])
                else:
                    datosNuevos.append(datosEstudianteAntiguos[i - 1])
                    contador += 1

            if contador != 4:
                EstudianteDB.actualizarEstudiante(
                    nombres=datosNuevos[1],
                    apellidos=datosNuevos[2],
                    telefono=datosNuevos[3],
                    correoElectronico=datosNuevos[4],
                    idEstudiante=datosNuevos[0]
                )
                client_socket.send("El estudiante se ha actualizado correctamente".encode())
            else:
                client_socket.send("No se han hecho cambios en el estudiante.".encode())

        elif opcion == "E3":
            # Extrae la informacion de la Base de Datos del estudiante que se solicito
            informacionEstudiante = EstudianteDB.seleccionarEstudianteId(int(listaDatos[0]))

            # Envia la informacion del estudiante al cliente
            client_socket.send(f"{informacionEstudiante}".encode())
        elif opcion == "E4":
            estudiantes = EstudianteDB.seleccionarTodosLosEstudiantes()
            client_socket.send(f"{estudiantes}".encode())
        elif opcion == "E5":
            EstudianteDB.eliminarEstudiante(int(listaDatos[0]))
            client_socket.send("El estudiante se ha eliminado correctamente".encode())
        elif opcion == "M2":
            client_socket.send("Esta opcion no esta disponible aun, estamos trabajando en ello".encode())
        elif opcion == "M3":
            # Envia informacion al cliente de que el servidor se cerro
            client_socket.send("Apagando el servidor...".encode())

            # El servidor se cierra
            server_socket.close()
            break
except Exception as e:
    print(f"{e}")
