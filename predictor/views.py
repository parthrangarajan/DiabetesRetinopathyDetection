from django.shortcuts import redirect, render
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from django.views.generic import  CreateView
from .forms import PredictionForm
from .models import *
import csv
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors




# Create your views here.
def predictor(request):
    forms_id = None
    
    form= PredictionForm(request.POST )
    context = {'form':form }
    if form.is_valid():
        form.save()
        x = form.save()
        forms_id = x.pk
        return redirect(f'/result/'+ forms_id)
    return render(request,'screening.html',context)
    

def result(request,pk):
    data = pd.read_csv(r"/home/husain/Projects/IBM-mini-project/predictor/archive/diabetes.csv")
    pk = int(pk)
    X = data.drop("Outcome", axis=1)
    Y = data["Outcome"]

    values = DiabetesData.objects.get(pk=pk)

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    val1 = float(values.pregnancies)
    val2 = float(values.glucose)
    val3 = float(values.blood_pressure)
    val4 = float(values.skin_thickness)
    val5 = float(values.insulin)
    val6 = float(values.pregnancies)
    val7 = float(values.pregnancies)
    val8 = float(values.pregnancies)

    pred = model.predict([[val1,val2,val3,val4,val5,val6,val7,val8]])

    result=""
    if pred == [1]:
        result = "POSITIVE"
    else:
        result="NEGATIVE"

    return render(request, 'result.html', {'result':result},{'pk':pk}) 

def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800')

def result_pdf(request,pk):  
    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)

    fileName = 'Diabetes_retinopathy_results.pdf'
    documentTitle = 'Diabetes retinopathy'
    title = 'Diabetic retinopathy report'
    symptoms_title = 'Diabetes retinopathy symptoms'

    symptoms = [
    'Spots or dark strings floating in your vision (floaters)',
    'Blurred vision.',
    'Fluctuating vision.',
    'Dark or empty areas in your vision.',
    'Vision loss.'
    ]

    pegnancies = 'pregnancies :'
    glucose = 'glucose :'
    blood_pressure = 'blood pressure :'
    skin_thickness = 'skin thickness :'
    insulin = 'insulin :'
    BMI = 'bmi :'
    DPF = 'Diabetes Pedigree function :'
    age = 'age :'
    
    patient_data = DiabetesData.objects.get(pk=pk)
    
    preg_data = patient_data.pregnancies
    glucose_data = patient_data.glucose
    blood_pressure = patient_data.blood_pressure
    skin_thickness = patient_data.skin_thickness
    insulin = patient_data.insulin
    BMI = patient_data.BMI
    DPF = patient_data.DPF
    age = patient_data.age


    drawMyRuler(pdf)
    pdfmetrics.registerFont(TTFont('abc', 'SakBunderan.ttf'))
    pdf.setFont('abc', 36)
    pdf.drawCentredString(300, 770, title)

    pdf.setFillColorRGB(0, 0, 255)
    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290,720, symptoms_title)
    pdf.line(30, 710, 550, 710)

    text = pdf.beginText(40, 680)
    text.setFont("Courier", 18)
    text.setFillColor(colors.red)
    for line in symptoms:
        text.textLine(line)

    pdf.drawText(text)

    pdf.save()
