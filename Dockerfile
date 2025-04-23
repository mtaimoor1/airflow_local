FROM apache/airflow:3.0.0

ENV APP_HOME="/opt"

# Install Airflow
ENV AIRFLOW_HOME="${APP_HOME}/airflow"

COPY requirements.txt ${AIRFLOW_HOME}/requirements.txt
RUN python3 -m pip install --no-cache-dir -r ${AIRFLOW_HOME}/requirements.txt

WORKDIR ${AIRFLOW_HOME}

COPY config/connections.json ${AIRFLOW_HOME}
COPY config/variables.json ${AIRFLOW_HOME}
COPY entrypoint.sh ${APP_HOME}
#COPY dags ${AIRFLOW_HOME}/dags

RUN mkdir -p ${AIRFLOW_HOME}/data/processed
RUN touch /opt/airflow/pass.json

ENTRYPOINT [ "/opt/entrypoint.sh" ]
