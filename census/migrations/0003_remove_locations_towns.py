# Generated by Django 4.1.2 on 2022-12-13 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0002_locations_securityquestions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locations',
            name='towns',
        ),
    ]
