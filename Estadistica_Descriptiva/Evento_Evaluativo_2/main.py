import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate


class ServiciosPublicosVillavicencio:
    def __init__(self):
        # Se obtiene la informacion del archivo Excel con la ruta del archivo
        self.informacionExcel = pd.read_excel('ServicioPublicoBusetasVillavoV2.xlsx')

        # Creamos una lista con los valores de calificacion del 1 al 5
        self.calificaciones = [1, 2, 3, 4, 5]

    def obtenerGraficaCalificacionesAseo(self):
        columnaAseo = self.informacionExcel['Aseo']
        columnaAseo = columnaAseo.tolist()
        frecuencia = [0, 0, 0, 0, 0]

        # Datos de ejemplo
        etiquetas = ['1', '2', '3', '4', '5']

        # Colores para cada porción del gráfico
        colores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']

        # Título del gráfico
        plt.title('Calificacion Aseo')

        for calificacion in columnaAseo:
            if calificacion == 1:
                frecuencia[0] += 1
            elif calificacion == 2:
                frecuencia[1] += 1
            elif calificacion == 3:
                frecuencia[2] += 1
            elif calificacion == 4:
                frecuencia[3] += 1
            elif calificacion == 5:
                frecuencia[4] += 1

        # Crear el gráfico de barras
        plt.bar(etiquetas, frecuencia, color=colores, edgecolor="black")

        plt.yticks(range(0, max(frecuencia) + 1, 100))

        print(frecuencia)

        # Mostrar el gráfico
        plt.show()

    def obtenerGraficaCalificacionesSeguridad(self):
        columnaAseo = self.informacionExcel['Seguridad']
        columnaAseo = columnaAseo.tolist()
        frecuencia = [0, 0, 0, 0, 0]

        # Datos de ejemplo
        etiquetas = ['1', '2', '3', '4', '5']

        # Colores para cada porción del gráfico
        colores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']

        # Explota (destaca) la porción de la calificación '3' (opcional)
        explode = (0, 0, 0, 0, 0)

        # Título del gráfico
        plt.title('Calificacion Seguridad')

        for calificacion in columnaAseo:
            if calificacion == 1:
                frecuencia[0] += 1
            elif calificacion == 2:
                frecuencia[1] += 1
            elif calificacion == 3:
                frecuencia[2] += 1
            elif calificacion == 4:
                frecuencia[3] += 1
            elif calificacion == 5:
                frecuencia[4] += 1

        # Crear el gráfico de pastel
        plt.pie(frecuencia, colors=colores, autopct='%1.1f%%', startangle=140, explode=explode, pctdistance=0.85)

        # Agregar un círculo en el centro para crear el agujero (gráfico de dona)
        centro_circulo = plt.Circle((0, 0), 0.7, color='white')
        fig = plt.gcf()
        fig.gca().add_artist(centro_circulo)

        # Agregar leyendas por color
        leyendas_por_color = [f'{etiqueta}: {frecuencia[i]}' for i, etiqueta in enumerate(etiquetas)]
        plt.legend(leyendas_por_color, loc="center right")

        # Mostrar el gráfico
        plt.axis('equal')  # Esto garantiza que el gráfico de pastel sea circular

        plt.show()

    def obtenerGraficaCalificacionesDiasUsoSemanal(self):
        columnaAseo = self.informacionExcel['DiasUsoSemanal']
        columnaAseo = columnaAseo.tolist()
        frecuencia = [0, 0, 0, 0, 0, 0, 0]

        # Datos de ejemplo
        etiquetas = ['1', '2', '3', '4', '5', '6', '7']

        # Colores para cada porción del gráfico
        colores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink', 'lightsteelblue', 'lightgray']

        # Explota (destaca) la porción de la calificación '3' (opcional)
        explode = (0.1, 0.2, 0, 0, 0, 0, 0)

        # Título del gráfico
        plt.title('Dias Uso Semanal')

        for calificacion in columnaAseo:
            if calificacion == 1:
                frecuencia[0] += 1
            elif calificacion == 2:
                frecuencia[1] += 1
            elif calificacion == 3:
                frecuencia[2] += 1
            elif calificacion == 4:
                frecuencia[3] += 1
            elif calificacion == 5:
                frecuencia[4] += 1
            elif calificacion == 6:
                frecuencia[5] += 1
            elif calificacion == 7:
                frecuencia[6] += 1

        # Crear el gráfico de pastel
        plt.pie(frecuencia, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=140, explode=explode)
        print(frecuencia)

        # Agregar leyendas por color
        leyendas_por_color = [f'{etiqueta}: {frecuencia[i]}' for i, etiqueta in enumerate(etiquetas)]
        plt.legend(leyendas_por_color, loc="center right")

        # Mostrar el gráfico
        plt.axis('equal')  # Esto garantiza que el gráfico de pastel sea circular
        plt.show()

    def obtenerGraficaCalificacionesFrecuenciaPlataformas(self):
        columnaAseo = self.informacionExcel['FrecPlataformas']
        columnaAseo = columnaAseo.tolist()
        frecuencia = [0, 0, 0, 0]

        # Datos de ejemplo
        etiquetas = ['Nunca', 'Una vez por semana', 'Dos veces por semana', 'Tres o mas veces por semana']

        # Colores para cada porción del gráfico
        colores = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']

        # Explota (destaca) la porción de la calificación '3' (opcional)
        explode = (0, 0, 0, 0)

        # Título del gráfico
        plt.title('Calificacion Seguridad')

        for calificacion in columnaAseo:
            if calificacion == "Nunca":
                frecuencia[0] += 1
            elif calificacion == "Una vez por semana":
                frecuencia[1] += 1
            elif calificacion == "Dos veces por semana":
                frecuencia[2] += 1
            elif calificacion == "Tres o mas veces por semana":
                frecuencia[3] += 1

        # Crear el gráfico de pastel
        plt.pie(frecuencia, colors=colores, autopct='%1.1f%%', startangle=140, explode=explode)
        print(frecuencia)

        # Agregar leyendas por color
        leyendas_por_color = [f'{etiqueta}: {frecuencia[i]}' for i, etiqueta in enumerate(etiquetas)]
        plt.legend(leyendas_por_color, title="Leyendas", loc="center right")

        # Mostrar el gráfico
        plt.axis('equal')  # Esto garantiza que el gráfico de pastel sea circular
        plt.show()


# Obtiene el número de columnas
# num_columnas = data.shape[1]

# print(f"El archivo Excel tiene {num_columnas} columnas.")

# # Itera a través de las filas del DataFrame
# for indice, fila in data.iterrows():
#     # Accede a cada valor en la fila
#     for valor in fila:
#         print(valor)
#     # Puedes realizar operaciones o procesamiento de datos con los valores de la fila
#     print(f"Fin de la fila {indice}")

# Convierte el DataFrame en una lista de listas para tabulate
# data_list = data.values.tolist()

# Imprime los datos en formato de tabla
# print(tabulate(data_list, headers=data.columns, tablefmt='grid'))

# for calificacionAseo in data["Aseo"]:
#     print(calificacionAseo)

# Extrae la columna 'Nombre_Columna' como una Serie
# columna_serie = data['Aseo']

# Convierte la Serie en una lista
# columna_lista = columna_serie.tolist()

# Ahora 'columna_lista' es una lista de Python
# print(columna_lista)

if __name__ == '__main__':
    app = ServiciosPublicosVillavicencio()
    app.obtenerGraficaCalificacionesDiasUsoSemanal()
