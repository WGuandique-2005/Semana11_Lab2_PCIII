"""
* Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
! a. Un gráfico de barras
Enlace al dataset utilizado: https://www.kaggle.com/datasets/ambaliyagati/spotify-dataset-for-playing-around-with-sql
"""

import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv('spotify_tracks.csv')
genre_counts = ds['genre'].value_counts().head(15)  # seleccionar solo los 15 géneros más frecuentes

plt.figure(figsize=(10, 6))
genre_counts.plot(kind='bar')
plt.title('15 Géneros más escuchados en Spotify')
plt.xlabel('Género')
plt.ylabel('Frecuencia')
plt.show()