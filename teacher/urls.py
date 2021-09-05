
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.TeacherPage.as_view(),name = 'TeacherPage'),
   
]
