# Generated by Django 2.0.4 on 2018-04-22 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0022_video_imagevideo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='imageVideo',
        ),
    ]
