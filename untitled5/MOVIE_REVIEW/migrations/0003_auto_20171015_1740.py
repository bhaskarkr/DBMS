# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-15 17:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MOVIE_REVIEW', '0002_auto_20171015_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actors',
            name='pic',
            field=models.URLField(blank=True, default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLV4iTgBnY8EbNX9fIe7ijBCwyTKLTZW-NNLjUbiPiNmyxhd-fXw', max_length=500),
        ),
        migrations.AlterField(
            model_name='directors',
            name='pic',
            field=models.URLField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRLV4iTgBnY8EbNX9fIe7ijBCwyTKLTZW-NNLjUbiPiNmyxhd-fXw'),
        ),
    ]
