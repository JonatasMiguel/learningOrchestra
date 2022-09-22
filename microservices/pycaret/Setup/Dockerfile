FROM python:3.7-slim

WORKDIR /usr/src/model
COPY . /usr/src/model

RUN apt-get update && apt-get install -y libgomp1
RUN pip install --trusted-host pypi.python.org -r requirements.txt

RUN pip install -r requirements.txt

ENV DEFAULT_MODEL_HOST_IP "0.0.0.0"
ENV DEFAULT_MODEL_HOST_PORT 5005

ENV EXPLORE_VOLUME_PATH "/explore"
ENV TRANSFORM_VOLUME_PATH "/transform"
ENV BINARY_VOLUME_PATH "/binaries"
ENV MODELS_VOLUME_PATH "/models"
ENV CODE_EXECUTOR_VOLUME_PATH "/code_executions"

CMD ["python", "server.py"]