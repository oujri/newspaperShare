# Generated by Django 2.0.4 on 2018-04-22 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0020_auto_20180422_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageVideo',
            fields=[
                ('image_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='journal.Image')),
            ],
            bases=('journal.image',),
        ),
    ]
