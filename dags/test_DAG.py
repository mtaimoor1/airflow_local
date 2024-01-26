from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import DagRun


default_args = {
    "owner": "Taimoor",
    "start_date": "2023-10-20",
    "retries": 0,
    "depends_on_past": True,
    "wait_for_downstream": True,
}


def compute_prev_run_date(dag_id, exec_date):
    dag_runs = DagRun.find(dag_id=dag_id, execution_end_date=exec_date)
    dag_runs.sort(key=lambda x: x.execution_date, reverse=True)
    return (
        dag_runs[1].end_date.strftime("%Y-%m-%d %H:%M:%S")
        if len(dag_runs) > 1
        else "2023-12-06 08:00:00"
    )


def teste(a, **kwargs):
    print(kwargs["ti"].execution_date)
    print("~~~~~~", kwargs["execution_date"].format("HH") == "18")
    print("###~~~~~~", type(kwargs["execution_date"].format("HH")))
    print("#~~~~~~", str(kwargs["execution_date"].format("HH")) == "18")
    print("~~~~~~~~~~~~~~", a)


def test2():
    print("This is function 2")
    raise Exception


with DAG(
    "test_DAG",
    default_args=default_args,
    schedule_interval="* * * * *",
    catchup=False,
    user_defined_macros={"prev_run_date": compute_prev_run_date},
    description="Gets all the trip data and dump it to postgres",
) as dag:
    a = PythonOperator(
        task_id="teste",
        python_callable=teste,
        op_kwargs={
            "a": '{{ prev_run_date( "test_DAG", execution_date) }}',
        },
    )
    b = PythonOperator(task_id="test2", python_callable=test2)

    a >> b
