from pathlib import Path
import os
from constants import Constants


class PlotterClassification:
    from pycaret import classification

    def __init__(self, name: str, plot: str, model: str):
        self.__name = name
        self.__plot = plot
        self.__model = model

    def create_plot(self) -> None:
        try:
            with open('resultados.txt', 'a') as f:
                f.write('Tentando carregar\n')
                model = self.classification.load_model(self.__model)
                f.write('Tentando plotar\n')
                self.classification.plot_model(model, self.__plot, save=True)
        except Exception as error:
            with open('resultados.txt', 'a') as f:
                f.write(f'pau 1{error.__cause__}\n')
                f.write(f'pau 1{repr(error)}\n')
                f.write(f'pau 1{str(error)}\n')

    def rename_file(self) -> None:
        os.rename(PlotterClassification.get_path_volume(PlotterClassification.get_name_default(self.__plot)),
                  PlotterClassification.get_path_volume(self.__name))

    def get_path_plot(self) -> str:
        return PlotterClassification.get_path_volume(self.__name)

    @staticmethod
    def get_path_volume(filename: str) -> str:
        return f'/usr/src/code_executor/{filename}'

    @staticmethod
    def get_name_default(plot: str):
        if plot == "auc":
            return "Area Under the Curve.png"
        elif plot == "threshold":
            return "Discrimination Threshold.png"
        elif plot == "pr":
            return "Precision Recall Curve.png"
        elif plot == "confusion_matrix":
            return "Confusion Matrix.png"
        elif plot == "error":
            return "Class Prediction Error.png"
        elif plot == "class_report":
            return "Classification Report.png"
        elif plot == "boundary":
            return "ADecision Boundary.png"
        elif plot == "rfe":
            return "Recursive Feature Selection.png"
        elif plot == "learning":
            return "Learning Curve.png"
        elif plot == "manifold":
            return "Manifold Learning.png"
        elif plot == "calibration":
            return "Calibration Curve.png"
        elif plot == "vc":
            return "Validation Curve.png"
        elif plot == "dimension":
            return "Dimension Learning.png"
        elif plot == "feature":
            return "Feature Importance.png"
        elif plot == "parameter":
            return "Model Hyperparameter.png"
