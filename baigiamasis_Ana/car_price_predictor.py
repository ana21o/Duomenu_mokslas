import joblib
import numpy as np

class CarPricePredictor:
    def __init__(self, model_path):
        self.model = joblib.load(model_path)

    def predict(self, X):
        return self.model.predict(X)
    

    