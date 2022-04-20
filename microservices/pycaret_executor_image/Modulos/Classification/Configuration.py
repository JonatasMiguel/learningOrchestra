from pycaret import classification
from SetupParameterHandler import ParametersSetupHandler

class ClassificationConfig:
    def __init__(self, id, data_set):
        self.id = id
        self.data_set = data_set


    def createConfig(self,param: dict):
        ph = ParametersSetupHandler(param)
        p = ph.treat()
        _ = classification.setup(**p)
        classification.save_config(f'{self.id}.pkl') 
        

