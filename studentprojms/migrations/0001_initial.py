# Generated by Django 2.0.5 on 2018-09-22 13:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projectId', models.IntegerField(default=0)),
                ('numreviews', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=128)),
                ('fid', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=10)),
                ('subject', models.CharField(max_length=128)),
                ('projectId', models.IntegerField(default=0)),
                ('userid', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projname', models.CharField(max_length=128)),
                ('projdesc', models.CharField(max_length=1000)),
                ('studname', models.CharField(max_length=128)),
                ('stuid', models.CharField(max_length=12)),
                ('branch', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=20)),
                ('status', models.IntegerField(default=0)),
                ('contact', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=20)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2018, 9, 22, 13, 44, 40, tzinfo=utc))),
            ],
        ),
    ]
