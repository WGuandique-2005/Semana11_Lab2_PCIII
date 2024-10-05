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


