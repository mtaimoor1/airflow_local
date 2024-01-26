#!/bin/sh

echo "Initializing Airflow Database..."
airflow db init

airflow db upgrade
echo "Your environment is ready."

airflow users create --username admin --password admin --firstname Taimoor --lastname Abbasi --role Admin --email taimoor@email.com
# variables
airflow variables import variables.json

# connections
airflow connections import connections.json --overwrite

exec "${@}"
