from typing import DefaultDict
from django.db import models
from django.db.models import OneToOneField
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING


# Create your models here.
class teacher(models.Model):
    user: OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.first_name+" "+self.user.last_name   

class course(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    course_teacher = models.ForeignKey(teacher, on_delete=CASCADE)
    course_student = models.JSONField(default=list)
    def __str__(self):
        return self.name

class lecture(models.Model):
    topic = models.CharField(max_length=20)
    subject = models.ForeignKey(course, on_delete=CASCADE)
    date = models.DateTimeField()
    attendance = models.JSONField(default=list)
    lecturer = models.ForeignKey(teacher, on_delete=DO_NOTHING)
    def __str__(self):
        return self.topic