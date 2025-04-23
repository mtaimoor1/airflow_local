#!/bin/sh

echo "Initializing Airflow Database..."
airflow db migrate
echo "Your environment is ready."

# variables
airflow variables import variables.json

# connections
airflow connections import connections.json --overwrite

exec "${@}"
