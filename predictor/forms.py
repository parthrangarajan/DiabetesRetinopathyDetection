from django import forms
from .models import *

class PredictionForm(forms.ModelForm):

    class Meta:
        model = DiabetesData
        fields= ['name', 'pregnancies', 'glucose', 'blood_pressure',  'skin_thickness', 'insulin', 'BMI', 'DPF', 'age']
