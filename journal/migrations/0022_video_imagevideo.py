# Generated by Django 2.0.4 on 2018-04-22 03:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0021_imagevideo'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='imageVideo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='journal.ImageVideo'),
            preserve_default=False,
        ),
    ]
