"""
__________________________________________________________________________
Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
    C) Un gráfico circular
Enlace al dataset utilizado: 
__________________________________________________________________________
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset de NetFlix.csv
datos = pd.read_csv('dataset/Leetcode_Questions.csv')

# Contar la frecuencia de cada tipo (movie o TV show)
Difficulty_counts = datos['Difficulty'].value_counts()

# Crear el gráfico de pastel
plt.figure(figsize=(10,8))
plt.pie(Difficulty_counts, labels = Difficulty_counts.index, autopct='%1.1f%%', 
        colors=['pink', 'green', 'yellow'],
        startangle=90,  # Iniciar el gráfico desde arriba
        explode=[0.05, 0.05, 0.05],  # Separar un poco cada sección del centro
        pctdistance=0.85,  # Distancia entre el porcentaje y el centro
        labeldistance=1.1,  # Distancia entre la etiqueta y el centro
        textprops={'size': 'large'})  # Tamaño de la fuente

plt.title('Dificultad de preguntas de Leetcode', fontsize=18)
plt.axis('equal')  # Garantizar que el gráfico sea circular
plt.show()
