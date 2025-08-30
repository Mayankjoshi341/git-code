import pandas as pd
import streamlit as st
from joblib import load
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load the pre-trained model pipeline
def main():
    model_file = st.file_uploader("drag or enter the model file here")
    model = load(model_file)
    perprocessor_step_name = str( st.text_input("Enter the pipline preporces step name"))
    data = st.file_uploader("Drag or enter the file here ")
    data = pd.read_csv(data)
    columns_in_data = data.columns.tolist()
    target = st.selectbox("select the target from the data" , columns_in_data)
    features = st.multiselect("select the features in the data " ,columns_in_data)
    perinfo = {}
    st.sidebar.subheader(f"Enter related details:")
    for col in features:
        if data[col].nunique()< 10 :
            list = data[col].unique().tolist()
            value_of_input = st.sidebar.selectbox(f"select {col}" , list)
            perinfo[col] = value_of_input
        elif data[col].nunique()>= 10 and data[col].dtype == 'int64':
            min_value = int(data[col].min())
            max_value = int(data[col].max())
            name_of_input = str(data[col].name)
            value_of_input = st.slider(f"select {name_of_input}" , min_value , max_value , int(data[col].mean()))
            perinfo[name_of_input] = value_of_input
        elif data[col].nunique()>= 10 and data[col].dtype == 'object':
            name_of_input = data[col].name
            value_of_input = st.selectbox(f"select {name_of_input}" , data[col].unique().tolist())
            perinfo[name_of_input] = value_of_input
    st.subheader("Employee details you entered:")
    st.dataframe(pd.DataFrame(perinfo , index=[0]))
    input_data = pd.DataFrame(perinfo)
    print(perinfo)
    if st.button(f"predict {target}"):
       result = model.predict(input_data)[0]
       if result == 1:
          st.success(f"The model predict yess")
       elif result == 0:
          st.error("model predict no")
       else:
          st.success(result)
                    

main()