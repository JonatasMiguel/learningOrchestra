import importlib
from concurrent.futures import ThreadPoolExecutor
from utils import Database, Data, Metadata, ObjectStorage
from constants import Constants
import traceback
import logging

class Parameters:
    __DATASET_KEY_CHARACTER = "$"
    __CLASS_INSTANCE_CHARACTER = "#"
    __DATASET_WITH_OBJECT_KEY_CHARACTER = "."
    __REMOVE_KEY_CHARACTER = ""

    def __init__(self, database: Database, data: Data):
        self.__database_connector = database
        self.__data = data

    def treat(self, method_parameters: dict) -> dict:
        logging.info('Start Parameters treat') 
        parameters = method_parameters.copy()
        logging.info('Start Parameters copy') 
        for name, value in parameters.items():
            if type(value) is list:
                new_value = []
                for item in value:
                    new_value.append(self.__treat_value(item))
                parameters[name] = new_value
            else:
                parameters[name] = self.__treat_value(value)
        logging.info('finish Parameters treat') 
        return parameters

    def __treat_value(self, value: object) -> object:
        if self.__is_dataset(value):
            logging.info('Start __get_dataset_name_from_value') 
            dataset_name = self.__get_dataset_name_from_value(
                value)
            logging.info('Start __has_dot_in_dataset_name') 
            if self.__has_dot_in_dataset_name(value):
                object_name = self.__get_name_after_dot_from_value(value)
                return self.__data.get_object_from_dataset(
                    dataset_name, object_name)

            else:
                return self.__data.get_dataset_content(
                    dataset_name)

        elif self.__is_a_class_instance(value):
            return self.__get_a_class_instance(value)

        else:
            return value

    def __get_a_class_instance(self, class_code: str) -> object:
        class_instance_name = "class_instance"
        class_instance = None
        context_variables = {}

        class_code = class_code.replace(
            self.__CLASS_INSTANCE_CHARACTER,
            f'{class_instance_name}=')

        import tensorflow
        exec(class_code, locals(), context_variables)

        return context_variables[class_instance_name]

    def __is_a_class_instance(self, value: object) -> bool:
        if type(value) != str:
            return False
        else:
            return self.__CLASS_INSTANCE_CHARACTER in value

    def __is_dataset(self, value: object) -> bool:
        if type(value) != str:
            return False
        else:
            return self.__DATASET_KEY_CHARACTER in value

    def __get_dataset_name_from_value(self, value: str) -> str:
        dataset_name = value.replace(self.__DATASET_KEY_CHARACTER,
                                     self.__REMOVE_KEY_CHARACTER)
        return dataset_name.split(self.__DATASET_WITH_OBJECT_KEY_CHARACTER)[
            Constants.FIRST_ARGUMENT]

    def __has_dot_in_dataset_name(self, dataset_name: str) -> bool:
        return self.__DATASET_WITH_OBJECT_KEY_CHARACTER in dataset_name

    def __get_name_after_dot_from_value(self, value: str) -> str:
        return value.split(
            self.__DATASET_WITH_OBJECT_KEY_CHARACTER)[Constants.SECOND_ARGUMENT]


class Execution:
    __DATASET_KEY_CHARACTER = "$"
    __REMOVE_KEY_CHARACTER = ""

    def __init__(self,
                 database_connector: Database,
                 executor_name: str,
                 executor_service_type: str,
                 parent_name: str,
                 parent_name_service_type: str,
                 metadata_creator: Metadata,
                 class_method: str,
                 parameters_handler: Parameters,
                 storage: ObjectStorage,
                 ):
        self.__metadata_creator = metadata_creator
        self.__thread_pool = ThreadPoolExecutor()
        self.__database_connector = database_connector
        self.__storage = storage
        self.__parameters_handler = parameters_handler
        self.executor_name = executor_name
        self.parent_name = parent_name
        self.class_method = class_method
        self.executor_service_type = executor_service_type
        self.parent_name_service_type = parent_name_service_type

    def create(self,
               module_path: str,
               class_name: str,
               method_parameters: dict,
               description: str) -> None:

        self.__metadata_creator.create_file(self.parent_name,
                                            self.executor_name,
                                            module_path,
                                            class_name,
                                            self.class_method,
                                            self.executor_service_type)

        self.__thread_pool.submit(self.__pipeline,
                                  module_path,
                                  method_parameters,
                                  description)

    def update(self,
               module_path: str,
               method_parameters: dict,
               description: str) -> None:
        self.__metadata_creator.update_finished_flag(self.executor_name, False)

        self.__thread_pool.submit(self.__pipeline,
                                  module_path,
                                  method_parameters,
                                  description)

    def __pipeline(self,
                   module_path: str,
                   method_parameters: dict,
                   description: str) -> None:
        try:
            logging.info('Start __pipeline')
            importlib.import_module(module_path)
            logging.info('Start import_module')
            model_instance = self.__storage.read(self.parent_name,
                                                 self.parent_name_service_type)
            logging.info('Start __storage.read')                                     
            method_result = self.__execute_a_object_method(model_instance,
                                                           self.class_method,
                                                           method_parameters)
            logging.info('Start __execute_a_object_method')                                                           
            self.__storage.save(method_result, self.executor_name,
                                self.executor_service_type)
            logging.info('Start save')                                
            self.__metadata_creator.update_finished_flag(self.executor_name,
                                                         flag=True)
            logging.info('Start update_finished_flag')                                                 

        except Exception as exception:
            logging.warn(f'Exception: {str(exception)}')
            traceback.print_exc()
            self.__metadata_creator.create_execution_document(
                self.executor_name,
                description,
                method_parameters,
                repr(exception))
            return None

        self.__metadata_creator.create_execution_document(self.executor_name,
                                                          description,
                                                          method_parameters,
                                                          )

    def __execute_a_object_method(self, class_instance: object, method: str,
                                  parameters: dict) -> object:
        logging.info('Start getattr')
        logging.info(f'=====> class_instance: {class_instance} ')          
        logging.info(f'=====> method: {method} ')                    
        class_method = getattr(class_instance, method)
        logging.info('Start self.__parameters_handler.treat(parameters)') 
        treated_parameters = self.__parameters_handler.treat(parameters)
        logging.info('Start class_method(**treated_parameters)')
        logging.info(f'=====> treated_parameters: {treated_parameters} ') 
        logging.info(f'=====> class_method: {class_method} ')  
        method_result = class_method(**treated_parameters)

        if self.executor_service_type == Constants.TRAIN_TENSORFLOW_TYPE or \
                self.executor_service_type == Constants.TRAIN_SCIKITLEARN_TYPE or \
                self.executor_service_type == Constants.TRAIN_AUTOKERAS_TYPE or \
                method_result is None:
            return class_instance

        return method_result
