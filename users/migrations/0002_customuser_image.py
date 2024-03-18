# Generated by Django 5.0.3 on 2024-03-10 17:27

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default/user.jpg', upload_to=users.models.CustomUser.image_upload_to),
        ),
    ]
