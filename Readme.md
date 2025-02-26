Technical Challenge
===

### Descripcion:

Tenemos eventos de comunicación y utilizando Apache Spark en un Docker calcularemos la facturación total de SMS, crearemos un dataset con los 100 usuarios con mayor facturación y crearemos un histograma de llamadas por hora.

### Requisitos

- Docker

- Docker Compose

- Python 3.6

- Apache Spark 2.3

### Archivos

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

### Preguntas
- La empresa cuenta con un cluster on premise de Hadoop en el cual se ejecuta, tanto el
data pipeline principal de los datos, como los análisis exploratorios de los equipos de
Data Science y Data Engineering. Teniendo en cuenta que cada proceso compite por un
número específico de recursos del cluster:
- ¿Cómo priorizaría los procesos productivos sobre los procesos de análisis
exploratorios?
> Sobreentiendo que como se utiliza spark, tiene un administrador de recursos como yarn, por consecuencia, crearia dos colas, donde una va a tener alta prioridad de recursos y otra baja prioridad con recursos limitados.
- Debido a que los procesos productivos del pipeline poseen un uso intensivo
tanto de CPU como de memoria, ¿qué estrategia utilizaría para administrar su
ejecución durante el día? ¿qué herramientas de scheduling conoce para tal fin?
> utilizaria airflow, para manejar el scheduling
- Existe una tabla del Data Lake con alta transaccionalidad, que es actualizada
diariamente con un gran volumen de datos. Consultas que cruzan información con esta
tabla ven afectada su performance en tiempos de respuesta.
Según su criterio, ¿cuáles serían las posibles causas de este problema? Dada la
respuesta anterior, qué sugeriría para solucionarlo
> propondria utilizar particiones en hive, para mejorar la cantidad de recursos, y habilitaria un spark cache como para poder reutilziar los datos recurrentes
- Imagine un clúster Hadoop de 3 nodos, con 50 GB de memoria y 12 cores por nodo.
Necesita ejecutar un proceso de Spark que utilizará la mitad de los recursos del clúster,
dejando la otra mitad disponible para otros jobs que se lanzarán posteriormente.
¿Qué configuraciones en la sesión de Spark implementaría para garantizar que la mitad
del clúster esté disponible para los jobs restantes?
Proporcione detalles sobre la asignación de recursos, configuraciones de Spark, y
cualquier otra configuración relevante
> haria el famoso calculo de memoria x ejecutor, en este caso tenemos:
3 nodos de 50 gb, total de 150gb de ram 
3 nodos con 12 cores, total 36 cores
asique, asignaria 72 gb de ram y 18 cores, y le dejaria 4 al driver
  spark.executor.instances=9
  spark.executor.cores=2
  spark.executor.memory=8G
  spark.driver.memory=4G
esta configuracion la podemos poner al momento de hacer el sparksession o al momento de llamar al spark-submit
