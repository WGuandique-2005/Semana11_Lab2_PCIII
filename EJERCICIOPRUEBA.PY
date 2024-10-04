"""
___________________________________________________________________________
Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
___________________________________________________________________________
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar los datos en un DataFrame
data = {
    "Duracion": [60, 60, 60, 45, 45, 60, 60, 45, 30, 60],
    "Calorias": [409.1, 479.0, 340.0, 282.4, 406.0, 300.0, 374.0, 253.3, 195.1, 269.0]  
}

df = pd.DataFrame(data)

plt.figure(figsize=(10,6))
plt.plot(df['Duracion'], df['Calorias'], color='b', marker='o', linestyle='-', label='Calories Burned')

plt.xlabel('Duracion en minutos', fontsize=12)
plt.ylabel('Calorias quemadas', fontsize=12)
plt.title('Calorías quemadas según la duración de la actividad', fontsize=16)
plt.legend()
plt.grid(True)

# Mostrar el gráfico
plt.show()
