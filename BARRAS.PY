import pandas as pd
import matplotlib.pyplot as plt

# Cargamos los datos del DataFrame

df = pd.read_csv('data.csv')

# Creamos el gráfico de barras
plt.figure(figsize=(10,6))
plt.bar(df['Duration'], df['Calories'], color='b')

# Añadimos las etiquetas y el título
plt.xlabel('Duracion en minutos', fontsize=12)
plt.ylabel('Calorias quemadas', fontsize=12)
plt.title('Calorías quemadas según la duración de la actividad', fontsize=16)

# Mostramos el gráfico
plt.grid(True)
plt.show()
