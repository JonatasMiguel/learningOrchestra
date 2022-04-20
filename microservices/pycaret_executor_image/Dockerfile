FROM pycaret/full

WORKDIR /usr/src/code_executor
COPY . /usr/src/code_executor


RUN sudo apt-get update && apt-get install -y libgomp1
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install -r requirements.txt

ENV MICROSERVICE_IP "0.0.0.0"
ENV MICROSERVICE_PORT 5010
ENV EXPLORE_VOLUME_PATH "/explore"
ENV TRANSFORM_VOLUME_PATH "/transform"
ENV BINARY_VOLUME_PATH "/binaries"
ENV MODELS_VOLUME_PATH "/models"
ENV CODE_EXECUTOR_VOLUME_PATH "/code_executions"
ENV DATASET_VOLUME_PATH "/datasets"

CMD ["python", "server.py"]