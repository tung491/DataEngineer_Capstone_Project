from datetime import datetime, timedelta

from airflow import DAG
from airflow.helpers.sql_queries import *
from airflow.operators import DataQualityOperator
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

# Set default argument
default_args = {
    'owner': 'tung491',
    'start_date': datetime(2020, 5, 14),
    'depends_on_past': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False
}

# Create DAG
dag = DAG('etl', default_args=default_args,
          description='Load and transform CSV files into Postgres',
          )

# Define the python callable for tasks
def create_us_accident():
    conn = psycopg2.connect("host='localhost' port=5433 dbname='postgres' user='tung491' password='Tung2001'")
    cursor = conn.cursor()

    cursor.execute(us_accidents_create)
    conn.commit()


def create_us_cities_demo():
    conn = psycopg2.connect("host='localhost' port=5433 dbname='postgres' user='tung491' password='Tung2001'")
    cursor = conn.cursor()

    cursor.execute(us_cities_demo_create)
    conn.commit()


def copy_table_us_accident():
    conn = psycopg2.connect("host='localhost' port=5433 dbname='postgres' user='tung491' password='Tung2001'")
    cursor = conn.cursor()
    cursor.execute(us_accidents_copy)
    conn.commit()


def copy_table_us_cities_demo():
    conn = psycopg2.connect("host='localhost' port=5433 dbname='postgres' user='tung491' password='Tung2001'")
    cursor = conn.cursor()

    cursor.execute(us_cities_demo_copy)

# Define Airflow tasks
start_operator = DummyOperator(task_id='Begin_execution', dag=dag)
create_accident_table = PythonOperator(task_id='Create US accident table',
                                       dag=dag,
                                       python_callable=create_us_accident)

create_demo_table = PythonOperator(task_id='Create US demographic table',
                                   dag=dag,
                                   python_callable=create_us_cities_demo)

copy_accident_table = PythonOperator(task_id='Create US accident table',
                                     dag=dag,
                                     python_callable=copy_table_us_accident)

copy_demo_table = PythonOperator(task_id="Copy US demographic table",
                                 dag=dag,
                                 python_callable=copy_table_us_cities_demo)

run_quality_checks = DataQualityOperator(
        task_id='Run_data_quality_checks',
        dag=dag,
        conn_id='postgres',
        tables=['us_cities_demographics', 'us_accident']
)

end_operator = DummyOperator(task_id='Stop_execution', dag=dag)

# Set dependencies.
start_operator >> create_accident_table >> copy_accident_table >> end_operator
start_operator >> create_demo_table >> copy_demo_table >> end_operator
