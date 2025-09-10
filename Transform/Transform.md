Carpeta Transform – Transformación y limpieza de datos

La carpeta Transform está encargada de la transformación y limpieza de los datos extraídos en la etapa anterior del pipeline ETL. Esta carpeta incluye la clase Transformer, que procesa y valida los datos antes de ser cargados a la base de datos o utilizados en otros procesos.

Archivo transformer.py

Este script contiene la clase Transformer, que se encarga de limpiar y transformar los datos extraídos desde Stores_clean.csv en un formato adecuado para el siguiente paso del pipeline ETL.
Funcionalidades principales:

Inicialización: La clase Transformer toma como entrada un DataFrame (df), que es el que contiene los datos extraídos.

Método transform: Este método realiza una serie de transformaciones sobre los datos:

Verifica que las columnas necesarias (store_id, store_area, items_available, daily_customer_count, store_sales) existan en el DataFrame.

Convierte las columnas numéricas a un tipo numérico (usando pd.to_numeric), manejando cualquier error de conversión.

Rellena los valores nulos en las columnas numéricas con 0.

Elimina las filas duplicadas basadas en la columna store_id.

Devuelve el DataFrame transformado.

Propósito:

El objetivo de este script es preparar y limpiar los datos para que estén listos para ser cargados en la base de datos o utilizados en análisis adicionales. Asegura que los datos sean consistentes, sin valores nulos o duplicados, y con los formatos adecuados para el procesamiento posterior.

Conclusión

La carpeta Transform juega un papel clave en el pipeline ETL al preparar los datos para su posterior procesamiento y almacenamiento. La clase Transformer permite realizar todas las transformaciones necesarias, garantizando la calidad de los datos antes de ser utilizados en otras partes del sistema. Este enfoque modular facilita la escalabilidad y el mantenimiento del proyecto ETL a largo plazo.