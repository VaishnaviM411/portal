from django.contrib import admin
from .models import course, lecture, teacher
# Register your models here.
admin.site.register(teacher)
admin.site.register(course)
admin.site.register(lecture)