#!/bin/bash

echo "--------------------------------------------------------------------"
cat << "EOF"
  _                      _            ___         _           _            
 | |   ___ __ _ _ _ _ _ (_)_ _  __ _ / _ \ _ _ __| |_  ___ __| |_ _ _ __ _ 
 | |__/ -_) _` | '_| ' \| | ' \/ _` | (_) | '_/ _| ' \/ -_|_-<  _| '_/ _` |
 |____\___\__,_|_| |_||_|_|_||_\__, |\___/|_| \__|_||_\___/__/\__|_| \__,_|
                               |___/                                       
    _       _       __  __ _                                               
   /_\ _  _| |_ ___|  \/  | |                                              
  / _ \ || |  _/ _ \ |\/| | |__                                            
 /_/ \_\_,_|\__\___/_|  |_|____|                                           
                                                                           

EOF

echo "                       a distributed machine learning processing tool"
echo "--------------------------------------------------------------------"



echo "--------------------------------------------------------------------"
echo "Deploying learningOrchestra in swarm cluster..."
echo "--------------------------------------------------------------------"

docker stack deploy --compose-file=docker-compose.yml microservice

echo "--------------------------------------------------------------------"
echo "Updating portainer agent microservice in each cluster node..."
echo "--------------------------------------------------------------------"
docker service update --image portainer/agent  microservice_agent

echo "--------------------------------------------------------------------"
echo "End."
echo "--------------------------------------------------------------------"
