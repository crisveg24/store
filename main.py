# main.py
import logging
import os
from Config.config import Config
from Extract.extractor import Extractor
from Transform.transformer import Transformer
from Load.loader import Loader
import sqlite3

# Configuración de logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    logging.info("Iniciando proceso ETL")

    try:
        # Rutas de entrada y salida
        input_path = "/workspaces/store/Extract/Files/Stores_clean.csv"
        output_path = "/workspaces/store/Extract/Files/Store_final.csv"

        # 0️⃣ Crear carpeta de la base de datos si no existe
        db_folder = os.path.dirname(Config.SQLITE_DB_PATH)
        os.makedirs(db_folder, exist_ok=True)  # asegura creación de carpeta
        logging.info(f"Carpeta de la base de datos verificada/creada: {db_folder}")

        # 1️⃣ Crear archivo SQLite y tabla si no existen
        conn = sqlite3.connect(Config.SQLITE_DB_PATH)
        cursor = conn.cursor()
        # Crear tabla dinámica según columnas del DataFrame
        # Si quieres usar columnas fijas, puedes escribirlas aquí; pero el Loader dinámico lo hará automáticamente
        conn.commit()
        conn.close()
        logging.info(f"Archivo SQLite preparado: {Config.SQLITE_DB_PATH}")

        # 2️⃣ EXTRAER
        logging.info("Extrayendo datos...")
        extractor = Extractor(input_path)
        df_raw = extractor.extract()
        if df_raw is None or df_raw.empty:
            logging.error("No se pudieron extraer datos.")
            return
        logging.info(f"Datos extraídos correctamente de {input_path} ({len(df_raw)} registros)")

        # 3️⃣ TRANSFORMAR
        logging.info("Transformando datos...")
        transformer = Transformer(df_raw)
        df_clean = transformer.transform()
        logging.info(f"Datos transformados: {len(df_clean)} registros")

        # 4️⃣ CARGAR
        logging.info("Cargando datos...")
        loader = Loader(df_clean)
        loader.to_csv(output_path)
        loader.to_sqlite()  # Guarda en SQLite dinámicamente según columnas del DataFrame
        logging.info(f"Datos guardados en {output_path} y en SQLite: {Config.SQLITE_DB_PATH}")

    except Exception as e:
        logging.error(f"Error en el proceso ETL: {e}")

if __name__ == "__main__":
    main()