# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 10:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOVIE_REVIEW', '0007_actors_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='directors',
            name='description',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]