Configuración del ETL – Carpeta config

La carpeta config contiene los parámetros y rutas esenciales que utiliza el ETL para procesar y almacenar los datos de la base de datos de tiendas (Stores). Centralizar la configuración permite modificar rutas y nombres de tablas sin afectar la lógica de procesamiento del ETL.
Buenas prácticas

Mantener las rutas relativas o absolutas consistentes para facilitar la ejecución del ETL en distintos entornos.

Centralizar la configuración permite modificar la base de datos o el archivo de entrada sin tocar el código de extracción, transformación o carga.

Es recomendable no incluir datos sensibles directamente en esta configuración; si en el futuro se agregan credenciales para conexiones externas, estas deberían ir en un archivo .env.

Resumen

La clase Config actúa como un punto único de referencia para todos los parámetros importantes del ETL, garantizando que el código sea más mantenible, reutilizable y fácil de adaptar a nuevos entornos o archivos de datos.