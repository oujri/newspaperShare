# Generated by Django 2.0.4 on 2018-05-01 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0041_auto_20180501_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='active',
        ),
    ]