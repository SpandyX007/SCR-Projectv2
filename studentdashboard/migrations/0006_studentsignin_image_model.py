# Generated by Django 5.0.4 on 2024-11-20 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboard', '0005_remove_studentsignin_image_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsignin',
            name='image_model',
            field=models.ImageField(default='NULL', upload_to=''),
        ),
    ]