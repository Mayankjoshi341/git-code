import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]   # MediScan/
DATA_DIR = BASE_DIR / "data" / "raw-data"

def load_all_data():
    return {
        "main": pd.read_csv(DATA_DIR / "dataset.csv"),
        "severity": pd.read_csv(DATA_DIR / "Symptom-severity.csv"),
        "description": pd.read_csv(DATA_DIR / "symptom_Description.csv"),
        "precaution": pd.read_csv(DATA_DIR / "symptom_precaution.csv"),
    }
