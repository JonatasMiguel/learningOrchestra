class Constants:
    FINISHED_FIELD_NAME = "finished"
    NAME_FIELD_NAME = "name"
    DESCRIPTION_FIELD_NAME = "description"
    FUNCTION_FIELD_NAME = "function"
    FUNCTION_PARAMETERS_FIELD_NAME = "functionParameters"
    TYPE_PARAM_NAME = "type"
    TOOL_PARAM_NAME = "tool"
    FUNCTION_MESSAGE_FIELD_NAME = "functionMessage"

    DEFAULT_MODEL_MICROSERVICE_TYPE = "defaultModel"
    EXCEPTION_FIELD_NAME = "exception"

    EXPLORE_VOLUME_PATH = "EXPLORE_VOLUME_PATH"
    TRANSFORM_VOLUME_PATH = "TRANSFORM_VOLUME_PATH"
    MODELS_VOLUME_PATH = "MODELS_VOLUME_PATH"
    BINARY_VOLUME_PATH = "BINARY_VOLUME_PATH"
    CODE_EXECUTOR_VOLUME_PATH = "CODE_EXECUTOR_VOLUME_PATH"
    DATASET_VOLUME_PATH = "DATASET_VOLUME_PATH"

    IMAGE_FORMAT = ".png"

    DELETED_MESSAGE = "deleted file"

    HTTP_STATUS_CODE_SUCCESS = 200
    HTTP_STATUS_CODE_SUCCESS_CREATED = 201
    HTTP_STATUS_CODE_CONFLICT = 409
    HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
    HTTP_STATUS_CODE_NOT_FOUND = 404
    GET_METHOD_NAME = "GET"

    DATABASE_URL = "DATABASE_URL"
    DATABASE_PORT = "DATABASE_PORT"
    DATABASE_NAME = "DATABASE_NAME"
    DATABASE_REPLICA_SET = "DATABASE_REPLICA_SET"

    ID_FIELD_NAME = "_id"
    METADATA_DOCUMENT_ID = 0

    MESSAGE_RESULT = "result"

    MODEL_SCIKITLEARN_TYPE = "model/scikitlearn"
    MODEL_TENSORFLOW_TYPE = "model/tensorflow"
    MODEL_AUTOKERAS_TYPE = "model/autokeras"

    TUNE_SCIKITLEARN_TYPE = "tune/scikitlearn"
    TUNE_TENSORFLOW_TYPE = "tune/tensorflow"
    TUNE_AUTOKERAS_TYPE = "tune/autokeras"

    TRAIN_SCIKITLEARN_TYPE = "train/scikitlearn"
    TRAIN_TENSORFLOW_TYPE = "train/tensorflow"
    TRAIN_AUTOKERAS_TYPE = "train/autokeras"

    EVALUATE_SCIKITLEARN_TYPE = "evaluate/scikitlearn"
    EVALUATE_TENSORFLOW_TYPE = "evaluate/tensorflow"
    EVALUATE_AUTOKERAS_TYPE = "evaluate/autokeras"

    PREDICT_SCIKITLEARN_TYPE = "predict/scikitlearn"
    PREDICT_TENSORFLOW_TYPE = "predict/tensorflow"
    PREDICT_AUTOKERAS_TYPE = "predict/autokeras"

    PYTHON_FUNCTION_TYPE = "function/python"
    DATASET_GENERIC_TYPE = "dataset/generic"

    TRANSFORM_SCIKITLEARN_TYPE = "transform/scikitlearn"
    TRANSFORM_TENSORFLOW_TYPE = "transform/tensorflow"
    TRANSFORM_AUTOKERAS_TYPE = "transform/autokeras"

    EXPLORE_SCIKITLEARN_TYPE = "explore/scikitlearn"
    EXPLORE_TENSORFLOW_TYPE = "explore/tensorflow"
    EXPLORE_AUTOKERAS_TYPE = "explore/autokeras"

    API_PATH = "/api/learningOrchestra/v1/"

    MICROSERVICE_URI_SWITCHER = {
        PYTHON_FUNCTION_TYPE: f'{API_PATH}{PYTHON_FUNCTION_TYPE}'
    }

    MICROSERVICE_URI_PATH = "/codeExecutor"
    MICROSERVICE_URI_GET_PARAMS = "?query={}&limit=20&skip=0"

    FIRST_ARGUMENT = 0
    SECOND_ARGUMENT = 1
