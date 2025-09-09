from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import MultiLabelBinarizer 
class SymptomEncoder(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.mlb = MultiLabelBinarizer()

    def fit(self, X, y=None):
        X_list = X.apply(lambda row: [str(sym).strip() for sym in row.dropna()], axis=1)
        self.mlb.fit(X_list)
        return self

    def transform(self, X):
        X_list = X.apply(lambda row: [str(sym).strip() for sym in row.dropna()], axis=1)
        return self.mlb.transform(X_list)
