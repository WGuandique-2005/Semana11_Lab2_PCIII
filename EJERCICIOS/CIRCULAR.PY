"""
__________________________________________________________________________
Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
    C) Un gráfico circular
Enlace al dataset utilizado: 
https://www.kaggle.com/datasets/mohitkumar282/leetcode-questions-dataset
__________________________________________________________________________
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset 
datos = pd.read_csv('dataset/Leetcode_Questions.csv')

# Contamos la frecuencia 
Difficulty_counts = datos['Difficulty'].value_counts()

# Creamos el gráfico de pastel
plt.figure(figsize=(10,8))
plt.pie(Difficulty_counts, labels = Difficulty_counts.index, autopct='%1.1f%%', 
        colors=['pink', 'green', 'yellow'],
        startangle=90,  # Iniciamos el gráfico desde arriba
        explode=[0.05, 0.05, 0.05],  # Separamos un poco cada sección del centro
        pctdistance=0.85,  # Distancia entre el porcentaje y el centro
        labeldistance=1.1,  # Distancia entre la etiqueta y el centro
        textprops={'size': 'large'})  # Tamaño de la fuente

plt.title('Dificultad de preguntas de Leetcode', fontsize=18)
plt.axis('equal')  # Garantizamos que el gráfico sea circular
plt.show()

"""
________________________________________________________________________________
Generamos un gráfico de pastel en el cual se visualizala distribución de las 
preguntas de Leetcode por nivel de dificultad (Fácil, Medio, Difícil). El dataset 
incluye una columna llamada Difficulty,que contiene el nivel de cada pregunta.
_________________________________________________________________________________
"""