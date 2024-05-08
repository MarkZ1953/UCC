import matplotlib.pyplot as plt
import pandas as pd

# Datos de ejemplo (puedes reemplazar esto con tus propios datos)
calificaciones = [1, 2, 3, 4, 5]
frecuencia = [1000, 1500, 1200, 800, 300]  # Número de veces que cada calificación aparece

archivo_excel = 'ServicioPublicoBusetasVillavoV2.xlsx'

data = pd.read_excel(archivo_excel)

# Extrae la columna 'Nombre_Columna' como una Serie
columna_serie = data['Aseo']

# Convierte la Serie en una lista
columna_lista = columna_serie.tolist()

# Crear el gráfico de barras
plt.bar(calificaciones, frecuencia)

# Etiquetas y título del gráfico
plt.xlabel('Calificación')
plt.ylabel('Frecuencia')
plt.title('Distribución de Calificaciones')

# Mostrar el gráfico
plt.show()