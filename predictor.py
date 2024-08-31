class Predictor:
    def __init__(self, model, preprocessor):
        self.model = model
        self.preprocessor = preprocessor

    def predict(self, df):
        """Predict anomalies in the data."""
        X = self.preprocessor.transform(df)
        predictions = self.model.predict(X)
        return predictions