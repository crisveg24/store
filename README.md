Proyecto ETL - Gestión de Tiendas

Este proyecto es un pipeline ETL (Extract, Transform, Load) para procesar y limpiar los datos de la base de datos de tiendas. Utiliza Python, Pandas para el procesamiento de datos y SQLite como base de datos de destino. Este proyecto sigue el enfoque de separación de responsabilidades utilizando un patrón arquitectónico por capas.

Descripción General

El objetivo del proyecto ETL es tomar los datos crudos de un archivo CSV (Stores.csv), limpiarlos, transformarlos y cargarlos en una base de datos SQLite. El pipeline está compuesto por tres pasos principales: Extracción, Transformación y Carga.

Extracción: Los datos se extraen de un archivo CSV.

Transformación: Los datos extraídos se limpian y normalizan, eliminando duplicados y valores nulos.

Carga: Los datos transformados se almacenan en una base de datos SQLite.

Características principales

Extracción de datos desde un archivo CSV.

Limpieza y transformación de datos utilizando Pandas.

Carga de los datos transformados en una base de datos SQLite.

Código modular, organizado en carpetas para cada paso del pipeline ETL.

Estructura del Proyecto
ETL/
├── Extract/
│   ├── Files/
│   │   ├── Stores.csv         # Archivo de entrada con los datos crudos
│   │   └── Stores_clean.csv   # Archivo de salida con los datos limpios
│   ├── clean.py               # Script para limpiar los datos del CSV
│   └── extractor.py           # Clase para extraer datos del CSV
├── Transform/
│   └── transformer.py         # Clase para transformar los datos extraídos
├── Load/
│   ├── loader.py              # Clase para cargar los datos en SQLite
│   └── etl_config.py          # Configuraciones para el pipeline ETL
└── requirements.txt           # Dependencias necesarias para ejecutar el proyecto

Dependencias

Este proyecto requiere las siguientes librerías para funcionar correctamente:

pandas: Para el procesamiento de datos.

sqlite3: Para interactuar con la base de datos SQLite.

Para instalar las dependencias, ejecuta el siguiente comando:

pip install -r requirements.txt

Contribuciones

Si deseas contribuir al proyecto, por favor sigue las buenas prácticas de documentación y arquitectura ya establecidas. ¡Cualquier mejora o sugerencia será bienvenida!

Licencia

Este proyecto es de uso libre para fines educativos y de aprendizaje.