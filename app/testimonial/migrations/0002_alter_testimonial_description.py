# Generated by Django 3.2 on 2022-07-21 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='description',
            field=models.TextField(max_length=180),
        ),
    ]