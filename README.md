# Pipeline ETL FIFA con PySpark

Este proyecto implementa un pipeline ETL (Extract, Transform, Load) distribuido para procesar datos de jugadores de FIFA utilizando PySpark. El sistema está diseñado para manejar grandes volúmenes de datos de manera eficiente, aprovechando las capacidades de procesamiento distribuido de Apache Spark.

## Características Principales

- Procesamiento distribuido con PySpark
- Análisis de datos de jugadores FIFA
- Visualizaciones estadísticas avanzadas
- Almacenamiento en SQLite y CSV
- Pipeline ETL modular y escalable

## Arquitectura

El proyecto sigue una arquitectura modular dividida en tres componentes principales:

### 1. Extracción (Extract)
- Lectura de datos CSV usando PySpark DataFrames
- Validación inicial de datos
- Manejo de formatos y codificación

### 2. Transformación (Transform)
- Limpieza de datos usando operaciones de PySpark
- Normalización de valores monetarios y numéricos
- Análisis por continente y nacionalidad
- Generación de visualizaciones estadísticas

### 3. Carga (Load)
- Almacenamiento en SQLite
- Exportación a CSV
- Generación de reportes gráficos

## Estructura del Proyecto
```
store/
├── Config/
│   └── config.py              # Configuraciones globales
├── Extract/
│   ├── Files/                 # Archivos de datos
│   └── extractor.py          # Lógica de extracción con PySpark
├── Transform/
│   ├── transformer.py        # Transformaciones usando PySpark
│   └── graficas_new.py      # Generación de visualizaciones
├── Load/
│   └── loader.py            # Carga de datos optimizada
└── main_pyspark_new.py      # Script principal de orquestación

## Requisitos

- Python 3.6+
- Java 8+ (requerido para Spark)
- PySpark 3.5.0+
- findspark 2.0.1+
- pandas
- seaborn
- matplotlib
- SQLite3

## Instalación

1. Asegúrate de tener Java instalado:
```bash
java -version
```

2. Instala las dependencias:
```bash
pip install -r Requirements
```

## Configuración

El proyecto requiere algunas configuraciones iniciales:

1. Estructura de directorios:
```bash
mkdir -p Extract/Files
```

2. Archivos de datos:
- Coloca el archivo `fifa_eda_stats_clean.csv` en `Extract/Files/`

## Uso

Para ejecutar el pipeline completo:

```bash
python main_pyspark_new.py
```

## Visualizaciones Generadas

El pipeline genera tres tipos de visualizaciones:

1. **Valor vs Overall**: Relación entre el valor del jugador y su puntuación general
2. **Valor Promedio por Continente**: Análisis del valor de jugadores por región
3. **Distribución del Valor**: Distribución estadística de valores por continente

## Rendimiento

El sistema está optimizado para procesamiento distribuido con las siguientes configuraciones:

- Memoria del driver: 2GB
- Memoria del executor: 2GB
- Arrow habilitado para optimización pandas-spark
- Timezone UTC para consistencia temporal

## Manejo de Errores

El sistema incluye:
- Logging detallado
- Manejo de excepciones robusto
- Limpieza automática de recursos
- Validación de datos en cada etapa

## Contribuciones

Las contribuciones son bienvenidas. Por favor, asegúrate de:

1. Mantener la estructura modular
2. Documentar el código nuevo
3. Seguir las convenciones de PEP 8
4. Incluir pruebas cuando sea posible

## Autor

Cristian Vega
