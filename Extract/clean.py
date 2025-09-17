import pandas as pd

# Leer el archivo CSV
df = pd.read_csv("Extract/Files/fifa_eda_stats.csv")

# Verificar las primeras filas para inspección
print("Primeras filas del archivo original:")
print(df.head())

# 1. Eliminar duplicados
df = df.drop_duplicates()
print(f"Filas después de eliminar duplicados: {df.shape[0]}")

# 2. Eliminar filas con valores vacíos en columnas clave (por ejemplo, 'Name', 'Nationality', 'Overall')
df = df.dropna(subset=['Name', 'Nationality', 'Overall'])
print(f"Filas después de eliminar filas vacías en columnas clave: {df.shape[0]}")

# 3. Normalizar nombres de columnas
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace(r"[^\w\s]", "")  # Eliminamos caracteres especiales
print("Nombres de columnas normalizados:")
print(df.columns)

# 4. Convertir 'Value', 'Wage' y 'Release Clause' a formato numérico
def convert_to_numeric(value):
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

df['value'] = df['value'].apply(convert_to_numeric)
df['wage'] = df['wage'].apply(convert_to_numeric)
df['release_clause'] = df['release_clause'].apply(convert_to_numeric)

# 5. Convertir 'Height' y 'Weight' a números (quitar cm y kg)
def convert_height(height):
    if isinstance(height, str):
        if "'" in height and '"' in height:
            feet, inches = height.split("'")
            inches = inches.replace('"', '').strip()
            # Convertir a centímetros
            total_inches = (int(feet) * 12) + int(inches)
            return total_inches * 2.54  # Convertir pulgadas a centímetros
        elif 'cm' in height:
            return float(height.replace('cm', '').strip())
    return height

df['height'] = df['height'].apply(convert_height)

# Convertir 'Weight' a número (quitar kg y convertir lbs a kg)
def convert_weight(weight):
    if isinstance(weight, str):
        if 'kg' in weight:
            return float(weight.replace('kg', '').strip())
        elif 'lbs' in weight:
            # Convertir de libras a kilogramos
            return float(weight.replace('lbs', '').strip()) * 0.453592
    return weight

df['weight'] = df['weight'].apply(convert_weight)

# 6. Rellenar valores nulos en columnas no críticas, como 'Preferred Foot', 'Work Rate', etc., con un valor por defecto o 'Unknown'
df['preferred_foot'] = df['preferred_foot'].fillna('Unknown')
df['work_rate'] = df['work_rate'].fillna('Unknown')

# 7. Guardar el archivo limpio
df.to_csv("Extract/Files/fifa_eda_stats_clean.csv", index=False)

print("CSV limpio guardado en 'fifa_eda_stats_clean.csv'")
