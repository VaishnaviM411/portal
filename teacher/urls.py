
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'teacher'

urlpatterns = [
    path('', views.TeacherPage.as_view(),name = 'TeacherPage'),
   path('scheduleLec/', views.scheduleLec.as_view(),name = 'scheduleLec'),
   path('markAttend/<str:topic>/', views.markAttend.as_view(),name = 'markAttend'),
    path('attendance/<topic>/', views.attendance.as_view(),name = 'attendance'),
]
