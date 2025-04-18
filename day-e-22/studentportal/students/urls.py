from django.urls import path
from .views import student_form, student_list   
urlpatterns = [
    path('', student_form, name='student_form'),
    path('list', student_list, name='student_list'),
   
]