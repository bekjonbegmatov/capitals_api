from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('' , views.getRoutes , name="get Routes"),
    path('country/all', views.getCountry, name="get Countries"),
    path('export/excel' , views.export_excel , name="Export Exsel")
]
