# Generated by Django 2.0.4 on 2018-04-29 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0034_news_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='lien',
        ),
        migrations.AddField(
            model_name='publisher',
            name='photoDeProfil',
            field=models.ForeignKey(default=59, on_delete=models.SET(59), to='journal.Image'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='journal/uploads/images/'),
        ),
    ]