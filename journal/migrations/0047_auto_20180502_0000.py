# Generated by Django 2.0.4 on 2018-05-01 23:00

from django.db import migrations, models
import journal.models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0046_auto_20180501_1641'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to=journal.models.PathAndRename('images/2018/05/02')),
        ),
    ]