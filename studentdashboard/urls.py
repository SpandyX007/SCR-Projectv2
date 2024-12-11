from django.urls import path
from . import views

urlpatterns = [
    path('student-dashboard/', views.studentdashboard, name='studentdashboard'),
    path('student/', views.student, name='student'),
    path('student-performance/', views.studentperformance, name='studentperformance'),
]