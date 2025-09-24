"""
ETL Pipeline para datos de FIFA usando PySpark

Este script implementa un pipeline ETL (Extract, Transform, Load) para procesar datos
de jugadores de FIFA utilizando PySpark. El pipeline realiza las siguientes operaciones:
1. Extracción de datos desde un archivo CSV
2. Transformación y limpieza de datos usando PySpark DataFrame
3. Carga de datos en formato CSV y base de datos SQLite
4. Generación de visualizaciones y análisis estadísticos

Requisitos:
- PySpark
- findspark
- Python 3.6+
- Java 8+

Autor: Cristian Vega
Fecha: Septiembre 2025
"""

import logging
import os
import findspark
findspark.init()  # Inicializar PySpark

from pyspark.sql import SparkSession
from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
from Transform.graficas_new import generar_graficas

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def create_spark_session():
    """
    Crear y configurar la sesión de Spark con configuraciones optimizadas.
    
    Configuraciones:
    - Memoria: 2GB para driver y executor
    - Arrow: Habilitado para mejor rendimiento con pandas
    - Timezone: UTC para consistencia temporal
    - Logging: Reducido para minimizar salida innecesaria
    
    Returns:
        SparkSession: Sesión de Spark configurada
    """
    return SparkSession.builder \
        .appName("FIFA Data ETL") \
        .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
        .config("spark.driver.memory", "2g") \
        .config("spark.executor.memory", "2g") \
        .config("spark.sql.execution.arrow.pyspark.enabled", "true") \
        .config("spark.driver.extraJavaOptions", "-Duser.timezone=UTC") \
        .config("spark.executor.extraJavaOptions", "-Duser.timezone=UTC") \
        .config("spark.sql.session.timeZone", "UTC") \
        .config("spark.ui.showConsoleProgress", "false") \
        .config("spark.sql.debug.maxToStringFields", "100") \
        .config("spark.logging.level", "ERROR") \
        .getOrCreate()

def main():
    """
    Función principal que ejecuta el pipeline ETL completo.
    
    El proceso incluye:
    1. Inicialización de Spark y configuración del entorno
    2. Extracción de datos desde archivo CSV
    3. Transformación y limpieza de datos
    4. Carga de datos procesados en CSV y SQLite
    5. Generación de visualizaciones analíticas
    
    La función maneja excepciones y asegura la limpieza de recursos
    incluso en caso de error.
    """
    logging.info("Iniciando proceso ETL con PySpark")
    spark = None

    try:
        # Inicializar Spark
        spark = create_spark_session()
        
        # Configurar rutas
        input_path = Config.INPUT_PATH
        output_path = "Extract/Files/fifa_eda_stats_final.csv"
        
        # Crear carpeta de salida si no existe
        db_folder = os.path.dirname(Config.SQLITE_DB_PATH)
        os.makedirs(db_folder, exist_ok=True)
        logging.info(f"Carpeta de salida verificada/creada: {db_folder}")

        # EXTRAER
        logging.info("Extrayendo datos...")
        extractor = Extractor(input_path, spark)
        df_raw = extractor.extract()
        if df_raw is None:
            logging.error("No se pudieron extraer datos.")
            return
        logging.info(f"Datos extraídos correctamente de {input_path} ({df_raw.count()} registros)")

        # TRANSFORMAR
        logging.info("Transformando datos...")
        transformer = Transformer(df_raw)
        df_clean = transformer.transform()
        logging.info(f"Datos transformados: {df_clean.count()} registros")

        # CARGAR
        logging.info("Cargando datos...")
        loader = Loader(df_clean)
        loader.to_csv(output_path)
        loader.to_sqlite()
        logging.info(f"Datos guardados en {output_path} y en SQLite: {Config.SQLITE_DB_PATH}")

        # GENERAR GRÁFICAS
        logging.info("Generando gráficas...")
        generar_graficas(df_clean)
        logging.info("Gráficas generadas correctamente.")

    except Exception as e:
        logging.error(f"Error en el proceso ETL: {e}")
        import traceback
        logging.error(f"Traceback completo: {traceback.format_exc()}")
        raise e

    finally:
        if spark:
            spark.stop()
            logging.info("Sesión de Spark cerrada")

if __name__ == "__main__":
    main()