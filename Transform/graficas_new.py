import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from pyspark.sql.functions import col, when, lit

# Diccionario de continentes
CONTINENTES = {
    'Asia': ['Japan', 'China', 'South Korea', 'Iran', 'Saudi Arabia'],
    'Europe': ['Spain', 'Germany', 'France', 'Italy', 'England', 'Portugal', 'Netherlands'],
    'Africa': ['Nigeria', 'Egypt', 'South Africa', 'Ghana', 'Cameroon'],
    'North America': ['United States', 'Mexico', 'Canada'],
    'South America': ['Argentina', 'Brazil', 'Colombia', 'Chile', 'Uruguay'],
    'Oceania': ['Australia', 'New Zealand']
}

def generar_graficas(spark_df):
    """
    Función para generar 3 gráficas con Seaborn usando datos de PySpark.
    """
    # Agregar la columna 'continent' basada en nacionalidad
    # Primero creamos la columna continent con valor 'Other' por defecto
    df_with_continent = spark_df.withColumn('continent', lit('Other'))
    
    # Luego actualizamos para cada continente
    for continente, paises in CONTINENTES.items():
        df_with_continent = df_with_continent.withColumn(
            'continent',
            when(col('nationality').isin(paises), lit(continente))
            .otherwise(col('continent'))
        )

    # Convertir a pandas para visualización
    df = df_with_continent.toPandas()
    
    # Gráfico 1: Relación entre 'value' y 'overall'
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df, x='value', y='overall', hue='nationality', palette='tab20', legend='full')
    plt.title('Relación entre Valor del Jugador y Overall')
    plt.xlabel('Valor del Jugador')
    plt.ylabel('Overall')
    
    plt.legend(title='Nacionalidad', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    plt.text(df['value'].max() * 0.5, 85, 
            "Eje X: Valor del jugador\nEje Y: Habilidad general (Overall)", 
            fontsize=12)
    
    plt.savefig("Extract/Files/valor_vs_overall.png", bbox_inches='tight')
    plt.close()

    # Gráfico 2: Valor promedio por continente
    plt.figure(figsize=(14, 8))
    sns.barplot(data=df, x='continent', y='value', estimator='mean', errorbar=None)
    plt.title('Valor Promedio de Jugadores por Continente')
    plt.xlabel('Continente')
    plt.ylabel('Valor Promedio')
    plt.xticks(rotation=45)
    
    plt.text(1, df['value'].max() * 0.8, 
            "Eje X: Continente\nEje Y: Valor Promedio de Jugadores", 
            fontsize=12)
    
    plt.savefig("Extract/Files/valor_promedio_por_continente.png", bbox_inches='tight')
    plt.close()

    # Gráfico 3: Distribución del valor por continente
    plt.figure(figsize=(14, 8))
    sns.boxplot(data=df, x='continent', y='value')
    plt.title('Distribución del Valor de los Jugadores por Continente')
    plt.xlabel('Continente')
    plt.ylabel('Valor del Jugador')
    plt.xticks(rotation=45)
    
    plt.text(1, df['value'].max() * 0.8, 
            "Eje X: Continente\nEje Y: Valor de los Jugadores", 
            fontsize=12)

    plt.savefig("Extract/Files/distribucion_valor_por_continente.png", bbox_inches='tight')
    plt.close()