
import numpy as np
import pandas as pd
import joblib

def hypothyroid_pred(data_lst):
    scale_max = pd.read_csv('hypodata_max_for_scaling.csv')
    scale_min = pd.read_csv('hypodata_min_for_scaling.csv')
    model = joblib.load("neural_network_numeric_data_model3.pkl")
    hypothyroid_classes = {0: 'No hypothyroid disease',
               1: 'primary hypothyroid',
               2: 'compensated hypothyroid',
               3: 'secondary hypothyroid'}
    data_arr = np.array(data_lst).reshape(-1, 6)
    d_scaled = np.subtract(data_arr,scale_min.values)/np.subtract(scale_max.values, scale_min.values)
    pred1 = model.predict(d_scaled)
    result = []
    for i in pred1:
        result.append(hypothyroid_classes[i])
    return result
