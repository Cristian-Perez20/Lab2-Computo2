import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos de películas
movies_df = pd.read_csv('movie6.csv')

# Filtrar las columnas necesarias (usamos las primeras 10 películas por simplicidad)
movie_ratings = movies_df[['title', 'vote_average']].dropna().head(10)

# Crear gráfico de líneas
plt.figure(figsize=(10, 6))
plt.plot(movie_ratings['title'], movie_ratings['vote_average'], marker='o', color='green')
plt.title('Movie Ratings (Top 10 Movies)')
plt.xlabel('Movie Title')
plt.ylabel('Average Rating')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()


""""Gráfico de líneas (Valoración promedio de películas del dataset de "movie"):

Calificaciones diversas: Las valoraciones promedio de las películas varían considerablemente, indicando
 una diferencia en la calidad percibida por los espectadores.

Películas con alta valoración: Las películas con una mayor puntuación pueden estar asociadas a 
un éxito crítico o comercial, reflejando la satisfacción del público.

Tendencia en puntuaciones: Al comparar las películas con mayor y menor valoración, se puede observar qué 
características o géneros podrían tener más éxito en cuanto a la respuesta de la audiencia.
"""