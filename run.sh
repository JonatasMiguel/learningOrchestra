#!/bin/bash

echo "learningOrchestra: a distributed machine learning processing tool"
echo "--------------------------------------------------------------------"
echo "Building the learningOrchestra microservice images..."
echo "--------------------------------------------------------------------"

docker build --tag 127.0.0.1:5000/spark_task:latest microservices/spark_task_image
docker push 127.0.0.1:5000/spark_task:latest

docker-compose build

echo "--------------------------------------------------------------------"
echo "Adding the microservice images in docker daemon security exception..."
echo "--------------------------------------------------------------------"

echo '{
  "insecure-registries" : ["myregistry:5000"]
}
' > /etc/docker/daemon.json

echo "--------------------------------------------------------------------"
echo "Restarting docker service..."
echo "--------------------------------------------------------------------"

service docker restart

echo "--------------------------------------------------------------------"
echo "Deploying learningOrchestra in swarm cluster..."
echo "--------------------------------------------------------------------"

docker stack deploy --compose-file=docker-compose.yml microservice

echo "--------------------------------------------------------------------"
echo "Pushing the microservice images in local repository..."
echo "--------------------------------------------------------------------"

sleep 30


database_api_repository=127.0.0.1:5000/database_api


echo "--------------------------------------------------------------------"
echo "Pushing databaseApi microservice image..."
echo "--------------------------------------------------------------------"
docker push $database_api_repository


spark_repository=127.0.0.1:5000/spark

echo "--------------------------------------------------------------------"
echo "Pushing spark image..."
echo "--------------------------------------------------------------------"
docker push $spark_repository


projection_repository=127.0.0.1:5000/projection

echo "--------------------------------------------------------------------"
echo "Pushing projection microservice image..."
echo "--------------------------------------------------------------------"
docker push $projection_repository


builder_repository=127.0.0.1:5000/builder

echo "--------------------------------------------------------------------"
echo "Pushing builder microservice image..."
echo "--------------------------------------------------------------------"
docker push $builder_repository


data_type_handler_repository=127.0.0.1:5000/data_type_handler

echo "--------------------------------------------------------------------"
echo "Pushing dataTypeHandler microservice image..."
echo "--------------------------------------------------------------------"
docker push $data_type_handler_repository


histogram_repository=127.0.0.1:5000/histogram

echo "--------------------------------------------------------------------"
echo "Pushing histogram microservice image..."
echo "--------------------------------------------------------------------"
docker push $histogram_repository


model_repository=127.0.0.1:5000/model

echo "--------------------------------------------------------------------"
echo "Pushing model microservice image..."
echo "--------------------------------------------------------------------"
docker push $model_repository


binary_executor_repository=127.0.0.1:5000/binary_executor

echo "--------------------------------------------------------------------"
echo "Pushing binaryExecutor microservice image..."
echo "--------------------------------------------------------------------"
docker push $binary_executor_repository


database_executor_repository=127.0.0.1:5000/database_executor

echo "--------------------------------------------------------------------"
echo "Pushing databaseExecutor microservice image..."
echo "--------------------------------------------------------------------"
docker push $database_executor_repository


code_executor_repository=127.0.0.1:5000/code_executor

echo "--------------------------------------------------------------------"
echo "Pushing codeExecutor microservice image..."
echo "--------------------------------------------------------------------"
docker push $code_executor_repository

pycaret_executor_repository=127.0.0.1:5000/pycaret_executor

echo "--------------------------------------------------------------------"
echo "Pushing pycaretExecutor microservice image..."
echo "--------------------------------------------------------------------"
docker push $pycaret_executor_repository


echo "--------------------------------------------------------------------"
echo "Updating portainer agent microservice in each cluster node..."
echo "--------------------------------------------------------------------"
docker service update --image portainer/agent  microservice_agent

echo "--------------------------------------------------------------------"
echo "End."
echo "--------------------------------------------------------------------"
