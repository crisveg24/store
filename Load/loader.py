from Config.config import Config
from pyspark.sql import SparkSession
import pandas as pd
import os

class Loader:
    """
    Clase para cargar los datos limpios a un destino usando PySpark.
    """
    def __init__(self, df):
        self.df = df

    def to_csv(self, output_path):
        """
        Guarda el DataFrame de Spark en un archivo CSV usando pandas como intermediario.
        """
        try:
            # Convertir a pandas y guardar
            pdf = self.df.toPandas()
            
            # Usar una ruta temporal en el directorio del usuario
            temp_path = os.path.join(os.path.expanduser("~"), "fifa_temp.csv")
            pdf.to_csv(temp_path, index=False)
            
            # Mover el archivo a su ubicación final
            output_dir = os.path.dirname(output_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
                
            if os.path.exists(output_path):
                os.remove(output_path)
            os.rename(temp_path, output_path)
            
            print(f"Datos guardados en {output_path}")
        except Exception as e:
            print(f"Error al guardar datos en CSV: {e}")
            if os.path.exists(temp_path):
                os.remove(temp_path)

    def to_sqlite(self, db_path=None, table_name=None):
        """
        Guarda el DataFrame de Spark en una base de datos SQLite usando pandas como intermediario.
        """
        db_path = db_path or Config.SQLITE_DB_PATH
        table_name = table_name or Config.SQLITE_TABLE
        
        try:
            # Convertir a pandas y guardar
            pdf = self.df.toPandas()
            output_dir = os.path.dirname(db_path)
            if output_dir:
                os.makedirs(output_dir, exist_ok=True)
            
            import sqlite3
            conn = sqlite3.connect(db_path)
            pdf.to_sql(table_name, conn, if_exists='replace', index=False)
            conn.close()
            
            print(f"Datos guardados en la base de datos SQLite: {db_path}, tabla: {table_name}")
        
        except Exception as e:
            print(f"Error al guardar en SQLite: {e}")
