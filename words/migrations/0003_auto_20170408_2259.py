# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-08 22:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_auto_20170408_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='name',
            field=models.CharField(default=0, max_length=200),
        ),
    ]
