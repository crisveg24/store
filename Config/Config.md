Configuración del ETL – Carpeta config

La carpeta config contiene los parámetros y rutas esenciales que utiliza el ETL para procesar y almacenar los datos de los jugadores de fútbol. Centralizar la configuración permite modificar rutas, nombres de tablas y otros parámetros sin afectar la lógica de procesamiento del ETL.

Buenas prácticas

Consistencia de rutas: Mantener las rutas relativas o absolutas consistentes facilita la ejecución del ETL en distintos entornos, ya sea localmente, en un servidor o en un entorno de nube como GitHub Codespaces.

Centralización de la configuración: Centralizar los parámetros críticos, como la base de datos de SQLite y los archivos de entrada, permite modificar estas configuraciones sin tocar el código de extracción, transformación o carga. Esto hace que el código sea más flexible y fácil de mantener.

Evitar la inclusión de datos sensibles: Si en el futuro se agregan credenciales para conexiones externas (por ejemplo, bases de datos remotas), estas deberían almacenarse de manera segura, por ejemplo, en un archivo .env y no en el código fuente.

Manejo de archivos de entrada y salida: Es importante que los archivos de entrada, como los CSVs, y las rutas de salida, como los archivos generados por el ETL (por ejemplo, archivos PNG o CSV de las gráficas), estén correctamente definidos para facilitar su ubicación y acceso.

Resumen

La clase Config actúa como un punto único de referencia para todos los parámetros importantes del ETL, garantizando que el código sea más mantenible, reutilizable y fácil de adaptar a nuevos entornos o archivos de datos. Centralizar la configuración también facilita la modificación de rutas y la actualización de parámetros sin necesidad de cambiar el código de los módulos de extracción, transformación o carga.