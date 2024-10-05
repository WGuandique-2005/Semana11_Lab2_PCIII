"""
____________________________________________________________________________
Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
    A). Un gráfico de barras
Enlace al dataset utilizado: 
https://www.kaggle.com/datasets/davinascimento/data-to-learn-data-science
____________________________________________________________________________
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos del DataFrame
df = pd.read_csv('dataset/data.csv')

# Creamos el gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(df['Duration'], df['Calories'], color=['Pink'], width=3)

# Añadimos las etiquetas y el título
plt.xlabel('Duracion en minutos', fontsize=12)
plt.ylabel('Calorias quemadas', fontsize=12)
plt.title('Calorías quemadas según la duración de la actividad', fontsize=16)

# Mostramos el gráfico de barras
plt.grid(True)
plt.show()

"""
_______________________________________________________________________
Genera un gráfico de barras que representa la relación entre la
duración de la actividad física y las calorías quemadas. Utilizando 
un dataset que contiene información sobre diferentes actividades, 
cada barra del gráfico indica cuántas calorías se queman en función 
de la duración de la actividad, expresada en minutos. 
_______________________________________________________________________
"""