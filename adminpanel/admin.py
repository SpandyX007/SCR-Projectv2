from django.contrib import admin
from .models import adminsignin
# Register your models here.
class adminsigninadmin(admin.ModelAdmin):
    list_display=("adminid_model","name_model","phoneno_model",
    "email_model","password_model","image_model")

admin.site.register(adminsignin,adminsigninadmin)