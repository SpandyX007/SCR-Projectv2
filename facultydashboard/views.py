from django.shortcuts import render

def facultydashboard(request):
    param={'title':'FacultyDashboard'}
    return render(request, 'facultydashboard.html', param)