# Generated by Django 2.0 on 2020-02-29 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0004_session_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='slug',
        ),
    ]
