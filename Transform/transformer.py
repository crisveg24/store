from pyspark.sql.functions import col, when, regexp_replace, lit
from pyspark.sql.types import DoubleType

class Transformer:
    """
    Clase para transformar y limpiar los datos extraídos usando PySpark.
    """
    def __init__(self, df):
        self.df = df

    def transform(self):
        """
        Realiza limpieza y transformación de los datos usando PySpark.
        """
        # Verificar si las columnas esenciales existen
        required_columns = ['id', 'name', 'age', 'nationality', 'overall', 'potential', 'value', 'wage', 'height', 'weight']
        for col_name in required_columns:
            if col_name not in self.df.columns:
                raise ValueError(f"La columna '{col_name}' no existe en el DataFrame")

        # Convertir columnas monetarias
        df = self.df
        df = self.convert_monetary_column(df, 'value')
        df = self.convert_monetary_column(df, 'wage')
        df = self.convert_monetary_column(df, 'release_clause')

        # Convertir columnas numéricas y rellenar nulos con 0
        num_cols = ['age', 'overall', 'potential', 'height', 'weight']
        for column in num_cols:
            df = df.withColumn(column, 
                             when(col(column).isNull(), lit(0))
                             .otherwise(col(column).cast(DoubleType())))

        # Eliminar duplicados por nombre
        df = df.dropDuplicates(['name'])

        self.df = df
        return self.df

    def convert_monetary_column(self, df, column_name):
        """
        Convierte valores monetarios (€100M, €1K) a valores numéricos usando PySpark.
        """
        if column_name not in df.columns:
            return df

        # Eliminar el símbolo €, la M y la K, y las comas
        df = df.withColumn(column_name, regexp_replace(col(column_name), '[€,]', ''))
        
        # Convertir valores con M (millones)
        df = df.withColumn(column_name,
            when(col(column_name).contains('M'),
                regexp_replace(col(column_name), 'M', '').cast(DoubleType()) * 1000000)
            .when(col(column_name).contains('K'),
                regexp_replace(col(column_name), 'K', '').cast(DoubleType()) * 1000)
            .otherwise(col(column_name).cast(DoubleType())))

        return df
