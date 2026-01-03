import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def fit_scaler(df):
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(df)

    x_scaled_df = pd.DataFrame(x_scaled, columns=df.columns , index=df.index)

    return scaler, x_scaled_df

def transform_scaler(scaler, df):
    x_scaled = scaler.transform(df)
    x_scaled_df = pd.DataFrame(x_scaled, columns=df.columns , index=df.index)
    return x_scaled_df