# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 15:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gost_app', '0002_auto_20160415_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='ulogovan',
            field=models.BooleanField(default=False),
        ),
    ]
