from django.shortcuts import render
from django.http import HttpResponse
from studentdashboard.models import studentsignin

def roothome(request):
    students=studentsignin.objects.all()
    print(students)
    param={'title':'HOME','students':students}
    return render(request, 'mainhome.html', param)

def contactus(request):
    param={'title':'ContactUs'}
    return render(request, 'contactus.html',param)

def aboutus(request):
    param={'title':'AboutUs'}
    return render(request, 'aboutus.html',param)

def explore(request):
    param={'title':'Explore'}
    return render(request,'explore.html',param)