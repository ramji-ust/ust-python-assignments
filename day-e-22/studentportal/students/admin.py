from django.contrib import admin
from .models import Student
# Register your models here.

admin.site.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'class_name', 'marks')
    list_filter = ('class_name',)
    ordering = ('name',)