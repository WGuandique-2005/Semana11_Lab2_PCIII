"""
_____________________________________________________________________________
 Haciendo uso de la página de Kaggle, seleccionar tres diferentes datasets.
    B) Un gráfico de lineas
Enlace al dataset utilizado: 
______________________________________________________________________________
"""
import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset de China VS Japón desde un archivo CSV
paises = pd.read_csv('dataset/Big_Japan_vs_China_Technology.csv')

# Agrupamos los datos por el sector tecnológico y contar la frecuencia de cada sector
tech_by_sector = paises.groupby('Tech Sector')['Tech Sector'].count().reset_index(name='Count')

# Ordenamos los sectores tecnológicos por la frecuencia de mayor a menor
tech_by_sector = tech_by_sector.sort_values('Count', ascending=False)

# Creamos una figura para el gráfico de líneas 
plt.figure(figsize=(10, 6))

# Creamos un gráfico de líneas que muestra la frecuencia de los sectores tecnológicos
plt.plot(tech_by_sector['Tech Sector'], tech_by_sector['Count'], 
        marker='o',  # agregar marcadores circulares en cada punto
        color='Pink',  # color del gráfico
        linewidth=2)  # grosor de la línea

# Añadimos el título y las etiquetas a los ejes
plt.title('Frecuencia de Sectores Tecnológicos de China VS Japón', fontsize=18)
plt.xlabel('Sector Tecnológico', fontsize=14)
plt.ylabel('Frecuencia', fontsize=14)

# Añadimos las etiquetas del eje x con una rotación de 45 grados
plt.xticks(rotation=45)

# Añadimos una cuadrícula con estilo
plt.grid(color='black')

# Mostramos el gráfico
plt.show()
