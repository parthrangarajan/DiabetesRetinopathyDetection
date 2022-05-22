from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class DiabetesData(models.Model):
    name = models.CharField(max_length=256,default="")
    pregnancies = models.CharField(max_length=256, default="")
    glucose = models.CharField(max_length=256, default="")
    blood_pressure = models.CharField(max_length=256, default="")
    skin_thickness = models.CharField(max_length=256, default="")
    insulin = models.CharField(max_length=256, default="")
    BMI = models.CharField(max_length=256, default="")
    DPF = models.CharField(max_length=256, default="")
    age = models.CharField(max_length=256, default="")

    def __str__(self):
        return self.name