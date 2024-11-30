from django.contrib import admin
from .models import studentsignin
# Register your models here.
class studentsigninadmin(admin.ModelAdmin):
    list_display=("usn_model","name_model","Fname_model","Mname_model","class10_model","class12_model","desc_model","DateOfBirth_model","phoneno_model","department_model","section_model",
    "email_model","password_model","image_model")

admin.site.register(studentsignin,studentsigninadmin)