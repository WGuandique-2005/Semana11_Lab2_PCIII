"""
_____________________________________________________________________________
 Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
    C) Un gráfico circular
Enlace al dataset utilizado: 
______________________________________________________________________________
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset de China vs Japon
paises = pd.read_csv('dataset/Big_Japan_vs_China_Technology.csv')


# Contamos la frecuencia de cada tipo, en este caso los paises de china y japon, con los sectores tecnologicos
type_counts = paises['type'].value_counts()


