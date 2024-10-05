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

# Filtramos el dataset para China y Japón por separado
china_data = paises[paises['Country'] == 'China']
japan_data = paises[paises['Country'] == 'Japan']

# Agrupamos los datos por el sector tecnológico y contamos las ocurrencias para cada país
china_tech_by_sector = china_data.groupby('Tech Sector')['Tech Sector'].count().reset_index(name='Count')
japan_tech_by_sector = japan_data.groupby('Tech Sector')['Tech Sector'].count().reset_index(name='Count')

# Ordenamos los sectores por frecuencia para tener consistencia
china_tech_by_sector = china_tech_by_sector.sort_values('Tech Sector')
japan_tech_by_sector = japan_tech_by_sector.sort_values('Tech Sector')

# Creamos una figura para el gráfico de líneas 
plt.figure(figsize=(12, 6))

# Línea para China
plt.plot(china_tech_by_sector['Tech Sector'], china_tech_by_sector['Count'], 
         marker='o', color='pink', linewidth=2, label='China')

# Línea para Japón
plt.plot(japan_tech_by_sector['Tech Sector'], japan_tech_by_sector['Count'], 
         marker='o', color='green', linewidth=2, label='Japón')

# Añadimos el título y las etiquetas a los ejes
plt.title('Frecuencia de Sectores Tecnológicos: China vs Japón', fontsize=18)
plt.xlabel('Sector Tecnológico', fontsize=14)
plt.ylabel('Frecuencia', fontsize=14)
plt.xticks(rotation=45)

# Añadimos una cuadrícula y la leyenda
plt.grid(color='gray')
plt.legend()

# Ajustamos el diseño y mostramos el gráfico
plt.tight_layout()
plt.show()
