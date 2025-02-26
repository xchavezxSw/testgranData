Technical Challenge
===

###Descripcion:

Tenemos eventos de comunicación y utilizando Apache Spark en un Docker calcularemos la facturación total de SMS, crearemos un dataset con los 100 usuarios con mayor facturación y crearemos un histograma de llamadas por hora.

###Requisitos

- Docker

- Docker Compose

- Python 3.6

- Apache Spark 2.3

###Archivos

- Dockerfile
- docker-compose.yml
- main.py: Código principal de procesamiento en PySpark.
- eventos.csv.gz: Dataset de eventos dummy.
- free_sms_destinations.csv.gz: Lista de destinos dummy.
- usuarios_top100.parquet: Dataset con los 100 usuarios con mayor facturación.
- histograma_llamadas.png: Histograma de llamadas por hora.

### Monto total facturado: $4265.50


### Instalación y Ejecución

### Construir la imagen de Docker:

- docker build -t spark_sms_analysis .
- docker-compose up -d

### Generación de Resultados

El script realiza los siguientes pasos:
- Carga y filtra los datos.
- Calcula la facturación total.
- Obtiene los 100 usuarios con mayor facturación y guarda el dataset en Parquet.
- Genera y guarda un histograma de llamadas por hora.