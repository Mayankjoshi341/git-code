from joblib import load
decoder = load(r"C:\Users\mayan\OneDrive\git-projects\git-code\MyData-Warehouse\projects\MEDICSCAN\Encoder.pkl")
print(decoder.inverse_transform([15]))
import pandas as pd
path_file2 = "C:\\Users\\mayan\\Downloads\\symptom_Description.csv"
desc  = pd.read_csv(path_file2)
path_file2.head()
path_file2.info()
path_file2.shape()