# Crear un diccionario vacío para almacenar los datos
registro_notas = {}

# Agregar datos de un estudiante a una materia
codigo_estudiante = "123"
materia = "Matematicas"
notas = [85, 90, 78, 95, 88]

# Verificar si el código del estudiante ya existe en el diccionario
if codigo_estudiante in registro_notas:
    # Si existe, agregar la materia y las notas a su diccionario interno
    registro_notas[codigo_estudiante][materia] = notas
else:
    # Si no existe, crear un nuevo diccionario interno para el estudiante
    registro_notas[codigo_estudiante] = {materia: notas}

# Mostrar el diccionario completo
print(registro_notas)
