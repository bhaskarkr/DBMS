# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOVIE_REVIEW', '0003_auto_20171015_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]