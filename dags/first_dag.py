from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define the DAG
with DAG(
    dag_id='hello_airflow',
    default_args=default_args,
    description='A simple Hello Airflow DAG',
    schedule_interval='@daily',  # or None for manual trigger
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['example'],
) as dag:

    # Task 1: Print the date
    print_date = BashOperator(
        task_id='print_date',
        bash_command='date'
    )

    # Task 2: Say hello
    say_hello = BashOperator(
        task_id='say_hello',
        bash_command='echo "Hello from Airflow!"'
    )

    # Set task order
    print_date >> say_hello
