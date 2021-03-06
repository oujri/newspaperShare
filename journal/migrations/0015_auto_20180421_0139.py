# Generated by Django 2.0.4 on 2018-04-21 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0014_auto_20180420_1822'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomComplet', models.CharField(max_length=50)),
                ('datePublication', models.DateTimeField(auto_now_add=True)),
                ('message', models.TextField()),
                ('nombreLike', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameField(
            model_name='image',
            old_name='uploaded_at',
            new_name='datePublication',
        ),
        migrations.AddField(
            model_name='news',
            name='nombreVue',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commentaire',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.News'),
        ),
    ]
