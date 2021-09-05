from django.shortcuts import render,redirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from .models import course, lecture, teacher

# Create your views here.
class AdminPage(View):
    def get(self,request,template_name='adminpage.html'):
        message={}
        lectures = lecture.objects.all()
        message['lectures']=lectures
        return render(request,template_name,message)

class TeacherPage(View):
    def get(self,request,template_name='teacherpage.html'):
        message={}
        thisteacher = teacher.objects.filter(user = request.user)
        thisteacher = thisteacher[0]
        lectures = lecture.objects.filter(lecturer = thisteacher)
        message['lectures']=lectures
        return render(request,template_name,message)

class scheduleLec(View):
    def get(self,request,template_name='schedule_lec.html'):
        return render(request,template_name)

    def post(self,request,template_name='schedule_lec.html'):
        message={}
        topic = request.POST.get('topic')
        subject = request.POST.get('subject')
        Subject = course.objects.all().filter(code = subject)
        attendance = ["0"]
        date = request.POST.get('date')
        lecturer = teacher.objects.filter(user = request.user)
        try:
            lectureData = lecture(topic=topic,subject=Subject[0],date=date,lecturer=lecturer[0],attendance=attendance)
            lectureData.save()
            message['error']="Lecture scheduled."
        except: 
            message['error']="Something went wrong!"
        return render(request,template_name,message)

class markAttend(View):
    def get(self,request,topic,template_name="mark_attendance.html"):
        message={}
        Lecture = lecture.objects.filter(topic=topic)
        message['lecture']= Lecture[0]
        Course = Lecture[0].subject
        students = Course.course_student
        message['students']= students
        return render(request,template_name,message)

    def post(self,request,topic,template_name="mark_attendance.html"):
        attendance = request.POST.getlist('list')
        lecture.objects.filter(topic=topic).update(attendance=attendance)
        Lecture = lecture.objects.filter(topic=topic)
        print(Lecture)
        print(attendance)
        message={}
        message['lecture']=Lecture
        return render(request,template_name,message)

class attendance(View):

    def get(self,request,topic,template_name="attendance.html"):
        message={}
        Lecture = lecture.objects.filter(topic=topic)
        message['lecture']= Lecture[0]
        Course = Lecture[0].subject
        students = Course.course_student
        message['students']= students
        return render(request,template_name,message)

class approve(View):

    def get(self,request,topic,template_name="approve.html"):
        message={}
        Lecture = lecture.objects.filter(topic=topic)
        message['lecture']= Lecture[0]
        Course = Lecture[0].subject
        students = Course.course_student
        message['students']= students
        return render(request,template_name,message)

    def post(self,request,topic,template_name="approve.html"):
        lecture.objects.filter(topic=topic).update(approved=True)
        return redirect('teacher:AdminPage')