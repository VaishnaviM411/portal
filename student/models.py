from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models import OneToOneField
# Create your models here.
class student(models.Model):
    user: OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.first_name+" "+self.user.last_name