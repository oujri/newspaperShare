# Generated by Django 2.0.4 on 2018-04-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0037_auto_20180429_1906'),
    ]

    operations = [
        migrations.AddField(
            model_name='publisher',
            name='google',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='publisher',
            name='linkedin',
            field=models.URLField(blank=True),
        ),
    ]