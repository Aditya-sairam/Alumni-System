# Generated by Django 2.0 on 2020-03-11 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Abstract', models.TextField()),
                ('Unique_name', models.SlugField(unique=True)),
                ('Implementation', models.TextField()),
                ('Technology_Stack', models.TextField()),
                ('Working_ScrrenShots', models.ImageField(blank=True, null=True, upload_to='image/')),
            ],
        ),
    ]
