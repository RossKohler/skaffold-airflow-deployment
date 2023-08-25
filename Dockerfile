FROM apache/airflow:2.6.2-python3.10

USER airflow
COPY --chown=airflow:root dags dags