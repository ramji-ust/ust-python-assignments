from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Student
# Create your views here.
@login_required
def student_form(request):
    print(request.POST)
    if(request.method == 'POST'):
        name = request.POST.get('name','unknown')
        age = request.POST.get('age','unknown')
        class_name = request.POST.get('class_name','unknown')
        marks = request.POST.get('marks','unknown')


        Student.objects.create(name=name, age=age, class_name=class_name, marks=marks)

        return redirect('student_list')
    return render(request, 'students/student_form.html')

@login_required
def student_list(request):
    context = {
        'students': Student.objects.all()
    }
    return render(request, 'students/student_list.html', context) 
