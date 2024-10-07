import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos del Balón de Oro 2024
ballon_dor_df = pd.read_csv('2024 Ballon Dor Nominees League Stats2.csv')

# Filtrar las columnas necesarias (usamos los primeros 10 jugadores por simplicidad)
playing_time = ballon_dor_df[['player', 'Playing Time-MP']].dropna().head(10)

# Crear gráfico circular
plt.figure(figsize=(8, 8))
plt.pie(playing_time['Playing Time-MP'], labels=playing_time['player'], autopct='%1.1f%%', startangle=140)
plt.title('Top 10 Ballon d\'Or Nominees by Playing Time')
plt.tight_layout()
plt.show()
