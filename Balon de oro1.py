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

""""Gráfico circular (Tiempo de juego de los nominados al Balón de Oro 2024):

Desigualdad en tiempo de juego: El gráfico muestra que algunos jugadores tienen un tiempo de 
juego considerablemente mayor que otros, lo que refleja su importancia en el equipo.

Top 10 jugadores: Los jugadores con más minutos en el campo probablemente juegan un rol crucial, lo 
que podría estar relacionado con su nominación al Balón de Oro.

Distribución clara: Los porcentajes muestran una distribución clara, destacando a ciertos 
jugadores que han acumulado más tiempo en los partidos.
"""