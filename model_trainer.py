from sklearn.ensemble import IsolationForest
import joblib

class ModelTrainer:
    def __init__(self, contamination=0.05):
        self.model = IsolationForest(contamination=contamination, n_jobs=-1)

    def train(self, X):
        """Train the model on the training data."""
        self.model.fit(X)

    def save_model(self, filename):
        """Save the trained model to a file."""
        joblib.dump(self.model, filename)

    def load_model(self, filename):
        """Load a saved model from a file."""
        self.model = joblib.load(filename)