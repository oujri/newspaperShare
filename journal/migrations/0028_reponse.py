# Generated by Django 2.0.4 on 2018-04-24 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0027_auto_20180424_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomComplet', models.CharField(max_length=50)),
                ('datePublication', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('nombreLike', models.IntegerField(default=0)),
                ('commentaire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.Commentaire')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]