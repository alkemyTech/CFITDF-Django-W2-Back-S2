# Generated by Django 5.2.1 on 2025-05-28 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Active'),
        ),
    ]
