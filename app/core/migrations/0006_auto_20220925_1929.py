# Generated by Django 3.2.15 on 2022-09-25 17:29

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200514_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivedleave',
            name='image',
            field=models.ImageField(default='profilepics/ydl-logo.png', upload_to=core.models.upload_to, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='leave',
            name='image',
            field=models.ImageField(default='profilepics/ydl-logo.png', upload_to=core.models.upload_to, verbose_name='Image'),
        ),
    ]