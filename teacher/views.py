from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

# Create your views here.
class TeacherPage(View):
    def get(self,request,template_name='teacherpage.html'):
        return render(request,template_name)