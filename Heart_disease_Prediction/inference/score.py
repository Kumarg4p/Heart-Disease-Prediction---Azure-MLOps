import os
import sys
import numpy as np
import pandas as pd
import joblib
#from sklearn.externals import joblib

import math
from azureml.core.model import Model
from azureml.monitoring import ModelDataCollector
import json
import re
import traceback
import logging


'''
Inference script for Heart disease prediction:

'''

def init():
    '''
    Initialize required models:
        Get the heart Model from Model Registry and load
    '''
    global prediction_dc
    global model
    prediction_dc = ModelDataCollector("Heart", designation="predictions", feature_names=["age","sex", "cp","trestbps","chol", "fbs", "restecg","thalach","exang", \
                                                                                          "oldpeak", "slope", "ca", "thal", "target" ])
                                                           
    model_path = Model.get_model_path('Heart')
    model = joblib.load(model_path+"/"+"Heart_model.pkl")
    print('Heart Diseas Prediction model loaded...')

def create_response(predicted_lbl):
    '''
    Create the Response object
    Arguments :
        predicted_label : Predicted Heart disease
    Returns :
        Response JSON object
    '''
    resp_dict = {}
    print("Predicted target : ",predicted_lbl)
    resp_dict["predicted_target"] = str(predicted_lbl)
    return json.loads(json.dumps({"output" : resp_dict}))

def run(raw_data):
    '''
    Get the inputs and predict the Heart disease
    Arguments : 
        raw_data : SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm
    Returns :
        Predicted Heart disease
    '''
    try:
        data = json.loads(raw_data)
        age = data['age']
        sex = data['sex']
        cp = data['cp']
        trestbps = data['trestbps']
        chol = data['chol']
        fbs = data['fbs']
        restecg = data['restecg']
        thalach = data['thalach']
        exang = data['exang']
        oldpeak = data['oldpeak']
        slope = data['slope']
        ca = data['ca']
        thal = data['thal']
        in_data = [[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]]
        in_data = pd.get_dummies(in_data, columns=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])
        predicted_target = model.predict(in_data)[0]
        prediction_dc.collect([age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,predicted_target])
        return create_response(predicted_target)
    except Exception as err:
        traceback.print_exc()
