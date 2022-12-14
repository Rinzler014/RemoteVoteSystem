# Generated by Django 4.1.2 on 2022-12-16 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Padron',
            fields=[
                ('cic', models.CharField(max_length=9, primary_key=True, serialize=False, unique=True)),
                ('curp', models.CharField(max_length=18)),
                ('name', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=40)),
                ('momLastName', models.CharField(max_length=40)),
                ('birthDate', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=20)),
                ('phoneNumber', models.CharField(max_length=20)),
                ('postalCode', models.IntegerField()),
                ('town', models.CharField(max_length=40)),
                ('estate', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=2)),
                ('secQuest1', models.CharField(max_length=80)),
                ('secAns1', models.CharField(max_length=20)),
                ('secQuest2', models.CharField(max_length=80)),
                ('secAns2', models.CharField(max_length=20)),
                ('secQuest3', models.CharField(max_length=80)),
                ('secAns3', models.CharField(max_length=20)),
                ('faceImage1', models.ImageField(upload_to='images/')),
                ('faceImage2', models.ImageField(upload_to='images/')),
                ('faceImage3', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
