from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User

# Create your views here.
class landing(View):
    def get(self, request, template_name='landing.html'):
        return render(request, template_name)

class Login(View):
    def get(self, request, template_name='login.html'):
        return render(request,template_name)

    def post(self, request, template_name='login.html'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        group = None
        if user is not None:
            if user.is_active:
                login(request, user)
                group = user.groups.all()[0].name
                if group == 'student_group':
                    return redirect('student:StudentPage')
                if group == 'teacher_group':
                    return redirect('teacher:TeacherPage')
                else:
                    return render(request, 'landing.html')
            else:
                return render(request, template_name, {'error_message': 'Your account has been disabled'})
        else:
            return render(request, template_name, {'error_message': 'Invalid Login'})



class Logout(View):
    def get(self, request):
        logout(request)
        return render(request, 'landing.html')
        