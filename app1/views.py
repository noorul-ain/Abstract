from django.shortcuts import render
from .models import Student, Teacher

# Create your views here.
def home(request):
    student_data = Student.objects.all()
    teacher_data = Teacher.objects.all()
    return render(request, 'home.html', {'teachers':teacher_data, 'students':student_data})


