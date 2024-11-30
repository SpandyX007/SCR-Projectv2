from django.urls import path
from . import views

urlpatterns = [
    path('faculty-dashboard/', views.facultydashboard, name='facultydashboard'),
]
