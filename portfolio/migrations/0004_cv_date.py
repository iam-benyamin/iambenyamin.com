# Generated by Django 3.2 on 2023-02-04 15:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_portfolio_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
