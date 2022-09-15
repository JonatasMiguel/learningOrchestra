from flask import jsonify, request, Flask
from setup import SetupPycaret, Parameters
from utils import Database, UserRequest, Metadata, ObjectStorage, Data
import os
from typing import Union
from constants import Constants
import logging

logging.basicConfig(filename='myapp.log', level=logging.INFO)

# Create the app object
app = Flask(__name__)

database = Database(
    os.environ[Constants.DATABASE_URL],
    os.environ[Constants.DATABASE_REPLICA_SET],
    int(os.environ[Constants.DATABASE_PORT]),
    os.environ[Constants.DATABASE_NAME],
)

request_validator = UserRequest(database)
storage = ObjectStorage(database)
data = Data(database, storage)
metadata_creator = Metadata(database)
parameters_handler = Parameters(database, data)

@app.route('/setuppycaret', methods=["POST"])
def setup() -> jsonify:
    logging.info('Requisição chegou.')
    service_type = request.args.get(Constants.TYPE_PARAM_NAME)
    model_name = request.json[Constants.MODEL_FIELD_NAME]
    description = request.json[Constants.DESCRIPTION_FIELD_NAME]
    module_path = request.json[Constants.MODULE_PATH_FIELD_NAME]
    class_name = request.json[Constants.CLASS_FIELD_NAME]
    class_parameters = request.json[Constants.FUNCTION_PARAMETERS_NAME] 

    #todo: validar o request
    logging.info('Iniciando METADATA')
    metadata_creator = Metadata(database)

    logging.info('SetupPycaret')
    setup_defalut = SetupPycaret(
            database,
            parameters_handler,
            model_name,
            service_type,
            metadata_creator,
            module_path,
            class_name,
            storage)

    logging.info('SetupPycaret create')
    setup_defalut.create(description, class_parameters)
    logging.info('Retornando ')
    return (
            jsonify({
                Constants.MESSAGE_RESULT:
                    f'{Constants.MICROSERVICE_URI_GET}{model_name}'
                    f'{Constants.MICROSERVICE_URI_GET_PARAMS}'}),
            Constants.HTTP_STATUS_CODE_SUCCESS_CREATED,
    )        