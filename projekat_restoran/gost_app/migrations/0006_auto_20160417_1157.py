# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-17 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gost_app', '0005_auto_20160416_2218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='email',
            field=models.EmailField(max_length=200),
        ),
    ]
