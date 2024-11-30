from django.db import models
from django.contrib.auth.models import AbstractUser

class facultysignin(models.Model):
    staffid_model=models.CharField(max_length=10, default="1BY23XX000")
    name_model=models.CharField(max_length=60, default="xyz", blank=False)
    phoneno_model=models.CharField(max_length=13, default="+910000000000")
    department_model=models.CharField(max_length=60, default="CSE")
    currsection_model=models.CharField(max_length=1, default="A")
    email_model=models.EmailField(max_length=50,blank=False,unique=True)
    password_model=models.CharField(max_length=50)
    image_model=models.ImageField(default="NULL")
