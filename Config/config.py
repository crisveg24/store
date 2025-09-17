class Config:
    """
    Clase de configuración para rutas y parámetros del ETL.
    """
    # Ruta del archivo CSV limpio
    INPUT_PATH = '/workspaces/store/Extract/Files/fifa_eda_stats_clean.csv'
    
    # Ruta de la base de datos SQLite
    SQLITE_DB_PATH = '/workspaces/store/Extract/Files/fifaeda_data.db'
    
    # Nombre de la tabla en la base de datos SQLite
    SQLITE_TABLE = 'fifa_players_data'
