from django.urls import path
from . import views

urlpatterns = [
    path('admin-panel/', views.adminpanel, name='adminpanel'),
    path('admin-panel-signedin/', views.adminsignedin, name='adminpanelsignedin'),
    path('registered-student/', views.registeredstudent, name='registeredstudent'),
]