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


"""". Gráfico de barras (RunTime de películas/series de Marvel Vs DC):

Duración variable: Las películas y series tienen duraciones diferentes, 
lo que refleja la diversidad en el tipo de contenido producido.

Películas largas: Las películas más largas podrían corresponder 
a eventos importantes en los universos cinematográficos.

Estrategias de contenido: Algunas películas más cortas podrían enfocarse en tramas ligeras o 
acción rápida, mientras que las largas buscan desarrollar más la historia."""
