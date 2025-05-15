from django.shortcuts import render, redirect
from .models import Student,Course,Teacher
from django.contrib.auth import login, logout, authenticate

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

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_teacher:
                return redirect('teacher_dashboard')
            elif user.is_student:
                return redirect('student_dashboard')
        else:
            return render(request, 'core/login.html', {'error': 'invalid credentials'})
    return render(request, 'core/login.html')

def logout_view(request):
    logout(request)
    return redirect('home')