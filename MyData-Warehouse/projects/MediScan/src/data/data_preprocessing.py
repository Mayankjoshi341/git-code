import pandas as pd
def main_data_processing(main_df : pd.DataFrame):
    
    symptoms_col = [col for col in main_df.columns if col.startswith("Symptom_")]
    main_df[symptoms_col] = main_df[symptoms_col].fillna("none")
    main_df[symptoms_col] = main_df[symptoms_col].astype(str)
    all_symptoms = set()
    all_symptoms_cleaned = []
    for col in symptoms_col:
        all_symptoms.update(main_df[col].unique())
    all_symptoms.discard("none")
    all_symptoms.discard("Missing value")
    for dieases in all_symptoms:
        dieases = dieases.replace("_" , " ")
        all_symptoms_cleaned.append(dieases)
    X = pd.DataFrame(0 , index = main_df.index, columns= sorted(all_symptoms_cleaned))
    for col in symptoms_col:
        for idx in main_df.index:
            symptoms = main_df.at[idx , col]
            if symptoms not in ["none", "Missing value"]:
                X.at[idx, symptoms] = 1
    return X , symptoms_col

from load_data import load_all_data
all = load_all_data()
x , cols = main_data_processing(all["main"])
print(x)

