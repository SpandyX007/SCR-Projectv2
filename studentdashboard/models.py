from django.db import models
from django.contrib.auth.models import AbstractUser

class studentsignin(models.Model):
    usn_model=models.CharField(max_length=10, default="1BY23XX000")
    name_model=models.CharField(max_length=60, default="xyz", blank=False)
    DateOfBirth_model=models.CharField(max_length=60, default="xyz", blank=False)
    Fname_model=models.CharField(max_length=60, default="abc")
    Mname_model=models.CharField(max_length=60, default="abc")
    class10_model=models.CharField(max_length=60, default="0")
    class12_model=models.CharField(max_length=60, default="0")
    phoneno_model=models.CharField(max_length=13, default="+910000000000")
    department_model=models.CharField(max_length=60, default="CSE")
    section_model=models.CharField(max_length=1, default="A")
    email_model=models.EmailField(max_length=50,blank=False,unique=True)
    password_model=models.CharField(max_length=50,default="1234")
    image_model=models.ImageField(default="NULL")
    desc_model=models.TextField(default="NULL")