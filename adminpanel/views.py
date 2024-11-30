from django.shortcuts import render
from .models import adminsignin
from studentdashboard.models import studentsignin

def adminpanel(request):
    params={'title':'admin'}
    return render(request, 'adminpanel.html', params)

def adminsignedin(request):
    param={'title':'ADMIN'}
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        try:
            modelpassword=adminsignin.objects.get(email_model=email)    
            if password==modelpassword.password_model:
                param={'title':'ADMIN', 'objects':modelpassword}
                return render(request, 'adminpanelsignedin.html',param)
        except:
            #print("postexcept")
            #print(password==modelpassword.password_model)
            return render(request,'adminpanel.html',{'error':'Invalid Email-Id OR Password!','title':'ADMIN'})
    print("normal")
    return render(request, 'adminpanel.html',param)

def registeredstudent(request):
    params={'title':'Thank You'}
    if request.method=="POST":
        name=request.POST.get('name')
        DateOfBirth=request.POST.get('DOB')
        studentimage=request.POST.get('studentimage')
        Fname=request.POST.get('fathername')
        Mname=request.POST.get('mothername')
        phno=request.POST.get('phonenumber')
        class10=request.POST.get('10marks')
        class12=request.POST.get('12marks')
        deptname=request.POST.get('deptname')
        collegemailid=request.POST.get('collegemailid')
        desc=request.POST.get('message')
        contactdata=studentsignin(name_model=name, DateOfBirth_model=DateOfBirth, Fname_model=Fname, Mname_model=Mname, phoneno_model=phno, department_model=deptname, email_model=collegemailid, desc_model=desc, image_model=studentimage, class10_model=class10, class12_model=class12)
        contactdata.save()
        return render(request, 'thankyoustudentregister.html',params)