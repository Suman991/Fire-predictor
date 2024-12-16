from flask import Flask, render_template, request, url_for ,redirect
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import numpy as np
import pandas as pd
import pickle


application=Flask(__name__)


# unpickle Ridge Regressor and Standard scaler pickle file
ridge_model=pickle.load(open(r'model\ridge.pkl','rb'))
standard_scaler=pickle.load(open(r'model\scaler.pkl','rb'))


@application.route('/',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('Temperature'))
        RH=float(request.form.get('RH'))
        Ws=float(request.form.get('Ws'))
        Rain=float(request.form.get('Rain'))
        FFMC=float(request.form.get('FFMC'))
        DMC=float(request.form.get('DMC'))
        ISI=float(request.form.get('ISI'))
        Classes=float(request.form.get('Classes'))
        Region=float(request.form.get('Region'))
        
            # Scaling all inputs
        new_data_scaled=standard_scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes,Region]])
            # predicting FWI
        result=ridge_model.predict(new_data_scaled)

        return render_template('index.html',results=result[0])
    else:
        return render_template("index.html",results=None)

        

if __name__=='__main__':
    application.run(debug=True)