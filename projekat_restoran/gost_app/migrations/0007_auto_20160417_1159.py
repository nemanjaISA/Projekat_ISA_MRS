# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 09:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gost_app', '0006_auto_20160417_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
    ]
