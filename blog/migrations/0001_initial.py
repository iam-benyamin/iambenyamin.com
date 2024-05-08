# Generated by Django 3.2 on 2023-01-11 17:00

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('discription', models.CharField(max_length=355)),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]