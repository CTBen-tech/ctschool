from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('student/<int:student_id>/courses/', views.student_courses, name='student_courses'),
]