from django.contrib import admin
from .models import facultysignin
# Register your models here.
class facultysigninadmin(admin.ModelAdmin):
    list_display=("staffid_model","name_model","phoneno_model","department_model","currsection_model",
    "email_model","password_model","image_model")

admin.site.register(facultysignin,facultysigninadmin)