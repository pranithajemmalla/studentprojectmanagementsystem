# Generated by Django 2.0.5 on 2018-09-27 20:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('studentprojms', '0009_auto_20180927_2356'),
    ]

    operations = [
        migrations.CreateModel(
            name='studmarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuid', models.IntegerField(default=0)),
                ('m1', models.IntegerField(default=0)),
                ('m2', models.IntegerField(default=0)),
                ('m3', models.IntegerField(default=0)),
                ('m4', models.IntegerField(default=0)),
                ('m5', models.IntegerField(default=0)),
                ('m6', models.IntegerField(default=0)),
                ('m7', models.IntegerField(default=0)),
                ('m8', models.IntegerField(default=0)),
                ('m9', models.IntegerField(default=0)),
                ('m10', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 20, 44, 5, tzinfo=utc)),
        ),
    ]
