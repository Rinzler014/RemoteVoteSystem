# Generated by Django 4.1.2 on 2022-12-13 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('census', '0005_rename_states_locations_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=18)),
                ('password', models.CharField(max_length=14)),
            ],
        ),
    ]
