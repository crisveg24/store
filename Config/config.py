class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    INPUT_PATH = '/workspaces/store/Extract/Files/Stores.csv'
    SQLITE_DB_PATH = '/workspaces/store/Extract/Files/etl_data.db'
    SQLITE_TABLE = 'store_bookings_clean'