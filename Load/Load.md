Carpeta Load – Carga de Datos

La carpeta Load es responsable de la carga de los datos limpios en el destino adecuado, ya sea un archivo CSV o una base de datos SQLite. Utilizando la clase Loader, se facilita la transferencia de datos desde el formato intermedio (DataFrame) a un almacenamiento persistente.

Archivo loader.py

Este script contiene la clase Loader, que se encarga de cargar los datos transformados en los pasos anteriores del pipeline ETL. La clase tiene métodos para guardar los datos en un archivo CSV o en una base de datos SQLite.

Métodos principales:
__init__(self, df)

Descripción: Inicializa la clase Loader con un DataFrame (df) que contiene los datos limpios.

Parámetros:

df (DataFrame): El DataFrame que contiene los datos a cargar.

to_csv(self, output_path)

Descripción: Guarda el DataFrame limpio en un archivo CSV.

Parámetros:

output_path (str): Ruta donde se guardará el archivo CSV.

Excepciones: Si ocurre un error al guardar los datos en el archivo, se captura la excepción y se imprime un mensaje de error.

to_sqlite(self, db_path=None, table_name=None)

Descripción: Guarda el DataFrame limpio en una base de datos SQLite.

Parámetros:

db_path (str, opcional): Ruta de la base de datos SQLite. Si no se especifica, se utiliza el valor por defecto de la configuración (Config.SQLITE_DB_PATH).

table_name (str, opcional): Nombre de la tabla en la que se almacenarán los datos. Si no se especifica, se utiliza el valor por defecto de la configuración (Config.SQLITE_TABLE).

Excepciones: Si ocurre un error al guardar los datos en la base de datos, se captura la excepción y se imprime un mensaje de error.

Propósito

El objetivo de la clase Loader es guardar los datos limpios en un formato persistente, ya sea como archivo CSV o en una base de datos SQLite. Esto permite que los datos procesados estén disponibles para su análisis posterior o para su integración en otros sistemas.

Conclusión

La clase Loader es un componente clave en el pipeline ETL, ya que se encarga de la carga de los datos a los destinos finales. Proporciona métodos fáciles de usar para guardar los datos en formatos accesibles y persistentes, lo que permite una fácil integración con otros sistemas o procesos de análisis.