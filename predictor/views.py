from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from .models import *


# Create your views here.
def predictor(request):

    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])

    factor_values = DiabetesData(
        user=request.user,
        pregnancies=val1,
        glucose=val2,
        blood_pressure=val3,
        skin_thickness = val4, 
        insulin=val5,
        BMI=val6,
        DPF=val7,
        age=val8
        )

    factor_values.save()
    scan_id = factor_values.id

    return render(request,'screening.html', {'id':scan_id})

def result(request,id):
    data = pd.read_csv(r"/home/husain/Projects/IBM-mini-project/predictor/archive/diabetes.csv")
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]

    values = DiabetesData.objects.get(id=id)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = values.pregnancies
    val2 = values.glucose
    val3 = values.blood_pressure
    val4 = values.skin_thickness
    val5 = values.insulin
    val6 = values.pregnancies
    val7 = values.pregnancies
    val8 = values.pregnancies

    pred = model.predict([[]])

    result=""
    if pred == [1]:
        result = "POSITIVE"
    else:
        result="NEGATIVE"

    return render(request, 'result.html', {'result':result}) 