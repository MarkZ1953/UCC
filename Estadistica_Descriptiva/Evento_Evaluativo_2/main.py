import pandas as pd

# Especifica la ruta del archivo Excel
archivo_excel = 'tu_archivo.xlsx'

# Lee el archivo Excel en un DataFrame
data = pd.read_excel(archivo_excel)

# Obtiene el número de columnas
num_columnas = data.shape[1]

print(f"El archivo Excel tiene {num_columnas} columnas.")