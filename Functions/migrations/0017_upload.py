# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-28 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Functions', '0016_auto_20170828_2325'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
    ]
