from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.IntegerField(unique=True)
    email =models.EmailField(unique=True)

    def _str_(self):
        return self.name
    
class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses')
    students = models.ManyToManyField('Student', related_name='courses')

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.IntegerField(unique=True)
    grade = models.IntegerField()
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    is_present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.course.title} - {self.date}"
    
class Fee(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.student.name} - {self.amount}"


    

