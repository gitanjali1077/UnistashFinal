# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-28 13:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Functions', '0011_auto_20170827_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(max_length=200, upload_to=b'')),
            ],
        ),
    ]
