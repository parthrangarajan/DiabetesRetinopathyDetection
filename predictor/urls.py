from django.contrib import admin
from django.urls import path, include
from .views import predictor,result


urlpatterns = [
  
    path('home/', predictor, name="home"),
    path('result/<int:pk>',result, name="result")

]
