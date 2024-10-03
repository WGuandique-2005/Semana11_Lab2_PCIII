"""
* Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
! b. Un gráfico de líneas
Enlace al dataset utilizado: https://www.kaggle.com/datasets/jaidalmotra/pokemon-dataset
"""

# Importar las librerías necesarias
import pandas as pd  # para manejar datos en forma de tablas
import matplotlib.pyplot as plt  # para crear gráficos

# Cargar el dataset de Pokémon desde un archivo CSV llamado "Pokemon.csv"
ds = pd.read_csv('Pokemon.csv')

# Agrupar los datos por la columna "type1" (tipo de Pokémon) y calcular la media de la columna "hp" (puntos de vida)
hp_by_type = ds.groupby('type1')['hp'].mean().reset_index()
# Ordenar los resultados en orden descendente según la media de HP
hp_by_type = hp_by_type.sort_values('hp', ascending=False)

# Crear una figura para el gráfico con un tamaño de 10x6 pulgadas
plt.figure(figsize=(10, 6))
# Crear un gráfico de líneas que muestra la media de HP por tipo de Pokémon
plt.plot(hp_by_type['type1'], hp_by_type['hp'], 
        marker='o',  # agregar marcadores circulares en cada punto
        color='blue',  # color del gráfico
        linewidth=2)  # grosor de la línea

plt.title('Media de HP por tipo de Pokémon (ordenados por HP descendente)', fontsize=18)
plt.xlabel('Tipo de Pokémon')
# Agregar etiquetas para cada punto en el eje x, rotadas 45 grados para que sean más legibles
plt.xticks(range(len(hp_by_type)), hp_by_type['type1'], rotation=45)
# Agregar un grid al gráfico para facilitar la lectura
plt.grid(True)
plt.ylabel('Media de HP')

# Mostrar el gráfico
plt.show()