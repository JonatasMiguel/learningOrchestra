from flask import jsonify, request, Flask
import os
from code_execution import Parameters, Function, Execution
from utils import Data, Database, UserRequest, Metadata, ObjectStorage
from typing import Union
from constants import Constants


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
function_treat = Function()


@app.route(Constants.MICROSERVICE_URI_PATH, methods=["POST"])
def create_execution() -> jsonify:
    filename = request.json[Constants.NAME_FIELD_NAME]

    try:
        with open('logs.txt','a') as f:
            f.write('Chegou requisição\n')

        description = request.json[Constants.DESCRIPTION_FIELD_NAME]
        service_type = request.args.get(Constants.TYPE_PARAM_NAME)
        function_parameters = request.json[Constants.FUNCTION_PARAMETERS_FIELD_NAME]
        function = request.json[Constants.FUNCTION_FIELD_NAME]

        request_errors = analyse_post_request_errors(
            request_validator,
            filename
        )

        if request_errors is not None:
            return request_errors

        execution = Execution(
            database,
            filename,
            service_type,
            storage,
            metadata_creator,
            parameters_handler,
            function_treat)

        execution.create(function, function_parameters, description)    
    except Exception as error:
        with open('resultados.txt', 'a') as f:
            f.write(f'erro: {error.__cause__}\n')
            f.write(f'erro: {repr(error)}\n')
            f.write(f'erro: {str(error)}\n')
    
    return (
        jsonify({
            Constants.MESSAGE_RESULT:
                f'{Constants.MICROSERVICE_URI_SWITCHER[service_type]}'
                f'{filename}{Constants.MICROSERVICE_URI_GET_PARAMS}'}),
        Constants.HTTP_STATUS_CODE_SUCCESS_CREATED,
    )


@app.route(f'{Constants.MICROSERVICE_URI_PATH}/<filename>', methods=["PATCH"])
def update_execution(filename: str) -> jsonify:
    service_type = request.args.get(Constants.TYPE_PARAM_NAME)
    description = request.json[Constants.DESCRIPTION_FIELD_NAME]
    function = request.json[Constants.FUNCTION_FIELD_NAME]
    function_parameters = request.json[Constants.FUNCTION_PARAMETERS_FIELD_NAME]

    request_errors = analyse_patch_request_errors(
        request_validator,
        filename)

    if request_errors is not None:
        return request_errors

    execution = Execution(
        database,
        filename,
        service_type,
        storage,
        metadata_creator,
        parameters_handler,
        function_treat)

    execution.update(function, function_parameters, description)

    return (
        jsonify({
            Constants.MESSAGE_RESULT:
                f'{Constants.MICROSERVICE_URI_SWITCHER[service_type]}'
                f'{filename}{Constants.MICROSERVICE_URI_GET_PARAMS}'}),
        Constants.HTTP_STATUS_CODE_SUCCESS_CREATED,
    )


@app.route(f'{Constants.MICROSERVICE_URI_PATH}/<filename>', methods=["DELETE"])
def delete_default_model(filename: str) -> jsonify:
    try:
        request_validator.existent_filename_validator(
            filename
        )
    except Exception as nonexistent_model_filename:
        return (
            jsonify(
                {Constants.MESSAGE_RESULT: str(nonexistent_model_filename)}),
            Constants.HTTP_STATUS_CODE_NOT_FOUND
        )

    storage.delete(filename)

    return (
        jsonify({
            Constants.MESSAGE_RESULT: Constants.DELETED_MESSAGE}),
        Constants.HTTP_STATUS_CODE_SUCCESS,
    )


def analyse_post_request_errors(request_validator: UserRequest,
                                filename: str) \
        -> Union[tuple, None]:
    try:
        request_validator.not_duplicated_filename_validator(
            filename
        )
    except Exception as duplicated_filename:
        return (
            jsonify({Constants.MESSAGE_RESULT: str(duplicated_filename)}),
            Constants.HTTP_STATUS_CODE_CONFLICT,
        )

    return None


def analyse_patch_request_errors(request_validator: UserRequest,
                                 filename: str) \
        -> Union[tuple, None]:
    try:
        request_validator.existent_filename_validator(
            filename
        )
    except Exception as nonexistent_filename:
        return (
            jsonify(
                {Constants.MESSAGE_RESULT: str(nonexistent_filename)}),
            Constants.HTTP_STATUS_CODE_NOT_FOUND,
        )

    return None


if __name__ == "__main__":
    app.run(
        host=os.environ["MICROSERVICE_IP"],
        port=int(os.environ["MICROSERVICE_PORT"])
    )
