# Generated by Django 2.0 on 2020-03-18 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20200318_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='numb_rem',
            field=models.IntegerField(default=100),
        ),
    ]
