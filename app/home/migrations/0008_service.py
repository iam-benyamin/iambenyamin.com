# Generated by Django 3.2 on 2022-06-06 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icone', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=150)),
                ('date', models.DateTimeField()),
            ],
        ),
    ]