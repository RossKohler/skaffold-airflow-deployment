from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def print_hello():
    print("Hello, Airflow!")

def print_world():
    print("Hello, World!")

dag = DAG(
    'test_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=1),  # Change this to your desired schedule
    catchup=False,
)

task_hello = PythonOperator(
    task_id='print_hello',
    python_callable=print_hello,
    dag=dag,
)

task_world = PythonOperator(
    task_id='print_world',
    python_callable=print_world,
    dag=dag,
)

task_hello >> task_world
