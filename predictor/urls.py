from django.contrib import admin
from django.urls import path, include
from .views import predictor, result


urlpatterns = [
    path('predictor', predictor, name="predictor"),
    path('result/<int:id>',result, name="result")

]
