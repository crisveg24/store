Carpeta Extract – Extracción y limpieza de datos

La carpeta Extract se encarga de extraer, limpiar y preparar los datos de entrada para el pipeline ETL de nuestro proyecto fifaeda. Esta carpeta incluye scripts para limpiar los archivos CSV originales y clases para la lectura estructurada de los datos.

Estructura de la carpeta
Extract/
│
├── Files/
│   ├── fifa_eda_stats_clean.csv    # Archivo CSV limpio con los datos de los jugadores
│   └── fifa_eda_stats.csv          # Archivo CSV original con los datos de los jugadores
│
├── clean.py                        # Script para limpiar y normalizar los datos del CSV
└── extractor.py                    # Clase Extractor para leer archivos CSV de forma estructurada

Archivo clean.py

Este script se encarga de limpiar y normalizar los datos del archivo CSV original (fifa_eda_stats.csv) para que puedan ser procesados correctamente en las siguientes etapas del ETL.

Funcionalidades principales:

Eliminar duplicados y valores nulos en las columnas clave.

Normalizar los nombres de las columnas.

Convertir valores de texto (como valores monetarios o unidades) a formatos numéricos adecuados.

Guardar el archivo limpio como fifa_eda_stats_clean.csv.

Archivo extractor.py

Este módulo contiene la clase Extractor, diseñada para leer archivos CSV de manera estructurada y devolver los datos en un DataFrame de pandas.

Funcionalidades principales:

Inicialización: La clase recibe la ruta del archivo a procesar (file_path).

Método extract: Este método lee el archivo CSV y devuelve un DataFrame. Si ocurre algún error durante la lectura, captura la excepción y devuelve None.

class Extractor:
    def __init__(self, file_path):
        self.file_path = file_path

    def extract(self):
        try:
            df = pd.read_csv(self.file_path)
            return df
        except Exception as e:
            print(f"Error al extraer datos: {e}")
            return None

Buenas prácticas y recomendaciones

Mantener los archivos originales: Es importante mantener los archivos CSV originales sin modificar para tener un histórico de los datos crudos. En nuestro caso, fifa_eda_stats.csv es el archivo de entrada original.

Utilizar clean.py antes de cargar los datos: Asegúrate de ejecutar clean.py para limpiar y normalizar los datos antes de cargarlos en la base de datos o realizar cualquier otro procesamiento. Esto garantiza que los datos sean consistentes y estén listos para el análisis.

Reutilización y pruebas unitarias: La clase Extractor permite la reutilización del código y facilita las pruebas unitarias, ya que abstrae la lógica de lectura de archivos CSV. Esto hace que el proceso sea más modular y fácil de probar.