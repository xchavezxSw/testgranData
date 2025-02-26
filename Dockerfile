FROM jupyter/pyspark-notebook:latest
WORKDIR /home/jovyan/work
COPY . .
RUN pip install pandas matplotlib
CMD ["start.sh", "jupyter", "notebook", "--NotebookApp.token=''"]