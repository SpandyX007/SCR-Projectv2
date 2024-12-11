from django.shortcuts import render,redirect
from .models import studentsignin

def studentdashboard(request):
    param={'title': 'StudentDashboard'}
    return render(request, 'studentdashboard.html',param)

def student(request):
    param={'title':'student'}
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            modelpassword=studentsignin.objects.get(email_model=email)    
            if password==modelpassword.password_model:
                param={'title':'student', 'objects':modelpassword}
                return render(request, 'student.html',param)
        except:
            #print("postexcept")
            #print(password==modelpassword.password_model)
            return render(request,'studentdashboard.html',{'error':'Invalid Email-Id','title':'student'})
    print("normal")
    return render(request, 'student.html',param)

def studentperformance(request):
    params={'title': 'performance'}
    return render(request, 'studentperformance.html', params)