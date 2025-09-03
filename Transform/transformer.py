import pandas as pd

class Transformer:
    """
    Clase para transformar y limpiar los datos extraídos de Stores_clean.csv.
    """
    def __init__(self, df):
        self.df = df

    def transform(self):
        """
        Realiza limpieza y transformación de los datos.
        """
        df = self.df.copy()

        # Verificar si las columnas existen
        required_columns = ['store_id', 'store_area', 'items_available', 'daily_customer_count', 'store_sales']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"La columna '{col}' no existe en el DataFrame")

        # Convertir las columnas a tipo numérico
        num_cols = ['store_area', 'items_available', 'daily_customer_count', 'store_sales']
        for col in num_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convierte a numérico, convirtiendo errores a NaN

        # Rellenar valores nulos en columnas numéricas con 0
        df[num_cols] = df[num_cols].fillna(0)

        # Si la columna 'store_id' tiene valores duplicados, los eliminamos
        df = df.drop_duplicates(subset=['store_id'])


        # Asignar el DataFrame transformado a self.df
        self.df = df
        return self.df
