# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOVIE_REVIEW', '0009_movies_trailer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='description',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
