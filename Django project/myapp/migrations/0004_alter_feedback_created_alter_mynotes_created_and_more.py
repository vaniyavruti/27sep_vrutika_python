# Generated by Django 4.1.4 on 2023-02-12 09:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_feedback_alter_mynotes_created_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='created',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 2, 12, 14, 39, 45, 89090)),
        ),
        migrations.AlterField(
            model_name='mynotes',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 12, 14, 39, 45, 89090)),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 2, 12, 14, 39, 45, 89090)),
        ),
    ]
