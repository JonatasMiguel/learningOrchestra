from pycaret.datasets import get_data

class ParametersSetupHandler:
    def __init__(self,param: dict):
        self.param = param

    def treat(self):
        self.param['data'] = get_data("titanic") #todo: aqui aplicar a busca do dataset no learning
        self.param['silent'] = True
        return self.param
        