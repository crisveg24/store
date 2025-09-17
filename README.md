Proyecto ETL - Gestión de Jugadores de Fútbol

Este proyecto es un pipeline ETL (Extract, Transform, Load) diseñado para procesar, limpiar y almacenar los datos de jugadores de fútbol. Utiliza Python y Pandas para el procesamiento de datos, y SQLite como base de datos de destino. El proyecto sigue un enfoque modular, organizando las responsabilidades en diferentes capas, facilitando así su escalabilidad y mantenimiento.

Descripción General

El objetivo del proyecto ETL es tomar los datos crudos de un archivo CSV (inicialmente fifa_eda_stats.csv), limpiarlos, transformarlos y cargarlos en una base de datos SQLite. El pipeline está compuesto por tres pasos principales: Extracción, Transformación y Carga.

Extracción: Los datos se extraen de un archivo CSV que contiene información sobre jugadores de fútbol.

Transformación: Los datos extraídos se limpian, se normalizan y se preparan para su almacenamiento, eliminando duplicados, valores nulos y realizando conversiones de tipo de datos.

Carga: Los datos transformados se almacenan en una base de datos SQLite y se generan archivos de salida como gráficas en formato PNG.

Características principales

Extracción de datos desde un archivo CSV (fifa_eda_stats.csv).

Limpieza y transformación de datos utilizando Pandas.

Carga de los datos transformados en una base de datos SQLite.

Generación de gráficas para visualizar patrones y relaciones entre los datos de los jugadores.

Código modular y organizado en carpetas para cada paso del pipeline ETL.

Estructura del Proyecto
ETL/
├── Extract/
│   ├── Files/
│   │   ├── fifa_eda_stats.csv        # Archivo de entrada con los datos crudos de los jugadores
│   │   └── fifa_eda_stats_clean.csv  # Archivo de salida con los datos limpios
│   ├── clean.py                      # Script para limpiar y normalizar los datos del CSV
│   └── extractor.py                  # Clase para extraer datos del CSV
├── Transform/
│   ├── transformer.py                # Clase para transformar los datos extraídos
│   └── graficas.py                   # Generación de gráficas para visualización de datos
├── Load/
│   ├── loader.py                     # Clase para cargar los datos en SQLite
│   └── etl_config.py                 # Configuraciones para el pipeline ETL
└── requirements.txt                  # Dependencias necesarias para ejecutar el proyecto

Dependencias

Este proyecto requiere las siguientes librerías para funcionar correctamente:

pandas: Para el procesamiento y análisis de datos.

sqlite3: Para interactuar con la base de datos SQLite.

seaborn: Para generar gráficas y visualizaciones de los datos.

matplotlib: Para la creación de gráficos con seaborn.

Instalación de dependencias

Para instalar las dependencias necesarias, ejecuta el siguiente comando:

pip install -r requirements.txt

Explicación de los cambios realizados:

Enfoque en jugadores de fútbol: El README ahora refleja que estamos trabajando con datos de jugadores de fútbol en lugar de tiendas.

Estructura del pipeline ETL: Detallamos cómo se organiza el proyecto en pasos modulares (Extracción, Transformación y Carga), haciendo énfasis en las funcionalidades específicas para los datos de los jugadores.

Gráficas: Se mencionó graficas.py en la sección de Transform, ya que genera visualizaciones de los datos después de la transformación.

Dependencias: Añadimos seaborn y matplotlib a las dependencias, ya que son necesarias para generar las gráficas.

Contribuciones

Si deseas contribuir al proyecto, por favor sigue las buenas prácticas de documentación y arquitectura ya establecidas. ¡Cualquier mejora o sugerencia será bienvenida!

Licencia

Este proyecto es de uso libre para fines educativos y de aprendizaje.
