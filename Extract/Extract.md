Carpeta Extract – Extracción y limpieza de datos

La carpeta Extract se encarga de extraer y preparar los datos de entrada para el pipeline ETL. Aquí se incluyen scripts para limpiar los archivos CSV originales y clases para la lectura estructurada de los datos.

Estructura de la carpeta
Extract/
│
├── Files/
│   ├── Stores.csv          # Archivo CSV original con los datos de las tiendas
│   └── Stores_clean.csv    # Archivo CSV resultante después de la limpieza
│
├── clean.py                # Script para limpiar y normalizar los datos del CSV
└── extractor.py            # Clase Extractor para leer archivos CSV de forma estructurada

Archivo clean.py

Este script se encarga de preparar y limpiar los datos originales del archivo CSV (Stores.csv) para que puedan ser procesados correctamente en las siguientes etapas del ETL.

Archivo extractor.py

Este módulo contiene la clase Extractor, diseñada para leer de manera estructurada archivos CSV y devolver los datos en un DataFrame de pandas.
Funcionalidades principales:

Inicialización: recibe la ruta del archivo a procesar (file_path).

Método extract: lee el CSV y devuelve un DataFrame. Si ocurre algún error durante la lectura, captura la excepción y devuelve None.

Buenas prácticas y recomendaciones

Mantener los archivos originales sin modificar para tener un histórico de los datos crudos.

Utilizar clean.py antes de cargar los datos a la base de datos para asegurar la calidad y consistencia de los datos.

La clase Extractor permite reutilización y pruebas unitarias, ya que abstrae la lógica de lectura de archivos CSV.