from django.shortcuts import render
from .models import Student,Course,Teacher

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'core/course_list.html', {'courses': courses})

def student_courses(request, student_id):
    student =Student.objects.get(student_id = student_id)
    courses = Student.courses.all()
    return render(request, 'core/student_courses.html', {'student': student, 'courses': courses})
