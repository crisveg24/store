import os
from pyspark.sql import SparkSession

class Extractor:
    """
    Clase para extraer datos de archivos fuente usando PySpark.
    """
    def __init__(self, file_path, spark_session=None):
        self.file_path = file_path
        self.spark = spark_session or SparkSession.builder \
            .appName("FIFA Data ETL") \
            .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
            .getOrCreate()

    def extract(self):
        """
        Extrae los datos del archivo especificado usando PySpark.
        """
        if not os.path.exists(self.file_path):
            print(f"Error: El archivo {self.file_path} no existe.")
            return None
        try:
            # Leer el archivo CSV con PySpark
            df = self.spark.read \
                .option("header", "true") \
                .option("inferSchema", "true") \
                .csv(self.file_path)
            print(f"Datos extraídos correctamente desde {self.file_path}")
            return df
        except Exception as e:
            print(f"Error al extraer datos: {e}")
            return None
            
    def __del__(self):
        """
        Asegurarse de cerrar la sesión de Spark al destruir la instancia.
        """
        if hasattr(self, 'spark'):
            self.spark.stop()
