# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-06 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskbot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelplan',
            name='breakfast',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='spa',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='travelplan',
            name='wifi',
            field=models.BooleanField(default=False),
        ),
    ]
