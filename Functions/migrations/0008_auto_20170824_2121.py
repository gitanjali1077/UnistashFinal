# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-24 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Functions', '0007_compsem1_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='compsem1',
            name='branch',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compsem1',
            name='semester',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]