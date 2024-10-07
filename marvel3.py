import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos de Marvel Vs DC NEW
marvel_vs_dc_df = pd.read_csv('Marvel Vs DC NEW4.csv')
colores=['red','blue','black','orange','purple','green']

# Filtrar las columnas necesarias y convertir 'RunTime' a un valor numérico
runtime_data = marvel_vs_dc_df[['Movie', 'RunTime']].dropna()
runtime_data['RunTime'] = runtime_data['RunTime'].replace(' min', '', regex=True)  # Eliminar el texto 'min' si existe
runtime_data['RunTime'] = pd.to_numeric(runtime_data['RunTime'], errors='coerce')  # Convertir a numérico
runtime_data = runtime_data.dropna()  # Eliminar valores no numéricos después de la conversión

# Seleccionar las primeras 10 películas/series para una mejor visualización
runtime_data = runtime_data.head(10)

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(runtime_data['Movie'], runtime_data['RunTime'], color= colores, edgecolor='black')

# Mejorar la visualización
plt.title('RunTime of Top 10 Marvel Vs DC Movies/Shows', fontsize=16)
plt.xlabel('Movies/Shows', fontsize=12)
plt.ylabel('RunTime (minutes)', fontsize=12)
plt.xticks(rotation=45, ha='right', fontsize=10)

# Añadir etiquetas en las barras con los valores
for i, value in enumerate(runtime_data['RunTime']):
    plt.text(i, value + 5, f'{int(value)}', ha='center', fontsize=10)

# Asegurarse de que el gráfico se vea bien
plt.tight_layout()
plt.show()
