
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path('', views.StudentPage.as_view(),name = 'StudentPage'),
   
]
