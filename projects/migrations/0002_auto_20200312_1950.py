# Generated by Django 2.0 on 2020-03-12 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Working_ScrrenShots',
        ),
        migrations.AddField(
            model_name='project',
            name='Working_ScreenShots',
            field=models.ImageField(blank=True, null=True, upload_to='media/image/'),
        ),
    ]
