class Constants:
    MODULE_PATH_FIELD_NAME = "modulePath"
    CLASS_FIELD_NAME = "class"
    CLASS_PARAMETERS_FIELD_NAME = "classParameters"
    MODEL_FIELD_NAME = "modelName"
    FINISHED_FIELD_NAME = "finished"
    DESCRIPTION_FIELD_NAME = "description"
    TYPE_PARAM_NAME = "type"

    MODEL_SCIKITLEARN_TYPE = "model/scikitlearn"
    MODEL_TENSORFLOW_TYPE = "model/tensorflow"
    MODEL_AUTOKERAS_TYPE = "model/autokeras"

    TUNE_SCIKITLEARN_TYPE = "tune/scikitlearn"
    TUNE_TENSORFLOW_TYPE = "tune/tensorflow"
        
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
    DATASET_TENSORFLOW_TYPE = "dataset/tensorflow"
    DATASET_AUTOKERAS_TYPE = "dataset/autokeras"

    TRANSFORM_SCIKITLEARN_TYPE = "transform/scikitlearn"
    TRANSFORM_TENSORFLOW_TYPE = "transform/tensorflow"

    EXPLORE_SCIKITLEARN_TYPE = "explore/scikitlearn"
    EXPLORE_TENSORFLOW_TYPE = "explore/tensorflow"
    EXPLORE_AUTOKERAS_TYPE = "explore/autokeras"

    HTTP_STATUS_CODE_SUCCESS = 200
    HTTP_STATUS_CODE_SUCCESS_CREATED = 201
    HTTP_STATUS_CODE_CONFLICT = 409
    HTTP_STATUS_CODE_NOT_ACCEPTABLE = 406
    HTTP_STATUS_CODE_NOT_FOUND = 404
    GET_METHOD_NAME = "GET"

    DEFAULT_MODEL_HOST_IP = "DEFAULT_MODEL_HOST_IP"
    DEFAULT_MODEL_HOST_PORT = "DEFAULT_MODEL_HOST_PORT"

    EXPLORE_VOLUME_PATH = "EXPLORE_VOLUME_PATH"
    TRANSFORM_VOLUME_PATH = "TRANSFORM_VOLUME_PATH"
    MODELS_VOLUME_PATH = "MODELS_VOLUME_PATH"
    BINARY_VOLUME_PATH = "BINARY_VOLUME_PATH"
    CODE_EXECUTOR_VOLUME_PATH = "CODE_EXECUTOR_VOLUME_PATH"

    DATABASE_URL = "DATABASE_URL"
    DATABASE_PORT = "DATABASE_PORT"
    DATABASE_NAME = "DATABASE_NAME"
    DATABASE_REPLICA_SET = "DATABASE_REPLICA_SET"

    ID_FIELD_NAME = "_id"
    METADATA_DOCUMENT_ID = 0

    MESSAGE_RESULT = "result"

    DELETED_MESSAGE = "deleted file"

    FUNCTION_PARAMETERS_NAME = "classParameters"
    EXCEPTION_FIELD_NAME = "exception"

    MICROSERVICE_URI_GET = "/api/learningOrchestra/v1/model/"
    MICROSERVICE_URI_GET_PARAMS = "?query={}&limit=20&skip=0"

    FIRST_ARGUMENT = 0
    SECOND_ARGUMENT = 1
