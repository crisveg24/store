import seaborn as sns
import matplotlib.pyplot as plt

# Función para asignar continentes basados en nacionalidad
def asignar_continente(nacionalidad):
    continentes = {
        'Asia': ['Japan', 'China', 'South Korea', 'Iran', 'Saudi Arabia'],
        'Europe': ['Spain', 'Germany', 'France', 'Italy', 'England', 'Portugal', 'Netherlands'],
        'Africa': ['Nigeria', 'Egypt', 'South Africa', 'Ghana', 'Cameroon'],
        'North America': ['United States', 'Mexico', 'Canada'],
        'South America': ['Argentina', 'Brazil', 'Colombia', 'Chile', 'Uruguay'],
        'Oceania': ['Australia', 'New Zealand']
    }
    
    for continente, paises in continentes.items():
        if nacionalidad in paises:
            return continente
    return 'Other'  # Si no pertenece a ninguno de los grupos anteriores

def generar_graficas(df):
    """
    Función para generar 3 gráficas con Seaborn y guardarlas como imágenes.
    """
    # Agregar la columna 'continent' para poder hacer el gráfico de barras por continente
    df['continent'] = df['nationality'].apply(asignar_continente)
    
    # Gráfico 1: Relación entre 'value' y 'overall' (valor del jugador vs habilidad)
    plt.figure(figsize=(12, 8))
    sns.scatterplot(data=df, x='value', y='overall', hue='nationality', palette='tab20', legend='full')
    plt.title('Relación entre Valor del Jugador y Overall')
    plt.xlabel('Valor del Jugador')
    plt.ylabel('Overall')
    
    # Mejorar la visibilidad de la leyenda
    plt.legend(title='Nacionalidad', bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=10)
    
    # Agregar explicaciones en la gráfica de dispersión
    plt.text(50000000, 85, "Eje X: Valor del jugador\nEje Y: Habilidad general (Overall)", fontsize=12)
    
    # Guardar la gráfica como archivo PNG
    plt.savefig("/workspaces/store/Extract/Files/valor_vs_overall.png")
    plt.close()  # Cerrar la gráfica para evitar sobrecargar la memoria

    # Gráfico 2: Valor promedio de los jugadores por continente
    plt.figure(figsize=(14, 8))
    sns.barplot(data=df, x='continent', y='value', estimator='mean', errorbar=None)
    plt.title('Valor Promedio de Jugadores por Continente')
    plt.xlabel('Continente')
    plt.ylabel('Valor Promedio')
    plt.xticks(rotation=45)
    
    # Agregar explicaciones en la gráfica de barras
    plt.text(1, 150000000, "Eje X: Continente\nEje Y: Valor Promedio de Jugadores", fontsize=12)
    
    # Guardar la gráfica como archivo PNG
    plt.savefig("/workspaces/store/Extract/Files/valor_promedio_por_continente.png")
    plt.close()  # Cerrar la gráfica para evitar sobrecargar la memoria

    # Gráfico 3: Distribución del 'value' por continente (usamos un boxplot)
    plt.figure(figsize=(14, 8))
    sns.boxplot(data=df, x='continent', y='value')
    plt.title('Distribución del Valor de los Jugadores por Continente')
    plt.xlabel('Continente')
    plt.ylabel('Valor del Jugador')
    plt.xticks(rotation=45)
    
    # Agregar explicaciones en el boxplot
    plt.text(1, 150000000, "Eje X: Continente\nEje Y: Valor de los Jugadores", fontsize=12)

    # Guardar la gráfica como archivo PNG
    plt.savefig("/workspaces/store/Extract/Files/distribucion_valor_por_continente.png")
    plt.close()  # Cerrar la gráfica para evitar sobrecargar la memoria
