# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-14 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='Email',
            field=models.EmailField(max_length=254),
        ),
    ]
