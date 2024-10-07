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
