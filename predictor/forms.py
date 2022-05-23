from django import forms
from .models import *

class PredictionForm(forms.ModelForm):

    class Meta:
        model = DiabetesData
        fields= ['name', 'pregnancies', 'glucose', 'blood_pressure',  'skin_thickness', 'insulin', 'BMI', 'DPF', 'age']
        widgets={
            'name' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'pregnancies': forms.TextInput(attrs={'class':'form-control py-2'}),
            'glucose' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'blood_pressure' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'skin_thickness' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'insulin' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'BMI' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'DPF' : forms.TextInput(attrs={'class':'form-control py-2'}),
            'age' : forms.TextInput(attrs={'class':'form-control py-2'})
        }