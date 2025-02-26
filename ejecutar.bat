docker build -t spark_sms_analysis .
docker-compose up -d
docker exec -it spark_container bash
jupyter notebook --ip 0.0.0.0 --port=8888 --allow-root