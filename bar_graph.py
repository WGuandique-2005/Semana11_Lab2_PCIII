"""
* Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
! a. Un gráfico de barras
Enlace al dataset utilizado: https://www.kaggle.com/datasets/ambaliyagati/spotify-dataset-for-playing-around-with-sql
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
ds = pd.read_csv('spotify_tracks.csv')

# Calcular la duración promedio por género en ms
duracion_generos = ds.groupby('genre')['duration_ms'].mean().reset_index()

# Seleccionar los 12 géneros con mayor duración promedio
top_duracion_generos = duracion_generos.nlargest(12, 'duration_ms')

plt.figure(figsize=(10, 6))
plt.bar(top_duracion_generos['genre'], top_duracion_generos['duration_ms'], color='#2ecc71')  # Color de las barras
plt.xlabel('Género', fontsize=12)  # Tamaño de la etiqueta del eje x
plt.ylabel('Duración promedio (ms)', fontsize=12)  # Tamaño de la etiqueta del eje y
plt.title('Los 12 géneros con mayor duración promedio en Spotify', fontsize=14, fontweight='bold')  # Tamaño y estilo del título
plt.xticks(rotation=90)  # Rotar las etiquetas del eje x para que sean más legibles
plt.tight_layout()  # Ajustar el tamaño del gráfico para que quepa todo
plt.show()

"""
* Analisis:
Los géneros con mayor duración promedio son "Progressive Trance", "Drum and Bass" y "Dubstep", 
con duraciones promedio de alrededor de 240-260 segundos (4-4,3 minutos).

Estos géneros suelen caracterizarse por ritmos complejos y estructuras musicales más largas, 
lo que puede explicar su mayor duración promedio.
"""