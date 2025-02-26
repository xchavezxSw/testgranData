import gzip
import csv
import random
from datetime import datetime
archivo_eventos = "eventos.csv.gz"
archivo_destinos = "free_sms_destinations.csv.gz"
columns = [
    "id_source", "id_destination", "region", "date", "hour", "calls", "seconds", "sms"
]
rownum = 1000

def generate_random_data():
    id_source = random.randint(1000, 9999)
    id_destination = random.randint(1000, 9999)
    region =random.randint(1,9)
    date = datetime.now().strftime("%Y%m%d")
    hour = random.randint(0, 23)
    calls = random.randint(0, 10)
    seconds = random.randint(0, 600) if calls > 0 else 0
    sms = random.randint(0, 5)
    return [id_source, id_destination, region, date, hour, calls, seconds, sms]
destinosGratuitos=[]
with gzip.open(archivo_eventos, "wt", newline='', encoding="utf-8") as gzfile:
    writer = csv.writer(gzfile)
    writer.writerow(columns)  # Escribir encabezado
    for _ in range(rownum):
        variable=generate_random_data()
        if len(destinosGratuitos)<=100:
            destinosGratuitos.append(variable[1])
        writer.writerow(variable)

with gzip.open(archivo_destinos, "wt", newline='', encoding="utf-8") as gzfile:
    writer = csv.writer(gzfile)
    writer.writerow(destinosGratuitos)
