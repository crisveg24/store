import pandas as pd

class Transformer:
    """
    Clase para transformar y limpiar los datos extraídos de fifa_eda_stats_clean.csv.
    """
    def __init__(self, df):
        self.df = df

    def transform(self):
        """
        Realiza limpieza y transformación de los datos.
        """
        df = self.df.copy()

        # Verificar si las columnas esenciales existen
        required_columns = ['id', 'name', 'age', 'nationality', 'overall', 'potential', 'value', 'wage', 'height', 'weight']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"La columna '{col}' no existe en el DataFrame")

        # Convertir las columnas numéricas necesarias a tipo numérico
        num_cols = ['age', 'overall', 'potential', 'value', 'wage', 'height', 'weight']
        for col in num_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')  # Convierte a numérico, convirtiendo errores a NaN

        # Limpiar valores en 'value', 'wage' y 'release_clause' (convertir de texto a valores numéricos)
        df['value'] = df['value'].apply(self.convert_to_numeric)
        df['wage'] = df['wage'].apply(self.convert_to_numeric)
        df['release_clause'] = df['release_clause'].apply(self.convert_to_numeric)

        # Rellenar valores nulos en columnas numéricas con 0
        df[num_cols] = df[num_cols].fillna(0)

        # Si la columna 'name' tiene valores duplicados, los eliminamos
        df = df.drop_duplicates(subset=['name'])

        # Asignar el DataFrame transformado a self.df
        self.df = df
        return self.df

    def convert_to_numeric(self, value):
        """
        Convierte valores de texto (como €100M, €1K) a valores numéricos.
        """
        if isinstance(value, str):
            value = value.replace('€', '').replace('M', '').replace('K', '').replace(',', '').strip()
            if 'M' in value:
                return float(value.replace('M', '')) * 1_000_000
            elif 'K' in value:
                return float(value.replace('K', '')) * 1_000
            try:
                return float(value)
            except ValueError:
                return None
        return value
