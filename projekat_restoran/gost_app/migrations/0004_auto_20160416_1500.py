# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gost_app', '0003_guest_ulogovan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='height_field',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='width_field',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
