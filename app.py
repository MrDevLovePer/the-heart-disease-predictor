from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('model2.sav', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':

        #Age
        age = float(request.form['age'])

        #Sex
        sex = request.form['sex']
        if sex==1:
            sex=1
        elif sex==0:
            sex=0

        #chest pain type
        cp = request.form['cp']
        if cp=='0':
            cp=0

        elif cp=='1':
            cp=1

        elif cp=='2':
            cp=2

        elif cp=='3':
            cp=3

        #Resting blood pressure
        trestbps = float(request.form['trestbps'])

        #Cholstral
        chol = float(request.form['chol'])

        #Fasting blood sugar
        fbs = request.form['fbs']
        if fbs=='Yes':
            fbs=1
        else:
            fbs=0

        #Resting Electro cardiograpghic Results
        restecg = request.form['restecg'] 
        if restecg=='0':
            restecg=0

        elif restecg=='1':
            restecg=1

        elif restecg=='2':
            restecg=2

        #Maximum heartrate achieved
        thalach	 = float(request.form['thalach'])  

        #Exercise included angina
        exang	 = request.form['exang']       
        if exang=='Yes':
            exang=1
        else:
            exang=0
        
        #ST depression induced by exercise relative to rest
        oldpeak	 = float(request.form['oldpeak'])        
        
        
        slope	 = request.form['slope']    
        if slope=='0':
            slope=0

        elif slope=='1':
            slope=1

        elif slope=='2':
            slope=2
        
        
        ca	 = request.form['ca']     
        if ca=='0':
            ca=0

        elif ca=='1':
            ca=1

        elif ca=='2':
            ca=2

        elif ca=='3':
            ca=3
        
        elif ca=='4':
            ca=4
        
        
        thal	 = request.form['thal']     
        if thal=='0':
            thal=0

        elif thal=='1':
            thal=1

        elif thal=='2':
            thal=2

        elif thal=='3':
            thal=3

        
        prediction=model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        output=prediction
        if output==[1]:
            return render_template('index.html',prediction_texts="Sorry, you have to visit doctor")
        else:
            return render_template('index.html',prediction_text="You need not to visit the doctor")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

