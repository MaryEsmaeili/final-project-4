import pandas as pd
from sklearn.preprocessing import StandardScaler

class Preprocessor:
    def __init__(self):
        self.scaler = StandardScaler()

    def fit_transform(self, df):
        """Fit and transform the data for training."""
        df = self._handle_missing_values(df)
        return pd.DataFrame(self.scaler.fit_transform(df), columns=df.columns)

    def transform(self, df):
        """Transform the data for prediction."""
        df = self._handle_missing_values(df)
        return pd.DataFrame(self.scaler.transform(df), columns=df.columns)

    def _handle_missing_values(self, df):
        """Fill missing values with the mean of the column."""
        return df.fillna(df.mean())