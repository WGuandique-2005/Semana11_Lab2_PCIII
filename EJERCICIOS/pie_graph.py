"""
* Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
! c. Un gráfico circular
Enlace al dataset utilizado: https://www.kaggle.com/datasets/imtkaggleteam/netflix
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset de NetFlix.csv
netflix_data = pd.read_csv('dataset/NetFlix.csv')

# Contar la frecuencia de cada tipo (movie o TV show)
type_counts = netflix_data['type'].value_counts()

# Crear el gráfico de pastel
plt.figure(figsize=(10,8))
plt.pie(type_counts, labels = type_counts.index, autopct='%1.1f%%', 
        colors=['#3498db', '#e74c3c'],
        startangle=90,  # Iniciar el gráfico desde arriba
        explode=[0.05, 0.05],  # Separar un poco cada sección del centro
        pctdistance=0.85,  # Distancia entre el porcentaje y el centro
        labeldistance=1.1,  # Distancia entre la etiqueta y el centro
        textprops={'size': 'large'})  # Tamaño de la fuente

plt.title('Distribución de películas y programas de TV en Netflix', fontsize=18)
plt.axis('equal')  # Garantizar que el gráfico sea circular
plt.show()

"""
* Analisis:
El gráfico circular nos muestra que Netflix tiene una oferta más amplia de 
películas que de programas de TV.
"""