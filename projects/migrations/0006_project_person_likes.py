# Generated by Django 2.0 on 2020-03-18 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='Person_Likes',
            field=models.IntegerField(default=0),
        ),
    ]
