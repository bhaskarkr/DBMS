# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOVIE_REVIEW', '0004_movies_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='actors',
            name='dob',
            field=models.DateField(default='2000-01-01'),
        ),
    ]
